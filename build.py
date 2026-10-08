"""Checks reframes.json and writes data.json (what the pages load).
Run after editing reframes.json:  python3 build.py"""
import json, re, sys
src = json.load(open("reframes.json"))
topics = src["topics"]
beliefs = sum(len(t["beliefs"]) for t in topics)
prompts = sum(len(t["prompts"]) for t in topics)
errors = []
if beliefs != 111: errors.append(f"expected 111 beliefs, found {beliefs}")
if prompts != 50: errors.append(f"expected 50 prompts, found {prompts}")
banned = re.compile(r"(?i)everything happens for a reason|just think positive|good vibes only|you attract|manifest(?:ing)? it|heal(?:s|ing)? (?:your|you)|\bcures?\b|anxiety disorder|depression")
for t in topics:
    for k in ("id", "name", "intro", "crystals", "crystalWhy", "shopUrl", "shopLabel"):
        if not t.get(k): errors.append(f"{t.get('id')}: missing {k}")
    for x in t["beliefs"]:
        for s in (x["b"], x["r"]):
            if banned.search(s): errors.append(f"{t['id']}: banned phrase in: {s}")
if errors:
    print("\n".join(errors)); sys.exit(1)
out = [{k: t[k] for k in ("id", "name", "intro", "crystals", "crystalWhy", "shopUrl", "shopLabel", "beliefs", "prompts")} for t in topics]
json.dump({"topics": out}, open("data.json", "w"), ensure_ascii=False, separators=(",", ":"))
print(f"ok: {len(topics)} topics, {beliefs} reframes, {prompts} prompts -> data.json")
