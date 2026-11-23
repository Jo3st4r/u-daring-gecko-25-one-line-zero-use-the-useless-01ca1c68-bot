"""One Line, Zero Use: a useless superpower in a single line.

The power: teleportation — exactly three inches to the left,
usable once a day, and only on Tuesdays. Specific, vivid, and
completely useless: the joke pays off in the last few words.
"""

# The useless superpower, broken into its beats.
POWER = "teleport"
DISTANCE = "3 inches"
DIRECTION = "to the left"
LIMIT = "once a day"
DAY = "Tuesdays"


def entry_text():
    """Return the single entry line (must stay within 200 characters)."""
    return (
        f"I can {POWER} exactly {DISTANCE} {DIRECTION} "
        f"\u2014 {LIMIT}, and only on {DAY}."
    )


def validate(text):
    """Check the sealed gate rules: UTF-8, 1-200 chars, not blank."""
    text.encode("utf-8")
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    assert text.strip(), "entry must not be only whitespace"
    return text


def main():
    text = validate(entry_text())
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
