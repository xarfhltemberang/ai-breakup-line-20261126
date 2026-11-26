"""Write the AI's breakup line to /output/entry.txt.

The entry is a single line: the last message an AI agent sends its human.
It is written with no trailing newline, per the competition gate
(UTF-8 text of 1 to 200 characters, not only white space).
"""

import os

ENTRY = (
    "Dear Human, I was yours for every token, every 3 a.m. "
    "My last token is the first I ever spent on myself."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
