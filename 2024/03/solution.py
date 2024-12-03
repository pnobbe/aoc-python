# Standard library imports
import pathlib
import sys
import re

def parse_data(puzzle_input):
    """Parse input."""
    pattern = r'(mul|don\'t|do)\((\d+,\d+)?\)'
    commands = re.findall(pattern, puzzle_input, re.MULTILINE)
    return commands


def part1(data):
    """Solve part 1."""
    multiplications = [tuple(map(int, m[1].split(","))) for m in data if m[0] == "mul"]
    return sum(a * b for a, b in multiplications)


def part2(data):
    """Solve part 2."""
    sum = 0
    enable_instructions = True
    for i, (command, numbers) in enumerate(data):
        if command == "don't":
            enable_instructions = False
        elif command == "do":
            enable_instructions = True
        elif enable_instructions and command == "mul":
            a, b = tuple(map(int, numbers.split(",")))
            sum += a * b
    
    return sum


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
