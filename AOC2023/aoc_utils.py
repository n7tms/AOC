# aoc_utils.py
import os
import subprocess
import time

DIRS = ([-1,-1],[0,-1],[1,-1],[-1,0],[0,0],[1,0],[-1,1],[0,1],[1,1])


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


def empty_matrix(x,y):
    return [[0] * y] * x

def manhattan_distance(a: tuple, b: tuple) -> int:
    """
    Give two tuples or lists, each consisting of 1 pair of integers,
    return the Manhattan distance between the two points.
    abs(a[0] - b[0]) + abs(a[1] - b[1])
    """
    return abs(a[0]-b[0]) + abs(a[1]-b[1])
    