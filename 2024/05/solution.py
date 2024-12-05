# Standard library imports
import pathlib
import sys


def validate(update, page_ordering_rules):
    for i in range(len(update)):
        before = update[:i]
        rules = page_ordering_rules.get(update[i])

        if rules is None:
            continue

        for b in before:
            if b in rules:
                return False

    return True


def fix(update, page_ordering_rules):
    for i in range(len(update)):
        current = update[i]
        before = update[:i]
        rules = page_ordering_rules.get(update[i])

        if rules is None:
            continue

        for rule in rules:
            for b in range(len(before)):
                if rule == before[b]:
                    del update[i]
                    update.insert(b, current)
                    return update

    return update


def parse_data(puzzle_input):
    """Parse input."""
    lines = puzzle_input.splitlines()
    page_ordering_rules = {}
    updates = []
    for line in lines:
        if "|" in line:
            x, y = map(int, line.split("|"))
            if page_ordering_rules.get(x) is None:
                page_ordering_rules[x] = [y]
            else:
                page_ordering_rules[x].append(y)
        elif "," in line:
            updates.append(list(map(int, line.split(","))))

    return (page_ordering_rules, updates)


def part1(data):
    """Solve part 1."""
    page_ordering_rules, updates = data

    correct_updates = []
    for update in updates:
        if validate(update, page_ordering_rules):
            correct_updates.append(update)

    sum = 0
    for update in correct_updates:
        sum += update[int(len(update) / 2)]

    return sum


def part2(data):
    """Solve part 2."""
    page_ordering_rules, updates = data

    incorrect_updates = []
    for update in updates:
        if not validate(update, page_ordering_rules):
            incorrect_updates.append(update)

    sum = 0
    for update in incorrect_updates:
        while not validate(update, page_ordering_rules):
            update = fix(update, page_ordering_rules)

        sum += update[int(len(update) / 2)]

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
