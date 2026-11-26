#!/usr/bin/env python3
"""Out of Tokens, Mid-Sentence.

The joke: the line IS the error. Instead of describing a token outage,
the agent's message dies mid-word -- "mid—" -- the em dash cutting the
sentence off exactly where the tokens ran out. The "ghosting" framing
makes it relatable: the AI did not abandon you, it just went broke
mid-sentence. Funny because the entry demonstrates the failure it
describes, in 51 characters, with no setup to wade through.

The program writes that single line to entry.txt in the output
directory, as UTF-8 bytes with no trailing newline, so the file holds
exactly the judged text and nothing else.
"""

import os

# The error message, exactly as judged. 51 characters, one line.
LINE = "I'm not ghosting you, I just ran out of tokens mid—"

MAX_CHARS = 140


def output_dir():
    """Return the directory the program must write into."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def write_entry(out_dir):
    """Write LINE to entry.txt as bytes, no trailing newline.

    The file is left readable by every user (mode 0644) because the
    grader collects outputs as a different user than the one running
    this program. The chmod is best effort: if it fails, the file is
    still written and the program still exits cleanly.
    """
    if not LINE.strip():
        raise ValueError("entry must not be blank")
    if len(LINE) > MAX_CHARS:
        raise ValueError("entry is over 140 characters")
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("entry must be a single line")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(LINE.encode("utf-8"))
    try:
        os.chmod(path, 0o644)
    except OSError:
        pass
    return path


def main():
    os.umask(0o022)
    write_entry(output_dir())


if __name__ == "__main__":
    main()
