# Standard library imports
import pathlib
import sys


def parse_data(puzzle_input):
    """Parse input."""
    return puzzle_input.splitlines()


def find_next_inclines_1(matrix, coordinates, next_incline):
    next_inclines = set()
    for coordinate in coordinates:
        x, y = coordinate
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0 or nx >= len(matrix[0]) or ny >= len(matrix):
                continue
            if matrix[ny][nx] == next_incline:
                next_inclines.add((nx, ny))

    return next_inclines


def score_trialhead_1(matrix, trialhead):
    inclines = {trialhead}
    next = 1
    while inclines:
        inclines = find_next_inclines_1(matrix, inclines, str(next))

        if next == 9:
            return len(inclines)

        next += 1


def part1(matrix):
    """Solve part 1."""
    # find all trialheads, aka coordinates where the cell == '0'
    trialheads = [
        (x, y)
        for y, row in enumerate(matrix)
        for x, cell in enumerate(row)
        if cell == "0"
    ]

    # starting at the trialheads, find the next inclines until we're at the summit (9)
    sum_score = 0
    for trialhead in trialheads:
        score = score_trialhead_1(matrix, trialhead)
        sum_score += score

    return sum_score


def find_next_inclines_2(matrix, coordinates, next_incline):
    next_inclines = []
    for coordinate in coordinates:
        x, y = coordinate
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0 or nx >= len(matrix[0]) or ny >= len(matrix):
                continue
            if matrix[ny][nx] == next_incline:
                next_inclines.append((nx, ny))

    return next_inclines


def score_trialhead_2(matrix, trialhead):
    inclines = [trialhead]
    next = 1
    while inclines:
        inclines = find_next_inclines_2(matrix, inclines, str(next))

        if next == 9:
            return len(inclines)

        next += 1


def part2(matrix):
    """Solve part 2."""
    # find all trialheads, aka coordinates where the cell == '0'
    trialheads = [
        (x, y)
        for y, row in enumerate(matrix)
        for x, cell in enumerate(row)
        if cell == "0"
    ]

    # starting at the trialheads, find the next inclines until we're at the summit (9)
    sum_score = 0
    for trialhead in trialheads:
        score = score_trialhead_2(matrix, trialhead)
        sum_score += score

    return sum_score

def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    matrix = parse_data(puzzle_input)
    yield part1(matrix)
    yield part2(matrix)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(puzzle_input=pathlib.Path(path).read_text().rstrip())
        print("\n".join(str(solution) for solution in solutions))
