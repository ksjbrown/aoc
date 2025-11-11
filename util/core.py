import pathlib


def get_dir_project_root() -> pathlib.Path:
    dir = pathlib.Path(__file__).parent
    while True:
        if (dir / ".git").is_dir():
            return dir
        assert dir != dir.parent
        dir = dir.parent


def get_dir_solution(year: int, day: int) -> pathlib.Path:
    return get_dir_project_root() / f"solutions/{year}/{day:02}"


def get_env() -> dict[str, str]:
    env = {}
    path_env = get_dir_project_root() / ".env"
    if path_env.is_file():
        with open(path_env, "r") as f:
            for line in f:
                key, value = line.split("=")
                env[key.strip()] = value.strip()
    return env


def get_session_cookie() -> str:
    return "session=" + get_env()["session"]
