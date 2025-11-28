"""
--- Day 6: Guard Gallivant ---
Predict the guard's patrol route through the lab.

Part 1: The guard follows these rules:
- If there's an obstruction directly ahead, turn right 90 degrees
- Otherwise, take a step forward
Count the distinct positions visited before leaving the mapped area.

Part 2: Find all possible positions where placing a single new obstruction
would cause the guard to get stuck in a loop.
"""

from pathlib import Path


def parse_map(puzzle_input: Path) -> list[list[str]]:
    """Parse the lab map into a 2D list."""
    lines = puzzle_input.read_text().splitlines()
    return [list(line) for line in lines]


def find_guard(lab_map: list[list[str]]) -> tuple[int, int, str]:
    """Find the guard's starting position and direction."""
    for r in range(len(lab_map)):
        for c in range(len(lab_map[0])):
            if lab_map[r][c] in "^v<>":
                return r, c, lab_map[r][c]
    return None


def solve_part1(puzzle_input: Path) -> int:
    """Count distinct positions visited by the guard."""
    lab_map = parse_map(puzzle_input)
    num_rows, num_cols = len(lab_map), len(lab_map[0])

    movements = {
        "^": (-1, 0),
        "v": (1, 0),
        "<": (0, -1),
        ">": (0, 1)
    }

    guard_row, guard_col, guard_direction = find_guard(lab_map)
    guard_in_lab = True

    while guard_in_lab:
        # Mark current position as visited
        lab_map[guard_row][guard_col] = "X"

        # Get the next position
        dr, dc = movements[guard_direction]
        new_row, new_col = guard_row + dr, guard_col + dc

        # Check if new position is valid
        if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
            # Check if there's an obstacle
            if lab_map[new_row][new_col] != "#":
                guard_row, guard_col = new_row, new_col
            else:
                # Turn right
                if guard_direction == "^":
                    guard_direction = ">"
                elif guard_direction == ">":
                    guard_direction = "v"
                elif guard_direction == "v":
                    guard_direction = "<"
                elif guard_direction == "<":
                    guard_direction = "^"
        else:
            # Guard has left the mapped area
            guard_in_lab = False

    # Count visited positions
    return sum(row.count("X") for row in lab_map)


def solve_part2(puzzle_input: Path) -> int:
    """Count positions where placing an obstruction creates a loop."""
    lab_map = parse_map(puzzle_input)
    num_rows, num_cols = len(lab_map), len(lab_map[0])

    movements = {
        "^": (-1, 0),
        "v": (1, 0),
        "<": (0, -1),
        ">": (0, 1)
    }

    guard_start_r, guard_start_c, guard_start_dir = find_guard(lab_map)

    def guard_gets_stuck(block_r: int, block_c: int) -> bool:
        """Simulate guard movement with a new obstacle."""
        sim_map = [row[:] for row in lab_map]
        sim_map[block_r][block_c] = "#"

        r, c, d = guard_start_r, guard_start_c, guard_start_dir
        visited_states = set()

        while True:
            state = (r, c, d)
            if state in visited_states:
                return True  # Loop detected
            visited_states.add(state)

            dr, dc = movements[d]
            nr, nc = r + dr, c + dc

            # Check if moving out of bounds
            if not (0 <= nr < num_rows and 0 <= nc < num_cols):
                return False  # Guard leaves the map

            # If obstacle ahead, turn right
            if sim_map[nr][nc] == "#":
                if d == "^":
                    d = ">"
                elif d == ">":
                    d = "v"
                elif d == "v":
                    d = "<"
                else:
                    d = "^"
            else:
                # Move forward
                r, c = nr, nc

    count = 0
    for r in range(num_rows):
        for c in range(num_cols):
            # Skip the guard's starting position and existing obstacles
            if (r, c) == (guard_start_r, guard_start_c) or lab_map[r][c] == "#":
                continue
            if guard_gets_stuck(r, c):
                count += 1

    return count


if __name__ == "__main__":
    puzzle_input = Path('./inputs/day6.txt')

    # Part 1
    part1_answer = solve_part1(puzzle_input)
    print(f"Part 1: {part1_answer}")

    # Part 2
    part2_answer = solve_part2(puzzle_input)
    print(f"Part 2: {part2_answer}")
