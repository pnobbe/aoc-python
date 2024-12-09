# Standard library imports
import pathlib
import sys


def parse_data(puzzle_input):
    """Parse input."""
    # load a matrix
    matrix = puzzle_input.splitlines()
    # find all unique frequencies, add to dictionary with cell as key and list of coordinates of each satellite as value
    frequencies = {}
    for i, row in enumerate(matrix):
        for j, cell in enumerate(row):
            if cell != ".":
                if cell not in frequencies:
                    frequencies[cell] = []
                frequencies[cell].append((i, j))

    return matrix, frequencies


def part1(data):
    """Solve part 1."""
    matrix, frequencies = data

    antinodes_in_bounds = set()
    for frequency in frequencies:
        antinodes = set()

        # get all antennas for this frequency
        antennas = frequencies[frequency]
        for antenna in antennas:
            other_antennas = antennas.copy()
            other_antennas.remove(antenna)

            # find antinodes for all antenna pairs
            for other_antenna in other_antennas:
                distance = (
                    other_antenna[0] - antenna[0],
                    other_antenna[1] - antenna[1],
                )

                antinodes.add((antenna[0] - distance[0], antenna[1] - distance[1]))
                antinodes.add((antenna[0] + distance[0], antenna[1] + distance[1]))

        # remove antinodes that overlap with antennas of the same frequency
        for antenna in antennas:
            antinodes.discard(antenna)

        # remove antinodes that are out of bounds
        for antinode in antinodes:
            if (
                antinode[0] < 0
                or antinode[0] >= len(matrix)
                or antinode[1] < 0
                or antinode[1] >= len(matrix[0])
            ):
                continue

            antinodes_in_bounds.add(antinode)

    return len(antinodes_in_bounds)


def part2(data):
    """Solve part 2."""
    matrix, frequencies = data

    antinodes_in_bounds = set()
    for frequency in frequencies:
        antinodes = set()

        # get all antennas for this frequency
        antennas = frequencies[frequency]
        for antenna in antennas:
            other_antennas = antennas.copy()
            other_antennas.remove(antenna)

            # find antinodes for all antenna pairs
            for other_antenna in other_antennas:
                distance = (
                    other_antenna[0] - antenna[0],
                    other_antenna[1] - antenna[1],
                )

                # generate all antinodes)
                curX = antenna[0]
                curY = antenna[1]

                while curX >= 0 and curX < len(matrix) and curY >= 0 and curY < len(matrix[0]):
                    antinodes.add((curX, curY))
                    curX += distance[0]
                    curY += distance[1]     

                curX = antenna[0]
                curY = antenna[1]       
                
                while curX >= 0 and curX < len(matrix) and curY >= 0 and curY < len(matrix[0]):
                    antinodes.add((curX, curY))
                    curX -= distance[0]
                    curY -= distance[1]     

        # remove antinodes that overlap with antennas of the same frequency
        #for antenna in antennas:
        #    antinodes.discard(antenna)

        antinodes_in_bounds.update(antinodes)

    return len(antinodes_in_bounds)


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
