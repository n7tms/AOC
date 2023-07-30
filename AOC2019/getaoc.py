# Code to get input from AOC website
# Original source: https://github.com/alvesvaren/AoC-template/blob/main/aoc/_api.py
# The original code has been adapted to my own environment and preferences.
# TODO Consider incorporating this into a master AOC utility module.

from typing import Union
import requests
from pathlib import Path
from datetime import datetime
import math

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




def get_input(day: int, year: int = 2019, overwrite: bool = False, filename: str = None):
    """
    Usage:
    ```python
    import aoc
    data_rows = aoc.get_input(5).splitlines()
    ```python
    """

    # Path("data").mkdir(exist_ok=True)

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


def intersecting_points(src: list, dst:list) -> list:
    """Intersecting_points uses a modified version of Bresenham's
    algorithm to plot points that intersect a line between two 
    given points. The list of points returned includes the end
    points.
    As a side benefit, this returns the points IN ORDER from the
    source to the destination.
    NOTE: DUE TO ROUNDING ERRORS, IT DOES NOT ALWAYS FIND ALL INTERSECTIONS!"""
    
    x0,y0 = src
    x1,y1 = dst

    dx = x1 - x0
    dy = y1 - y0

    points = []

    if abs(dx) >= abs(dy):
        steps = abs(dx)
    else:
        steps = abs(dy)

    x_increment = dx / steps
    y_increment = dy / steps

    x = x0
    y = y0
    for _ in range(steps + 1):
        if round(x) == x and round(y) == y:
            points.append([round(x),round(y)])
        x += x_increment
        y += y_increment
    
    return points


def calc_heading(src: list, dst: list) -> float:
    """Given two points (eg. (1,3) and (5,6)), calc_heading calculates the heading
    or bearing FROM the src TO the dst, in degrees, and returns the value as a float. """
    heading = math.atan2(dst[0] - src[0], src[1] - dst[1]) * 180 / math.pi
    if heading < 0:
        return 360 + heading
    return heading
