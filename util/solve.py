import io
import pathlib
import subprocess
import sys
from typing import Callable

import util.core
import util.input


def main():
    year = int(sys.argv[1])
    day = int(sys.argv[2])
    solutions = solve(year, day)
    if len(solutions) == 0:
        print(f"No solutions for year {year}, day {day}", file=sys.stderr)
        return
    for ft, parts in solve(year, day).items():
        print(f"Solution: {ft}")
        print(f"  Part 1: {parts[0]}")
        print(f"  Part 2: {parts[1]}")


def solve(year: int, day: int) -> dict[str, tuple[str, str]]:
    """Runs the solution, returning the printed output.

    The application detects the solution type, and runs the solution,
    according to the solution rules for that file type.
    """
    res: dict[str, tuple[str, str]] = {}
    dir = util.core.get_dir_solution(year, day)
    input = util.input.get_input(year, day)
    for ft, solver in _solvers.items():
        for path in dir.glob(ft):
            solution = solver(path, input)
            part1, part2 = solution.splitlines()
            res.update({str(path): (part1, part2)})
    return res


T_Solver = Callable[[pathlib.Path, bytes], str]
_solvers: dict[str, T_Solver] = {}


def register_solver(ft: str) -> Callable[[T_Solver], T_Solver]:
    def decorator(fn: T_Solver) -> T_Solver:
        _solvers[ft] = fn
        return fn

    return decorator


@register_solver("solution.py")
def solve_python(path: pathlib.Path, input: bytes) -> str:
    """Gets a path to the solution directory.
    Returns a command that when executed, reads task input from stdin, and writes task output to stdout
    """
    res = subprocess.run(
        [
            "python",
            str(path),
        ],
        capture_output=True,
        input=input,
    )
    return res.stdout.decode()


if __name__ == "__main__":
    main()
