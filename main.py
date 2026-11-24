"""Entry for make.fun 'Angry Judge: The Short Rant Contest'
(u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046).

Writes the winning short rant to /output/entry.txt (UTF-8, 345 characters,
inside the contest's 400-character cap).
The rant targets a small everyday annoyance — the colleague who microwaves
fish in the shared office kitchen — framed as a whodunit, because the
suspect list, the group chat and the culprit hiding inside both are what
make the anger feel shared rather than performed.
Deterministic: same bytes on every run.
"""

from pathlib import Path

ENTRY = "Someone in my office microwaves fish. FISH. In a shared box that heats everyone's food, in a building with no windows that open, at 11:40 in the morning like a declaration of war. We have a suspect list. We have a group chat about it. The fish person is in the group chat, adding theories. It is a whodunit where the weapon reeks until Thursday."


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
