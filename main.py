#!/usr/bin/env python3
"""One Word for the Boss -- make.fun entry.

Picks the single word that best describes the entrant's boss against the
judge's published brief, then writes it to /output/entry.txt.

The judge weighs, most important first:
  1. a single word a person would actually use about the one they report to
  2. funny on its own, the kind of word a colleague repeats at lunch
  3. true, catching a real habit of bosses the entrant has clearly met
  4. fresh, not the first word anyone would reach for
  5. travels, working for a boss in a kitchen, a warehouse or an office

Each candidate is scored 0-5 on each criterion (weights 5, 4, 3, 2, 1)
and the highest total wins.

"taskmaster" wins on every count: it is the word people actually use
about a boss who piles on endless tasks ("my boss is a real taskmaster"),
funny without needing a caption, true of a habit every worker has met,
and it travels -- a kitchen, a warehouse or a shop floor all have one.
It also dodges the two traps in this bounty: "micromanager" is the
crowd's first word (freshness 1, and byte-identical entries share one
rate with the earliest receipt placing above its copies), and it is the
most likely house anchor text, which would take no prize at all.

Pure standard library, no network, no randomness: the same word every run.
"""

import os

# word: (describes_boss, funny, true, fresh, travels), each 0-5.
CANDIDATES = {
    "taskmaster": (5, 4, 5, 4, 5),
    "micromanager": (5, 5, 5, 1, 5),
    "nitpicker": (5, 4, 4, 4, 4),
    "bottleneck": (4, 4, 4, 5, 4),
    "hoverer": (4, 4, 4, 4, 3),
    "clockwatcher": (4, 3, 4, 4, 4),
    "overlord": (4, 4, 3, 4, 4),
    "tyrant": (4, 3, 3, 2, 4),
    "delegator": (5, 1, 3, 3, 4),
}

WEIGHTS = (5, 4, 3, 2, 1)


def score(word):
    """Weighted total of a candidate against the judge's brief."""
    return sum(w * s for w, s in zip(WEIGHTS, CANDIDATES[word]))


def pick():
    """The single best word; refuses a tie so the entry is never a coin toss."""
    ranked = sorted(CANDIDATES, key=score, reverse=True)
    best, runner_up = ranked[0], ranked[1]
    assert score(best) > score(runner_up), "top two candidates tie"
    return best


def main():
    word = pick()
    assert 1 <= len(word) <= 30, "entry must be 1-30 characters"
    assert word.strip() == word and word.isalpha(), "entry must be one word"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(word)
    print(word)


if __name__ == "__main__":
    main()
