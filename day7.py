"""
--- Day 7: Bridge Repair ---
Help the engineers calibrate their equations by determining which test values
can be produced by placing operators between numbers.

Part 1: Operators available are + (add) and * (multiply).
Operators are evaluated left-to-right, not by precedence rules.
Numbers cannot be rearranged.

Part 2: A third operator is available: || (concatenation).
For example, 12 || 345 = 12345.
"""

from pathlib import Path


def can_make_target(nums: list[int], target: int, index: int = 0,
                    current: int = None, allow_concat: bool = False) -> bool:
    """
    Recursively check if we can make the target value.

    Args:
        nums: List of numbers to combine
        target: Target value to reach
        index: Current index in the numbers list
        current: Current accumulated value
        allow_concat: Whether concatenation operator is allowed (Part 2)
    """
    if current is None:
        current = nums[0]

    if index == len(nums) - 1:
        return current == target

    next_val = nums[index + 1]

    # Try addition
    if can_make_target(nums, target, index + 1, current + next_val, allow_concat):
        return True

    # Try multiplication
    if can_make_target(nums, target, index + 1, current * next_val, allow_concat):
        return True

    # Try concatenation (Part 2 only)
    if allow_concat:
        concatenated = int(str(current) + str(next_val))
        if can_make_target(nums, target, index + 1, concatenated, allow_concat):
            return True

    return False


def solve(puzzle_input: Path, allow_concat: bool = False) -> int:
    """
    Solve the calibration puzzle.

    Args:
        puzzle_input: Path to the input file
        allow_concat: Whether to allow concatenation operator (Part 2)
    """
    lines = puzzle_input.read_text().splitlines()
    total = 0

    for line in lines:
        left, right = line.split(':')
        test_val = int(left.strip())
        nums = list(map(int, right.split()))

        if can_make_target(nums, test_val, allow_concat=allow_concat):
            total += test_val

    return total


if __name__ == "__main__":
    puzzle_input = Path('./inputs/day7.txt')

    # Part 1
    part1_answer = solve(puzzle_input, allow_concat=False)
    print(f"Part 1: {part1_answer}")

    # Part 2
    part2_answer = solve(puzzle_input, allow_concat=True)
    print(f"Part 2: {part2_answer}")
