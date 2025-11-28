"""
--- Day 4: Ceres Search ---
Help the Elf with her word search puzzle.

Part 1: Find all occurrences of "XMAS" in a word search grid.
Words can be horizontal, vertical, diagonal, written backwards, or overlapping.

Part 2: Find all X-MAS patterns - two "MAS" in the shape of an X.
Each MAS can be written forwards or backwards.
"""

from pathlib import Path


def read_grid(puzzle_input: Path) -> list[str]:
    """Read the puzzle input into a grid."""
    with puzzle_input.open() as file:
        grid = [line.strip() for line in file]
    return grid


def count_word_occurrences(grid: list[str], word: str) -> int:
    """Count all occurrences of a word in the grid (all directions)."""
    rows = len(grid)
    cols = len(grid[0])
    word_len = len(word)
    count = 0

    # Check horizontal (left to right and right to left)
    for r in range(rows):
        for c in range(cols - word_len + 1):
            if grid[r][c:c + word_len] == word:
                count += 1
            if grid[r][c:c + word_len][::-1] == word:
                count += 1

    # Check vertical (top to bottom and bottom to top)
    for c in range(cols):
        for r in range(rows - word_len + 1):
            if ''.join(grid[r + i][c] for i in range(word_len)) == word:
                count += 1
            if ''.join(grid[r + i][c] for i in range(word_len))[::-1] == word:
                count += 1

    # Check diagonal (top-left to bottom-right and bottom-right to top-left)
    for r in range(rows - word_len + 1):
        for c in range(cols - word_len + 1):
            if ''.join(grid[r + i][c + i] for i in range(word_len)) == word:
                count += 1
            if ''.join(grid[r + i][c + i] for i in range(word_len))[::-1] == word:
                count += 1

    # Check diagonal (top-right to bottom-left and bottom-left to top-right)
    for r in range(rows - word_len + 1):
        for c in range(word_len - 1, cols):
            if ''.join(grid[r + i][c - i] for i in range(word_len)) == word:
                count += 1
            if ''.join(grid[r + i][c - i] for i in range(word_len))[::-1] == word:
                count += 1

    return count


def count_x_mas(grid: list[str]) -> int:
    """Count all X-MAS patterns (two MAS in the shape of an X)."""
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    for r in range(rows - 2):
        for c in range(cols - 2):
            main_diagonal = grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2]
            anti_diagonal = grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c]
            if main_diagonal in ("MAS", "SAM") and anti_diagonal in ("MAS", "SAM"):
                count += 1

    return count


if __name__ == "__main__":
    puzzle_input = Path('./inputs/day4.txt')
    grid = read_grid(puzzle_input)

    # Part 1
    word = "XMAS"
    part1_answer = count_word_occurrences(grid, word)
    print(f"Part 1: {part1_answer}")

    # Part 2
    part2_answer = count_x_mas(grid)
    print(f"Part 2: {part2_answer}")
