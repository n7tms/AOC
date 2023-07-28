# Code to get input from AOC website
# Original source: https://github.com/alvesvaren/AoC-template/blob/main/aoc/_api.py
# The original code has been adapted to my own environment and preferences.
# TODO Consider incorporating this into a master AOC utility module.

from typing import Union
import requests
from pathlib import Path
from datetime import datetime

_SESSION_FILE_NAME = "session.txt"
_YEAR_FILE_NAME = "AOC2019/year.txt"


def _set_read_file(filename: str, default: str = None) -> Union[str, None]:
    try:
        with open(filename) as file:
            return file.read()
    except FileNotFoundError:
        if default:
            with open(filename, "w") as file:
                file.write(default)
                return default
        return None


SESSION = _set_read_file(_SESSION_FILE_NAME)
if not SESSION:
    SESSION = _set_read_file(
        _SESSION_FILE_NAME,
        input("Enter your session cookie: "))
assert SESSION is not None
SESSION = SESSION.strip()

YEAR = _set_read_file(_YEAR_FILE_NAME)
if not YEAR:
    YEAR = _set_read_file(
        _YEAR_FILE_NAME,
        str(datetime.now().year))
    assert YEAR is not None
YEAR = int(YEAR.strip())

def get_input(day: int, year: int = YEAR, overwrite: bool = False, filename: str = None):
    """
    Usage:
    ```python
    import aoc
    data_rows = aoc.get_input(5).splitlines()
    ```python
    """

    # Path("data").mkdir(exist_ok=True)

    if filename == None:
        # file_name = f"data/{year}_{day}.txt"
        file_name = f"AOC2019/{year}_{day}.in"
    else:
        file_name = filename

    data = None if overwrite else _set_read_file(file_name)
    if not data:
        response = requests.get(
                f"https://adventofcode.com/{year}/day/{day}/input",
                cookies={"session": SESSION})
        if not response.ok:
            if response.status_code == 404:
                raise FileNotFoundError(response.text)
            raise RuntimeError(f"Request failed, code: {response.status_code}, message: {response.content}")
        data = _set_read_file(
            file_name,
            response.text[:-1])
    if data is None:
        raise FileNotFoundError(f"Data could not be fetched for day {day}")
    return data


# rotate a 2-dimensional list 90 degrees clockwise
def rotate_cw(data: list) -> list:
    """Rotate a 2-dimensional list clockwise.
    Note: Works on other-dimensional lists, too, but
    your mileage may vary."""
    return list(zip(*data[::-1]))

