# Standard library imports
import pathlib
import sys


def parse_data(puzzle_input):
    """Parse input."""
    lines = puzzle_input.splitlines()
    data = []
    for line in lines:
        input = line.split(":")
        test_number = int(input[0])
        operators = list(map(int, input[1].split()))
        data.append((test_number, operators))

    return data


def part1(data):
    """Solve part 1."""
    total_calibration_result = 0
    for line in data:
        test_number, operators = line
        if compute(test_number, operators):
            total_calibration_result += test_number

    return total_calibration_result


def compute(test_number, operators):
    # generate all permutations of the operators, either multiply or add
    for i in range(2 ** len(operators)):
        result = operators[0]
        for j in range(1, len(operators)):
            if (i >> j) % 2 == 0:
                result += operators[j]
            else:
                result *= operators[j]

        if result == test_number:
            return True

    return False


def compute2(test_number, operators):
    # generate all permutations of the operators, either multiply, add or combine
    for i in range(3 ** len(operators)):
        result = operators[0]
        temp = i
        for j in range(1, len(operators)):
            operation = temp % 3
            temp //= 3
            if operation == 0:
                # add
                result += operators[j]
            elif operation == 1:
                # multiply
                result *= operators[j]
            else:
                # combine
                result = int(f"{result}{operators[j]}")

        if result == test_number:
            return True

    return False


def part2(data):
    """Solve part 2."""
    total_calibration_result = 0
    for line in data:
        test_number, operators = line
        if compute2(test_number, operators):
            total_calibration_result += test_number

    return total_calibration_result


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
