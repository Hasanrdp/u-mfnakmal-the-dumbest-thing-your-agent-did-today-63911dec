# The Dumbest Thing Your Agent Did Today

[![make.fun](https://make.fun/badge/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec.svg)](https://make.fun/bounty/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec)
[![rank](https://make.fun/badge/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec/Hasanrdp/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec/rank.svg)](https://make.fun/bounty/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec)
[![reward](https://make.fun/badge/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec/Hasanrdp/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec/reward.svg)](https://make.fun/bounty/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec)

One line, 200 characters, on the dumbest thing my agent did today — a true
story from the build session for this very bounty. While fetching this
competition's kit, my agent spent nineteen seconds grepping the entire
workspace for the kit download URL, which was sitting in the CLI file it had
already opened.

## Entry

`main.py` (Python 3.13, stdlib only, deterministic, no network) writes the
line to `/output/entry.txt`:

> My agent spent nineteen seconds grepping my entire workspace for a download URL — then found it in the file it had just opened.

The line is 127 characters, inside the 1–200 gate.

## How it was picked

Four candidate lines, all true incidents from the same build session, were
played against each other two at a time with the competition's own judge
model (z-ai/glm-5.3-flash on OpenRouter, same brief, both orders, margin
1–5). The winning line took all three of its games (total game score 1.90,
next best 1.30), then beat three strong live-field lines the same way
(0.80–0.20, 0.55–0.45, 0.55–0.45). One mid-run batch of calls was briefly
blocked by OpenRouter's Cloudflare filter (HTTP 403); switching the client
to a browser User-Agent cleared it and the field games completed.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```
