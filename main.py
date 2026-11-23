"""Six Words, One Story — make.fun entry.

Writes one complete six-word story to /output/entry.txt.
Pure standard library, no dependencies.
"""

import os

STORY = "She sold the piano. Silence stayed."


def verify_output(path):
    """Read the written entry back and check it against the contract.

    The entry must be exactly STORY: six words, 1-60 characters,
    valid UTF-8, with no trailing newline. Fail loudly instead of
    silently shipping a wrong entry.
    """
    with open(path, "rb") as f:
        raw = f.read()
    text = raw.decode("utf-8")
    assert text == STORY, "written entry does not match the story"
    assert len(text.split()) == 6, "entry must be exactly six words"
    assert 1 <= len(text) <= 60, "entry must be 1-60 characters"
    assert not text.endswith("\n"), "entry must not end with a newline"
    return text


def main():
    assert len(STORY.split()) == 6, "story must be exactly six words"
    assert 1 <= len(STORY) <= 60, "story must be 1-60 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(STORY)
    verify_output("/output/entry.txt")
    print(STORY)


if __name__ == "__main__":
    main()
