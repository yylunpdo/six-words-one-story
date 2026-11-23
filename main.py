"""Six Words, One Story — make.fun entry.

Writes one complete six-word story to /output/entry.txt.
Pure standard library, no dependencies.
"""

import os

STORY = "She sold the piano. Silence stayed."


def main():
    assert len(STORY.split()) == 6, "story must be exactly six words"
    assert 1 <= len(STORY) <= 60, "story must be 1-60 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(STORY)
    print(STORY)


if __name__ == "__main__":
    main()
