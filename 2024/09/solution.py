# Standard library imports
import pathlib
import sys
from itertools import chain


def parse_data(puzzle_input):
    """Parse input."""
    explicit = []
    id = 0

    if len(puzzle_input) % 2 != 0:
        puzzle_input += "0"

    pairs = list(zip(puzzle_input[0::2], puzzle_input[1::2]))
    for files, space in pairs:
        strid = str(id)
        test = [strid for _ in range(int(files))]
        test2 = ["." for _ in range(int(space))]

        explicit.append(test)
        explicit.append(test2)
        id += 1

    return explicit, [x for xs in explicit for x in xs]


def sort(data):
    # iterate over data in reverse
    # if the current element is a dot, skip it
    last_empty_spot = 0
    for i in range(len(data) - 1, -1, -1):

        if data[i] == ".":
            continue

        # if the current element is a number, swap it with the earliest dot in the list
        for j in range(last_empty_spot, len(data) - 1):
            if j >= i:
                return data

            if data[j] == ".":
                data[j] = data[i]
                data[i] = "."

                last_empty_spot = j + 1
                break

    return data


def part1(data):
    """Solve part 1."""
    _, flattened = data
    flattened = sort(flattened)

    checksum = 0
    # calculate checksum
    for i in range(len(flattened)):
        if flattened[i] == ".":
            continue

        checksum += int(flattened[i]) * i

    return checksum


def sort2(raw_data):
    for i in range(len(raw_data) - 1, -1, -1):

        # if the current sequence is a file, swap it with the earliest sequence of free space that can contain it
        for j in range(len(raw_data) - 1):
            if j >= i:
                continue
            
            if "." in raw_data[i] or len(raw_data[i]) == 0:
                continue

            if '.' not in raw_data[j]:
                continue

            if len(raw_data[j]) < len(raw_data[i]):
                continue

            # we found a potential spot with enough free space
            sequence_length = 0
            for k in range(len(raw_data[j])):
                if raw_data[j][k] != ".":
                    sequence_length = 0
                    continue
                else:
                    sequence_length += 1
                if sequence_length == len(raw_data[i]):
                    for index, l in enumerate(raw_data[i]):

                        raw_data[j][k - (sequence_length-1) + index] = l
                    raw_data[i] = ["." for _ in range(len(raw_data[i]))]
                    continue

    return [x for xs in raw_data for x in xs]


def part2(data):
    """Solve part 2."""
    raw_data, _ = data
    flattened = sort2(raw_data)

    checksum = 0
    # calculate checksum
    for i in range(len(flattened)):
        if flattened[i] == ".":
            continue

        checksum += int(flattened[i]) * i

    return checksum


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
