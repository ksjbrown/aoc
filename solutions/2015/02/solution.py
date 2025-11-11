import sys


def main(input: str):
    print(part1(input))
    print(part2(input))


def part1(input: str) -> str:
    total_area = 0
    for line in input.splitlines():
        l, w, h = [int(x) for x in line.split("x", 3)]
        sides = [l * w, l * h, w * h]
        area = sum(2 * side for side in sides) + min(sides)
        total_area += area
    return str(total_area)


def part2(input: str) -> str:
    total_length = 0
    for line in input.splitlines():
        l, w, h = [int(x) for x in line.split("x", 3)]
        perimeters = [2 * l + 2 * h, 2 * l + 2 * w, 2 * w + 2 * h]
        length = min(perimeters) + l * w * h
        total_length += length
    return str(total_length)


if __name__ == "__main__":
    main(sys.stdin.read())
