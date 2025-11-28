"""
--- Day 2: Red-Nosed Reports ---
Analyze unusual data from the Red-Nosed reactor. Each report is a list of
numbers called levels that are separated by spaces.

Part 1: A report is safe if:
- The levels are either all increasing or all decreasing
- Any two adjacent levels differ by at least one and at most three

Part 2: With the Problem Dampener, a report is safe if:
- It's already safe, OR
- Removing a single level from an unsafe report would make it safe
"""

from pathlib import Path


def is_safe_report(report: list[int]) -> bool:
    """Check if a report is safe according to the rules."""
    increasing = all(1 <= report[i+1] - report[i] <= 3 for i in range(len(report) - 1))
    decreasing = all(1 <= report[i] - report[i+1] <= 3 for i in range(len(report) - 1))
    return increasing or decreasing


def is_safe_with_dampener(report: list[int]) -> bool:
    """Check if a report is safe with the Problem Dampener."""
    if is_safe_report(report):
        return True
    for i in range(len(report)):
        modified_report = report[:i] + report[i+1:]
        if is_safe_report(modified_report):
            return True
    return False


def count_safe_reports(puzzle_input: Path) -> int:
    """Count safe reports without the dampener."""
    safe_count = 0
    with puzzle_input.open() as file:
        for line in file:
            report = list(map(int, line.split()))
            if is_safe_report(report):
                safe_count += 1
    return safe_count


def count_safe_reports_with_dampener(puzzle_input: Path) -> int:
    """Count safe reports with the Problem Dampener."""
    safe_count = 0
    with puzzle_input.open() as file:
        for line in file:
            report = list(map(int, line.split()))
            if is_safe_with_dampener(report):
                safe_count += 1
    return safe_count


if __name__ == "__main__":
    puzzle_input = Path('./inputs/day2.txt')

    # Part 1
    part1_answer = count_safe_reports(puzzle_input)
    print(f"Part 1: {part1_answer}")

    # Part 2
    part2_answer = count_safe_reports_with_dampener(puzzle_input)
    print(f"Part 2: {part2_answer}")
