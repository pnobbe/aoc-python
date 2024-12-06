# Standard library imports
import pathlib
import sys


def parse_data(puzzle_input):
    """Parse input."""
    return puzzle_input.splitlines()


def part1(data):
    """Solve part 1."""
    count = 0
    width = len(data[0])
    length = len(data)
    # find all occurrences of 'X' in the matrix
    for i in range(length):
        for j in range(width):
            if data[i][j] == "X":
                count += xmas_occurrences(data, (i, j))

    return count


def xmas_occurrences(matrix, start_coord):
    """Verify if 'XMAS' is written in any direction from the X at the start_coord"""
    width = len(matrix[0])
    length = len(matrix)
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    total = 0
    for direction in directions:
        x, y = start_coord
        for letter in "XMAS":
            if x < 0 or y < 0 or x >= length or y >= width or matrix[x][y] != letter:
                break
            x += direction[0]
            y += direction[1]
        else:
            total += 1

    return total


def part2(data):
    """Solve part 2."""
    count = 0
    width = len(data[0])
    length = len(data)
    # find all occurrences of 'A' in the matrix
    for i in range(length):
        for j in range(width):
            if data[i][j] == "A":
                if x_mas_occurs(data, (i, j)):
                    count += 1

    return count


def x_mas_occurs(matrix, start_coord):
    """Verify if 'MAS' appears twice, crossing each other in any direction from the A at the start_coord"""
    width = len(matrix[0])
    length = len(matrix)

    x = start_coord[0]
    y = start_coord[1]

    if x < 1 or y < 1 or x >= length - 1 or y >= width - 1:
        return False

    letters = [
        matrix[x - 1][y - 1],  # top left
        matrix[x + 1][y + 1],  # bottom right
        matrix[x - 1][y + 1],  # top right
        matrix[x + 1][y - 1],  # bottom left
    ]

    if letters.count("M") == 2 and letters.count("S") == 2 and letters[0] != letters[1]:
        return True

    return False


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
