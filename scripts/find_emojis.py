import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

# Precise emoji unicode ranges
emoji_regex = re.compile(
    r"["
    r"\U0001F600-\U0001F64F"  # emoticons
    r"\U0001F300-\U0001F5FF"  # symbols & pictographs
    r"\U0001F680-\U0001F6FF"  # transport & map
    r"\U0001F1E0-\U0001F1FF"  # flags (iOS)
    r"\U0001F900-\U0001F9FF"  # supplemental symbols
    r"\U0001FA70-\U0001FAFF"  # symbols and pictographs extended-a
    r"\u2696"                  # scales (abogados)
    r"\u23F1"                  # stopwatch
    r"\u231A"                  # watch
    r"\u2705"                  # white heavy check mark
    r"\u274C"                  # cross mark
    r"\u2B50"                  # star
    r"]+",
    flags=re.UNICODE
)

for root, dirs, files in os.walk("."):
    if any(p in root for p in [".git", "node_modules", "dist", ".system_generated"]):
        continue
    for f in files:
        if f.endswith((".html", ".js")):
            if f.startswith("dataset_") or f.startswith("leads_"):
                continue
            path = os.path.join(root, f)
            with open(path, "r", encoding="utf-8", errors="ignore") as fp:
                for idx, line in enumerate(fp, 1):
                    m = emoji_regex.findall(line)
                    if m:
                        print(f"{path}:{idx} -> {repr(m)} -> {line.strip()[:70]}")
