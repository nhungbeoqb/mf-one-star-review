#!/usr/bin/env python3
"""One-Star Review of Something Essential.

Writes one single-line deadpan one-star review, at most 160 characters,
of an everyday essential everyone relies on, to /output/entry.txt.
Python 3.13 standard library only.

Candidates considered (9, genuinely different):
  A. Toilet paper — the perforation tears cleanly everywhere except the
     one square in your hand. -- CHOSEN: undeniably essential, universal,
     and the grievance (the perforation failing exactly where it matters)
     is a small daily annoyance everyone recognises but has never seen
     written down as a review. Deadpan throughout, one joke, the sting
     lands in the last few words on a concrete image: the square in hand.
  B. Knees — silent for thirty years, now they narrate every staircase.
     Funny, but a body part is a weaker "everyday essential" than the
     brief's sun/gravity/sleep/water/oxygen/Mondays class.
  C. Shoelaces — hold all day, then come undone the moment both hands
     are full. Sharp grievance, but not everyone wears lace-up shoes.
  D. Batteries — reads full all week, then dies mid-way through the one
     thing you needed it for. Good turn, but "the one thing" is generic.
  E. Snooze button — lends nine minutes, collects the whole morning.
     Elegant ledger image, but a snooze button is not an essential.
  F. Gravity — holds the moon in orbit, cannot hold my phone on the
     arm of the sofa. Strong contrast, but gravity is a listed example
     and the field of 2820 will be flooded with it.
  G. Rain — holds off all morning, starts the moment I leave without
     an umbrella. Concrete scene, but "holds off" winks at intent.
  H. Electricity — powers the whole house, cannot reach the one socket
     behind the bed. Good, but the socket problem is niche, not universal.
  I. Sleep — eight hours a night, every night, and I still wake up
     tired. Tight and true, but sleep is a listed example, flooded.

v1: "One star. It tears along the perforation everywhere except the
square I am holding."
v2 (genuine second-round revision): "tears" -> "tears cleanly" (the
tear is clean everywhere else, ragged where it counts) and "the square
I am holding" -> "the one square in my hand" (more embodied, tighter).
"""

import os

# The review, assembled from named parts so each clause reads on its own.
RATING = "One star. "
COMPLAINT = "It tears cleanly along the perforation everywhere except "
PUNCH = "the one square in my hand."

ENTRY = RATING + COMPLAINT + PUNCH


def write_entry(text: str) -> None:
    """Write the review to the gate file, exactly one line + newline."""
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


def main() -> None:
    write_entry(ENTRY)


if __name__ == "__main__":
    main()
