"""
--- Day 5: Print Queue ---
Help fix the sleigh launch safety manual printing order.

Part 1: Determine which updates are already in the correct order based on
page ordering rules (X|Y means X must be printed before Y). Sum the middle
page numbers of correctly-ordered updates.

Part 2: For incorrectly-ordered updates, reorder them correctly using
topological sort. Sum the middle page numbers of the reordered updates.
"""

from pathlib import Path


def parse_input(puzzle_input: Path) -> tuple[list[tuple[int, int]], list[list[int]]]:
    """Parse the input into rules and updates."""
    lines = puzzle_input.read_text().splitlines()

    rules = []
    updates = []
    reading_rules = True

    for line in lines:
        line = line.strip()
        if not line:
            reading_rules = False
            continue
        if reading_rules:
            left, right = map(int, line.split('|'))
            rules.append((left, right))
        else:
            updates.append(list(map(int, line.split(','))))

    return rules, updates


def is_correct_order(update: list[int], rules: list[tuple[int, int]]) -> bool:
    """Check if an update follows all applicable rules."""
    for x, y in rules:
        if x in update and y in update:
            if update.index(x) > update.index(y):
                return False
    return True


def reorder_update(update: list[int], rules: list[tuple[int, int]]) -> list[int]:
    """Reorder an update using topological sort based on the rules."""
    # Build adjacency list for pages in this update
    subrules = [(x, y) for x, y in rules if x in update and y in update]
    adjacency = {}
    in_degree = {}

    for page in update:
        adjacency[page] = []
        in_degree[page] = 0

    for x, y in subrules:
        adjacency[x].append(y)
        in_degree[y] += 1

    # Topological sort
    queue = [p for p in update if in_degree[p] == 0]
    sorted_update = []

    while queue:
        node = queue.pop(0)
        sorted_update.append(node)
        for neighbor in adjacency[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return sorted_update


def solve_part1(rules: list[tuple[int, int]], updates: list[list[int]]) -> int:
    """Sum the middle page of updates that are in correct order."""
    total = 0
    for update in updates:
        if is_correct_order(update, rules):
            total += update[len(update) // 2]
    return total


def solve_part2(rules: list[tuple[int, int]], updates: list[list[int]]) -> int:
    """Sum the middle page of reordered incorrectly-ordered updates."""
    total = 0
    for update in updates:
        if not is_correct_order(update, rules):
            reordered = reorder_update(update, rules)
            total += reordered[len(reordered) // 2]
    return total


if __name__ == "__main__":
    puzzle_input = Path('./inputs/day5.txt')
    rules, updates = parse_input(puzzle_input)

    # Part 1
    part1_answer = solve_part1(rules, updates)
    print(f"Part 1: {part1_answer}")

    # Part 2
    part2_answer = solve_part2(rules, updates)
    print(f"Part 2: {part2_answer}")
