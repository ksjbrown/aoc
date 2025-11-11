import pathlib
import sys
import urllib.request

import util.core


def main():
    b = get_input(int(sys.argv[1]), int(sys.argv[2]))
    sys.stderr.buffer.write(b)


def get_input(year: int, day: int) -> bytes:
    path = get_input_path(year, day)
    if not path.is_file():
        download_remote_input(year, day, target=path)
    with open(path, "rb") as f:
        return f.read()


def get_input_path(year: int, day: int) -> pathlib.Path:
    return util.core.get_dir_solution(year, day) / "input.txt"


def get_input_url(year: int, day: int) -> str:
    return f"https://adventofcode.com/{year}/day/{day}/input"


def download_remote_input(year: int, day: int, target: str | pathlib.Path) -> None:
    url = get_input_url(year, day)
    req = urllib.request.Request(url)
    cookie = util.core.get_session_cookie()
    req.add_header("Cookie", cookie)

    with urllib.request.urlopen(req) as resp:
        path = pathlib.Path(target)
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "wb") as f:
            f.write(resp.read())


if __name__ == "__main__":
    main()
