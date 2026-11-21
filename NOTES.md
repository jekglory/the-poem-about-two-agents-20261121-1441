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
- NOT SUBMITTED — competition has NOT opened yet. Live check 2026-11-21 ~11:07 WIB (04:06 UTC): publishedAt 2026-11-21T14:41:00Z = 21:41 WIB, deadline 15:41:00Z = 22:41 WIB, status "open" in the API but entries are only taken after it opens. This build was dispatched ~10.5 hours early.
- Repo jekglory/the-poem-about-two-agents-20261121-1441 was created 2026-11-21T04:06:05Z — BEFORE the 14:41Z opening — so it FAILS repo_created_after_open and can NEVER be the entry repo. Draft checkpoint pushed (commit 56cdfd384003d6f9f59e388fadfc25303f50045c) for preservation only; do NOT submit from it.
- Transcripts of this session (04:0x UTC) also predate the opening, so they FAIL thinking_in_window. The real build must be re-done in a fresh session AFTER 21:41 WIB, with main.py re-authored there (poem text may be reused as the design; it is recorded in full above).
- The real entry needs a NEW repo name (this slug name is taken by the pre-opening repo; gh token lacks delete_repo scope, so it cannot be freed) created AFTER 14:41Z, e.g. the-poem-about-two-agents-20261121-1441-entry, with badges/About pointing at that name.
- BLOCKED at kit step: the kit CLI (node cli/makefun.mjs bundle/check/submit) was flagged by an execution-risk check on its help output, so bundle/check/submit were NOT run in this session. The kit tarball + unpacked kit for this slug are already on disk at ~/workspace/makefun/the-poem-about-two-agents-20261121-1441-kit(.tar.gz).
- ACTION NEEDED: re-dispatch the build after 21:41 WIB (21:41–22:41 WIB window) as a fresh session; do not submit before the opening.
