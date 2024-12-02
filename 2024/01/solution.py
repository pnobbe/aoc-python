# Standard library imports
import pathlib
import sys


def parse_data(puzzle_input):
    """Parse input."""
    column1 = list()
    column2 = list()

    lines = puzzle_input.splitlines()

    for line in lines:
        column1.append(int(line.split()[0]))
        column2.append(int(line.split()[1]))
    return (column1, column2)


def part1(data):
    column1, column2 = data
    column1.sort()
    column2.sort()
    
    sum = 0
    for i in range(len(column1)):
        sum += abs(column1[i] - column2[i])

    return sum



def part2(data):
    """Solve part 2."""
    column1, column2 = data

    sum = 0
    for i in column1:
        count = column2.count(i)
        sum += i * count

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