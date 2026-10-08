# Belief Reframes (Mooncat Crystals)

Lead-magnet tool: pick a topic, pick the thought that sounds like yours, get a balanced reframe, a journal prompt and a crystal pairing (linked to a live Shopify collection). Plus "write your own" (saved only in the visitor's browser). Interactive only, no printable (Kristen's call). Bottom of the page points to Crystal Skool for more tools.

Like the Crystal Care tool, the page has no sign-up and is noindexed: people get the URL from a Flodesk opt-in form (its workflow emails the link) or from Kristen's emails. Deep link a topic with `?topic=money` (ids: money, worth, confidence, love, rest, boundaries, mistakes, change, intuition, creativity).

- `reframes.json`: the hand-edited content. See its `_about` for tone rules.
- `build.py`: run after editing reframes.json. Checks there are exactly 111 reframes and 50 prompts and no banned phrases, then writes `data.json` (what the pages load).
- `index.html`: the tool.

Look: loads the shared theme from https://dashboard.mooncatcrystals.com/mooncat-theme.css (theme key "crystalskool-theme", `?theme=` param), same as the Crystal Care tool.

Hosting: Cloudflare Pages, no build command, output `/`. No functions or env vars.

Tone: grounded, specific, never preachy or toxic-positive. Reframes never tell someone a feeling is wrong or promise an outcome. Crystals are reminders, never a fix. Every page carries the 988 note.
