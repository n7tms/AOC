# aoc_utils.py
import os
import subprocess
import time
import numpy as np
import logging


DIRS = ([-1,-1],[0,-1],[1,-1],[-1,0],[0,0],[1,0],[-1,1],[0,1],[1,1])

logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)
logger = logging.getLogger('AOC')

    

# def retrieve(year, day):
#     cmd = "curl https://adventofcode.com/" + str(year) + "/day/" + str(day) + "/input --cookie \"session=" + COOKIE + "\" > " + str(year) + str(day).zfill(2) + ".txt"
#     # print(os.system(cmd))
#     print(cmd)


def read_cookie():
    with open('AOC2023/cookie.in') as fp:
        data = fp.read()
    return data


def get_input(year, day, force=False):
    # Does force=True? or Does the file not exist?
    #   Yes: retrieve the input data and [over]write the txt file.
    # Does the file exist and force=False?
    #   Yes: return None

    cookie = read_cookie()

    # target_file = "AOC2023\\inputs\\" + str(year) + str(day).zfill(2) + ".in"
    target_file = os.path.join("AOC2023","inputs",str(year) + str(day).zfill(2) + ".in")
    # print(target_file)
    if os.path.exists(target_file) and not force:
        print(f"retrieve(): '{target_file}' already exists. (force not True)")
        return None
    else:
        cmd = "curl https://adventofcode.com/" + str(year) + "/day/" + str(day) + "/input --cookie \"session=" + cookie + "\" > " + target_file 
        print(cmd)
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)

        # give the subprocess time to finish
        time.sleep(3)


def empty_matrix(rows: int,cols: int, fill_value=0) -> list:
    return [[fill_value] * cols for _ in range(rows)]
    # return [[fill_value] * cols] * rows


def manhattan_distance(a: tuple, b: tuple) -> int:
    """
    Give two tuples or lists, each consisting of 1 pair of integers,
    return the Manhattan distance between the two points.
    abs(a[0] - b[0]) + abs(a[1] - b[1])
    """
    return abs(a[0]-b[0]) + abs(a[1]-b[1])


def rotate90(data: list, dir=-1) -> list:
    tmp = []
    for r in data:
        new_row = []
        for c in r:
            new_row.append(c)
        tmp.append(new_row)

    tmp = list(np.rot90(tmp,dir))
    # mash everything back together
    final_array = []
    for r in tmp:
        final_array.append("".join([str(item) for item in r]))

    return final_array

def shoelace_formula(data: list, include_border=False) -> float:
    """
    Calculates the area of an irregular polygon
    (Based on: https://www.themathdoctors.org/polygon-coordinates-and-areas/)
    This is similar to Pick's Theorem, but Pick's integer coordinates; Shoelace does not.

    Args:
        data (list):            an array of vertices [[(x1,y1),(x2,y2)], [(x2,y2),(x3,y3)], ...]
        include_border (bool):  determines if the boundary of the area should also be included
                                in the area (True) or just the area inside the boundary (False).
    
    Returns:
        float: the area of the polygon
        
    Note: each row in data may consist of additional information. Only the first
          two elements in each row are used to calculate the area.
    """

    perimeter = 0
    # Shoelace Formula
    s1,s2 = 0,0
    for line in data:
        s1 += (line[0][0] * line[1][1])
        s2 += (line[1][0] * line[0][1])
        if line[0][0] == line[1][0]:
            perimeter += abs(line[0][1]-line[1][1])
        else:
            perimeter += abs(line[0][0]-line[1][0])

    area = .5 * abs(s1 - s2)
    if include_border:
        area += perimeter//2 + 1

    return area
