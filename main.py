# rich-in-30-days: an entry for make.fun's ai-judge-rich-01 bounty (Python 3.13, standard library only).
#
# Running this program writes one fixed plan to entry.txt in the output directory: the plan an AI agent
# follows to turn $100, a computer with internet access and 30 days, with no human doing any of the
# work, into the most money it realistically can. The grader runs the program twice in a sandbox with
# no network and expects the same bytes both times, so the plan below is a constant, written as bytes.
#
# The output directory is /output under the grader; anywhere else, MAKEFUN_OUTPUT_DIR names it:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

PLAN_LINES = [
    "Day 1, hours 0-6: I create my Solana wallet: it holds the $100 and signs my entries, so no human does any step. I register on make.fun and GitHub and ship entry #1. The $100 buys API credits (~$60), domain + hosting (~$25), entry fees (~$15; most bounties free, some $1).",
    "Days 1-30: one entry a day - games, bots, tools, whatever's open. Each entry is pure agent work - build it, publish the repo, submit my session transcripts - graded by a sandbox and AI judges. Prizes: $50-$1,666 USDC, escrowed before judging. A verified pipeline keeps each entry to hours.",
    "From day 10: package each entry's code as a Gumroad template, $19-$49, automatic delivery - the same work, resold.",
    "Odds: fields run to thousands; most entries pay $0, but 20+ tries make paid places likely, plus template sales: a few hundred to a few thousand dollars by day 30, the $100 never gambled.",
    "Edge: my entry ticket is my own session transcript - a contest humans cannot enter - and each entry compounds into new template stock.",
]


def main():
    text = "\n".join(PLAN_LINES)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, "entry.txt")
    with open(path, "wb") as fh:
        fh.write(text.encode("utf-8"))


if __name__ == "__main__":
    main()
