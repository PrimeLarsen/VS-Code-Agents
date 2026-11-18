import re
import sys
import tomllib
from pathlib import Path

root = Path(__file__).resolve().parents[2]
problems = []

for path in sorted(root.rglob("*")):
    if ".git" in path.parts or not path.is_file():
        continue
    if path.suffix == ".md":
        text = path.read_text(encoding="utf-8")
        fences = sum(1 for line in text.splitlines() if line.lstrip().startswith("```"))
        if fences % 2:
            problems.append(f"{path.relative_to(root)}: unbalanced code fences")
        for match in re.finditer(r"\[[^\]]*\]\(([^)]+)\)", text):
            target = match.group(1).split("#", 1)[0]
            if not target or target.startswith(("http://", "https://", "mailto:")):
                continue
            if not (path.parent / target).resolve().exists():
                problems.append(f"{path.relative_to(root)}: broken relative link -> {target}")
    elif path.suffix == ".toml":
        try:
            tomllib.loads(path.read_text(encoding="utf-8"))
        except tomllib.TOMLDecodeError as exc:
            problems.append(f"{path.relative_to(root)}: invalid TOML ({exc})")

if problems:
    print("\n".join(problems))
    sys.exit(1)

print("docs check OK: markdown links and code fences valid, TOML files parse")
