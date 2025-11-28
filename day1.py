"""
--- Day 1: Historian Hysteria ---
The Chief Historian is always present for the big Christmas sleigh launch,
but nobody has seen him in months! Last anyone heard, he was visiting
locations that are historically significant to the North Pole; a group of
Senior Historians has asked you to accompany them as they check the places
they think he was most likely to visit.

As each location is checked, they will mark it on their list with a star.
They figure the Chief Historian must be in one of the first fifty places
they'll look, so in order to save Christmas, you need to help them get
fifty stars on their list before Santa takes off on December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on
each day in the Advent calendar; the second puzzle is unlocked when you
complete the first. Each puzzle grants one star. Good luck!

Part 1: Calculate total distance between left and right lists by pairing
smallest with smallest, second-smallest with second-smallest, etc.

Part 2: Calculate similarity score by multiplying each number in left list
by the number of times it appears in right list.
"""

from pathlib import Path
from collections import Counter


def read_input(puzzle_input: Path) -> tuple[list[int], list[int]]:
    """Read the puzzle input and return two sorted lists."""
    x = []
    y = []
    with puzzle_input.open() as file:
        for line in file:
            a, b = line.split()
            x.append(int(a))
            y.append(int(b))
    x.sort()
    y.sort()
    return x, y


def distance_between_lists(x: list[int], y: list[int]) -> int:
    """Calculate the difference between each element in the lists x and y."""
    total = 0
    for i in range(len(x)):
        total += abs(x[i] - y[i])
    return total


def similarity_score(x: list[int], y: list[int]) -> int:
    """Calculate similarity score based on frequency of left list numbers in right list."""
    y_counts = Counter(y)
    score = 0
    for num in x:
        score += num * y_counts[num]
    return score


if __name__ == "__main__":
    puzzle_input = Path('./inputs/day1.txt')

    # Part 1
    x, y = read_input(puzzle_input)
    part1_answer = distance_between_lists(x, y)
    print(f"Part 1: {part1_answer}")

    # Part 2
    x, y = read_input(puzzle_input)
    part2_answer = similarity_score(x, y)
    print(f"Part 2: {part2_answer}")
