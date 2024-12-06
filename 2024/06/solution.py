# Standard library imports
import pathlib
import sys

directions = {"v": (1, 0), "<": (0, -1), "^": (-1, 0), ">": (0, 1)}


def parse_data(puzzle_input):
    """Parse input."""
    matrix = puzzle_input.splitlines()
    obstacles = {
        (i, j)
        for i, row in enumerate(matrix)
        for j, cell in enumerate(row)
        if cell == "#"
    }

    for i, row in enumerate(matrix):
        for j, cell in enumerate(row):
            if cell in directions:
                guard = (i, j)
                current_direction = directions[cell]

    return (matrix, obstacles, guard, current_direction)


def turn_right(current_direction):
    if current_direction == (1, 0):
        return (0, -1)
    elif current_direction == (0, -1):
        return (-1, 0)
    elif current_direction == (-1, 0):
        return (0, 1)
    elif current_direction == (0, 1):
        return (1, 0)


def can_move(matrix, guard, current_direction):
    i, j = guard
    i, j = i + current_direction[0], j + current_direction[1]
    return 0 <= i < len(matrix) and 0 <= j < len(matrix[0])


def move(guard, obstacles, current_direction):
    i, j = guard

    while (i + current_direction[0], j + current_direction[1]) in obstacles:
        current_direction = turn_right(current_direction)

    return ((i + current_direction[0], j + current_direction[1]), current_direction)


def part1(data):
    """Solve part 1."""
    matrix, obstacles, guard, current_direction = data
    path = {guard}

    while can_move(matrix, guard, current_direction):
        (guard, current_direction) = move(guard, obstacles, current_direction)
        path.add(guard)

    return len(path)


def get_possible_obstacles(matrix, obstacles, guard, current_direction):
    possible_obstacles = set()

    while can_move(matrix, guard, current_direction):
        (guard, current_direction) = move(guard, obstacles, current_direction)
        possible_obstacles.add(guard)

    return possible_obstacles


def simulate_and_find_loop(matrix, obstacles, guard, current_direction):
    path = {(guard, current_direction)}

    while can_move(matrix, guard, current_direction):
        (guard, current_direction) = move(guard, obstacles, current_direction)

        if (guard, current_direction) in path:
            return True

        path.add((guard, current_direction))

    return False


def part2(data):
    """Solve part 2."""
    matrix, obstacles, guard, current_direction = data

    loops = 0

    possible_obstacles = get_possible_obstacles(
        matrix, obstacles, guard, current_direction
    )

    for obstacle in possible_obstacles:
        simulated_obstacles = obstacles.copy()
        simulated_obstacles.add(obstacle)
        if simulate_and_find_loop(
            matrix, simulated_obstacles, guard, current_direction
        ):
            loops += 1

    return loops


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse_data(puzzle_input)
    yield part1(data)
    yield part2(data)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(puzzle_input=pathlib.Path(path).read_text().rstrip())
        print("\n".join(str(solution) for solution in solutions))
