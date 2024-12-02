# Standard library imports
import pathlib
import sys


def parse_data(puzzle_input):
    """Parse input."""
    return puzzle_input.splitlines()


def part1(data):
    """Solve part 1."""
    sum = 0
    for report in data:
        report = [int(x) for x in report.split()]
        if is_safe(report):
            sum += 1

    return sum

def is_safe(report) -> bool:
    if (report[0] - report[1] > 0):
        direction = -1
    elif (report[0] - report[1] < 0):
        direction = 1
    else:
        return False
    
    for i in range(len(report) - 1):
        left = report[i]
        right = report[i+1]
        allowed = [left+direction, left+2*direction, left+3*direction]
        if (right not in allowed):
            return False
        
    return True

def is_safe_with_dampener(report) -> bool:
    if is_safe(report):
        return True
    
    for j in range(len(report)):
            variant = report.copy()
            del variant[j]
            if (is_safe(variant)):
                return True
            
    return False


def part2(data):
    """Solve part 2."""
    sum = 0
    for report in data:
        report = [int(x) for x in report.split()]
        if is_safe_with_dampener(report):
            sum += 1

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