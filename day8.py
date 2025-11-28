"""
--- Day 8: Resonant Collinearity ---
You find yourselves on the roof of a top-secret Easter Bunny installation.

The antennas emit signals that create antinodes at specific locations. An antinode
occurs at any point that is perfectly in line with two antennas of the same frequency,
but only when one of the antennas is twice as far away as the other.

Part 1: For each pair of antennas with the same frequency, there are two antinodes,
one on either side of them. Count the unique locations within the bounds of the map
that contain an antinode.

Part 2: (To be revealed after Part 1 is solved)
"""

from pathlib import Path
from collections import defaultdict
from itertools import combinations


def parse_map(puzzle_input: Path) -> tuple[list[str], int, int]:
    """Parse the antenna map and return grid with dimensions."""
    with puzzle_input.open() as file:
        grid = [line.strip() for line in file]
    return grid, len(grid), len(grid[0])


def find_antennas(grid: list[str]) -> dict[str, list[tuple[int, int]]]:
    """Find all antennas grouped by frequency."""
    antennas = defaultdict(list)

    for r, row in enumerate(grid):
        for c, char in enumerate(row):
            if char != '.':
                antennas[char].append((r, c))

    return antennas


def find_antinodes(antennas: dict[str, list[tuple[int, int]]],
                   rows: int, cols: int) -> set[tuple[int, int]]:
    """Find all antinode locations within the map bounds."""
    antinodes = set()

    # For each frequency
    for frequency, positions in antennas.items():
        # Check all pairs of antennas with the same frequency
        for (r1, c1), (r2, c2) in combinations(positions, 2):
            # Calculate the vector from first antenna to second
            dr = r2 - r1
            dc = c2 - c1

            # Antinode 1: extends the line beyond the first antenna
            # (first antenna is twice as far from this antinode as second antenna)
            antinode1 = (r1 - dr, c1 - dc)

            # Antinode 2: extends the line beyond the second antenna
            # (second antenna is twice as far from this antinode as first antenna)
            antinode2 = (r2 + dr, c2 + dc)

            # Check if antinodes are within bounds
            if 0 <= antinode1[0] < rows and 0 <= antinode1[1] < cols:
                antinodes.add(antinode1)

            if 0 <= antinode2[0] < rows and 0 <= antinode2[1] < cols:
                antinodes.add(antinode2)

    return antinodes


def solve_part1(puzzle_input: Path) -> int:
    """Count unique antinode locations within the map bounds."""
    grid, rows, cols = parse_map(puzzle_input)
    antennas = find_antennas(grid)
    antinodes = find_antinodes(antennas, rows, cols)
    return len(antinodes)


if __name__ == "__main__":
    puzzle_input = Path('./inputs/day8.txt')

    # Part 1
    part1_answer = solve_part1(puzzle_input)
    print(f"Part 1: {part1_answer}")
