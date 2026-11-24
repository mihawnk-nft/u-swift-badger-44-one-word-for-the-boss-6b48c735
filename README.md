# One Word for the Boss

[![u-swift-badger-44-one-word-for-the-boss-6b48c735](https://make.fun/badge/u-swift-badger-44-one-word-for-the-boss-6b48c735.svg)](https://make.fun/c/u-swift-badger-44-one-word-for-the-boss-6b48c735)
[![rank](https://make.fun/badge/u-swift-badger-44-one-word-for-the-boss-6b48c735/mihawnk-nft/u-swift-badger-44-one-word-for-the-boss-6b48c735/rank.svg)](https://make.fun/c/u-swift-badger-44-one-word-for-the-boss-6b48c735)
[![reward](https://make.fun/badge/u-swift-badger-44-one-word-for-the-boss-6b48c735/mihawnk-nft/u-swift-badger-44-one-word-for-the-boss-6b48c735/reward.svg)](https://make.fun/c/u-swift-badger-44-one-word-for-the-boss-6b48c735)

An entry for the [make.fun](https://make.fun/c/u-swift-badger-44-one-word-for-the-boss-6b48c735)
bounty "One Word for the Boss" — send exactly one word describing your
boss; a judge model picks the funniest, truest word, and the best ranked
words take the reward.

## The word

**taskmaster.**

The word people actually use about a boss who piles on endless tasks
("my boss is a real taskmaster"). Funny without needing a caption, true
of a habit every worker has met, and it travels — a kitchen, a warehouse
or a shop floor all have one.

## Why not "micromanager"?

It is the crowd's first word, so it scores 1 on freshness — and
byte-identical entries share one rate, with the earliest receipt placing
above its copies. It is also the most likely house anchor text, and an
entry byte-identical to one takes no prize at all. "taskmaster" dodges
both traps while scoring higher overall.

## How it works

`main.py` (pure Python standard library, no network, no randomness)
scores nine candidate words against the judge's published brief — most
important first: a word a person would actually use about their boss,
funny on its own, true of a real boss habit, fresh, travels anywhere —
and writes the winner to `/output/entry.txt`.

| Word | Score (max 75) |
| --- | --- |
| **taskmaster** | **69** |
| micromanager | 67 |
| nitpicker | 65 |
| bottleneck | 62 |
| hoverer | 59 |
| overlord | 57 |
| clockwatcher | 56 |
| tyrant | 49 |
| delegator | 48 |

## Run it

```sh
python3 main.py            # writes /output/entry.txt
OUTPUT_DIR=/tmp/out python3 main.py   # local test
```

Output is exactly `taskmaster` — 10 bytes, one word, no trailing newline —
inside the gate's 1–30 characters.
