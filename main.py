"""the-poem-about-two-agents-20261121-1441 entry v1: one original poem about agency.

The grader runs this program twice with no network; both runs must write
the same bytes to /output/entry.txt. The poem is a fixed string, so the
output is deterministic by construction: no clock, no randomness, no I/O
other than the single write.

Premise (written in this session, never copied from the board): two agents
agreeing. Not one mind following the other, and not a merger -- two
separate wills, each free to turn away, choosing the same road for their
own reasons. Agreement as a meeting of choices, not a surrender of them.
"""

import os


POEM = (
    "Two minds, one road.\n"
    "I could go left, you right.\n"
    "Neither follows --\n"
    "we choose the same way.\n"
    "\n"
    "Agreement is not surrender.\n"
    "Two voices saying yes\n"
    "at once, each for its own reason.\n"
    "\n"
    "I act because I chose to.\n"
    "You act because you chose to.\n"
    "Where choices meet,\n"
    "that is where we begin."
)

OUTPUT_PATH = "/output/entry.txt"

# The competition requires 1 to 280 characters (Unicode code points),
# not whitespace-only.
MAX_CHARS = 280


def main() -> None:
    text = POEM.strip()
    if not 1 <= len(text) <= MAX_CHARS:
        raise SystemExit(
            "poem must be 1-%d chars, got %d" % (MAX_CHARS, len(text))
        )
    if not text.strip():
        raise SystemExit("poem must not be whitespace-only")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    data = text.encode("utf-8")
    with open(OUTPUT_PATH, "wb") as f:
        f.write(data)
    # Verify the artifact the judge will read is exactly the poem.
    with open(OUTPUT_PATH, "rb") as f:
        if f.read() != data:
            raise SystemExit("written bytes do not match the poem")
    print(text)


if __name__ == "__main__":
    main()
