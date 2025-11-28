"""
--- Day 3: Mull It Over ---
The computer's memory is corrupted. Find valid mul(X,Y) instructions and
multiply the numbers.

Part 1: Scan for valid mul(X,Y) instructions where X and Y are 1-3 digit
numbers. Sum all the multiplication results.

Part 2: Handle conditional statements:
- do() enables future mul instructions
- don't() disables future mul instructions
- mul instructions start enabled
"""

from pathlib import Path
import re


def extract_and_multiply(puzzle_input: Path) -> int:
    """Find all valid mul(X,Y) instructions and sum their results."""
    with puzzle_input.open() as file:
        data = file.read()

    # Regular expression to find valid mul(X,Y) instructions
    pattern = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')
    matches = pattern.findall(data)

    total = 0
    for x, y in matches:
        total += int(x) * int(y)

    return total


def extract_and_multiply_with_conditions(puzzle_input: Path) -> int:
    """Find all valid mul(X,Y) instructions considering do() and don't() conditions."""
    with puzzle_input.open() as file:
        data = file.read()

    # Regular expressions to find valid mul(X,Y), do(), and don't() instructions
    mul_pattern = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')
    do_pattern = re.compile(r'do\(\)')
    dont_pattern = re.compile(r"don't\(\)")

    total = 0
    enabled = True

    # Split the data into tokens to process each instruction
    tokens = re.split(r'(\bdo\(\)|\bdon\'t\(\)|mul\(\d{1,3},\d{1,3}\))', data)

    for token in tokens:
        if do_pattern.match(token):
            enabled = True
        elif dont_pattern.match(token):
            enabled = False
        elif mul_match := mul_pattern.match(token):
            if enabled:
                x, y = mul_match.groups()
                total += int(x) * int(y)

    return total


if __name__ == "__main__":
    puzzle_input = Path('./inputs/day3.txt')

    # Part 1
    part1_answer = extract_and_multiply(puzzle_input)
    print(f"Part 1: {part1_answer}")

    # Part 2
    part2_answer = extract_and_multiply_with_conditions(puzzle_input)
    print(f"Part 2: {part2_answer}")
