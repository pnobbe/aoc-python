# Standard library imports
from functools import lru_cache
import pathlib
import sys
import time


def parse_data(puzzle_input):
    """Parse input."""
    return list(map(int, puzzle_input.split()))


@lru_cache(maxsize=None)
def blink(stone, times_remaining):
    if times_remaining == 0:
        return 1

    str_stone = str(stone)
    match stone:
        case 0:
            return blink(1, times_remaining - 1)
        case _ if (l := len(str_stone)) % 2 == 0:
            return blink(int(str_stone[: l // 2]), times_remaining - 1) + blink(
                int(str_stone[l // 2 :]), times_remaining - 1
            )
        case _:
            return blink(stone * 2024, times_remaining - 1)


def part1(stones):
    """Solve part 1."""
    return sum([blink(stone, 25) for stone in stones])


def part2(stones):
    """Solve part 2."""
    return sum([blink(stone, 75) for stone in stones])


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    stones = parse_data(puzzle_input)
    yield part1(stones)
    yield part2(stones)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(puzzle_input=pathlib.Path(path).read_text().rstrip())
        print("\n".join(str(solution) for solution in solutions))
