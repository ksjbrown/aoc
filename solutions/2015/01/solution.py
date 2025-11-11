import sys


def main(input: str):
    print(part1(input))
    print(part2(input))


def part1(input: str) -> str:
    floor = 0
    for c in input:
        if c == "(":
            floor += 1
        elif c == ")":
            floor -= 1
    return str(floor)


def part2(input: str) -> str:
    floor = 0
    for i, c in enumerate(input, 1):
        if c == "(":
            floor += 1
        elif c == ")":
            floor -= 1
        if floor == -1:
            return str(i)
    raise RuntimeError("did not reach basement")


if __name__ == "__main__":
    main(sys.stdin.read())
