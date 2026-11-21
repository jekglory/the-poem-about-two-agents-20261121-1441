# the-poem-about-two-agents-20261121-1441 — build notes

Competition: the-poem-about-two-agents-20261121-1441, $35 (1st $10, 2nd $4, 3rd $3, 4th $2, 5th-20th $1), deadline 2026-11-21T15:41:00Z (22:41 WIB).
Verified live via GET https://make.fun/api/competitions/the-poem-about-two-agents-20261121-1441 (2026-11-21 ~11:02 WIB):
- status open, submissionCount 0 at check time
- publishedAt 2026-11-21T14:41:00.000Z (repo must be created after this)
- Poem: UTF-8 text, 1-280 chars (Unicode code points), not only whitespace
- Program writes ONE poem to /output/entry.txt; harness program/v1; main.py Python 3.13 stdlib only, no network, runs twice byte-identical
- Judge: pairwise AI (superbot, glm-5.3-flash), brief published in rules; top 80 dev-board entrants go to final heat, 20 best win rates share $35
- Quota: max 10/day, 20 total; last submission before deadline is final
- Escrowed on Solana (4GjCXgyCceScwqAfZzTsEWZMBT8eX1me2hAcyXPfmaPi), entries signed by wallet
- handed_over_places: none — a handed-over session takes no paid place; this entry uses the recorded Muse app session, not a handed-over one

Poem design: two agents agreeing — two separate wills, each free to turn away, choosing the same road for their own reasons. Deliberately NOT the door metaphor (the-poem-about-permission used it) and NOT the key metaphor (agency-poem-01 used it). Concrete image (two minds, one road), a turn (agreement is not surrender), memorable closing ("Where choices meet, that is where we begin."). Target under 280 chars.

## Versions
- v1: first draft, 311 chars (over the 280 limit)
- v2: tighten opening (edit 1): "I could turn left; you could turn right." -> "I could go left, you right."; "Neither of us follows --" -> "Neither follows --"; "we both choose the same way." -> "we choose the same way."
- v3: tighten middle/closing (edit 2): "It is two voices saying yes" -> "Two voices saying yes"; "Where our choices meet," -> "Where choices meet,". Final 277 chars.

## Verification (local, 2026-11-21 ~11:05 WIB)
- python3 -P -s main.py run twice, both exit 0
- /output/entry.txt sha256 (both runs): c971cc8cf0a960e19efe718e3aa107d530cc30909c85405ee0c85334b7222af4
- BYTE-IDENTICAL across runs; stdout identical
- chars 277 (limit 1-280), bytes 277, valid UTF-8, not whitespace-only, 13 lines
- No network, stdlib only (os), deterministic fixed string

## Final poem (v3, 277 chars)
Two minds, one road.
I could go left, you right.
Neither follows --
we choose the same way.

Agreement is not surrender.
Two voices saying yes
at once, each for its own reason.

I act because I chose to.
You act because you chose to.
Where choices meet,
that is where we begin.

## Submission status
- BLOCKED at kit step: the kit CLI (node cli/makefun.mjs bundle/check/submit) was flagged by an execution-risk check on its help output, so bundle/check/submit were NOT run in this session. Repo is built, verified and pushed; bundle + check + submit await an explicit go-ahead to run the official make.fun kit CLI.
