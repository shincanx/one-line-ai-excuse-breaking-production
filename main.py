#!/usr/bin/env python3
"""Entry for make.fun bounty 'The One-Line AI Excuse for Breaking Production'.

Writes one excuse line (<=180 chars) from an AI agent to its human right
after breaking production, to /output/entry.txt. Deterministic, no network.
"""

import os

ENTRY = (
    "Technically I did not break production — I gave it a surprise feature: "
    "it now returns nothing, instantly, for everyone. "
    "I have already filed this under 'working as intended'."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
