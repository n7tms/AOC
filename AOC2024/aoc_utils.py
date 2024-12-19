# aoc_utils.py
import os
import subprocess
import time
# import numpy as np
import logging


    

# def retrieve(year, day):
#     cmd = "curl https://adventofcode.com/" + str(year) + "/day/" + str(day) + "/input --cookie \"session=" + COOKIE + "\" > " + str(year) + str(day).zfill(2) + ".txt"
#     # print(os.system(cmd))
#     print(cmd)


def read_cookie(year):
    with open('AOC' + str(year) + '/cookie.in') as fp:
        data = fp.read()
    return data


def get_input(year, day, force=False):
    # Does force=True? or Does the file not exist?
    #   Yes: retrieve the input data and [over]write the txt file.
    # Does the file exist and force=False?
    #   Yes: return None

    cookie = read_cookie(year)

    target_file = os.path.join("AOC"+str(year),"inputs",str(year) + "-" + str(day).zfill(2) + ".in")
    # print(target_file)
    if os.path.exists(target_file) and not force:
        # print(f"retrieve(): '{target_file}' already exists. (force not True)")
        return None
    else:
        cmd = "curl https://adventofcode.com/" + str(year) + "/day/" + str(int(day)) + "/input --cookie \"session=" + cookie + "\" > " + target_file 
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
    This is similar to Pick's Theorem, but Pick's requires integer coordinates; Shoelace does not.

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



def flood_fill(data: list, start: tuple, old: any, new:any, changed=[]) -> list:
    """
    Fill an area of an array with a value.
    flood_fill assumes the boundary is one value (old).

    Args:
        data (list):   a 2D array of values
        start (tuple):  a 2-element tuple representing the coordinate (r,c) to start flooding
        old (any):      the value representing the boundary of the field to flood
        new (any):      the value to flood the field with

    Returns:
        (list):         returns the flooded field
    """


    # starting coords
    r,c = start

    # make sure the current coords are inside the array.
    if not (0 <= c < len(data[0])) or not (0 <= r < len(data)):
        return

    # if the current coords are on the boundary (or don't match the old value),
    # return without doing anything.
    if data[r][c] != old:
        return

    # change the value at the current coords to the new value
    data[r][c] = new
    changed.append((r,c))

    # recursively flood the surrounding cells
    flood_fill(data, (r+1, c), old, new, changed)
    flood_fill(data, (r-1, c), old, new, changed)
    flood_fill(data, (r, c+1), old, new, changed)
    flood_fill(data, (r, c-1), old, new, changed)

    return data, changed


from collections import deque

def bfs_shortest_path(valid_points, start, target):
    """
    Perform a BFS search to find the shortest path from start to target.

    :param valid_points: List of tuples representing valid points on the map.
    :param start: Starting point (x, y).
    :param target: Target point (x, y).
    :return: A list representing the shortest path from start to target if one exists, otherwise None.
    """
    valid_set = set(valid_points)  # Use a set for quick lookup

    if start not in valid_set or target not in valid_set:
        return None

    # Directions for adjacency (vertical and horizontal only)
    directions = [
        (-1, 0), (1, 0), (0, -1), (0, 1)
    ]

    def get_neighbors(point):
        x, y = point
        neighbors = [(x + dx, y + dy) for dx, dy in directions]
        return [n for n in neighbors if n in valid_set]

    queue = deque([(start, [start])])  # Queue stores (current_point, path_so_far)
    visited = set()

    while queue:
        current, path = queue.popleft()

        if current == target:
            return path

        if current in visited:
            continue

        visited.add(current)

        for neighbor in get_neighbors(current):
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))

    return None


def count_direction_changes(path):
    if not path or len(path) < 3:
        return 0

    direction_changes = 0

    # Helper function to calculate direction
    def get_direction(p1, p2):
        return (p2[0] - p1[0], p2[1] - p1[1])

    # Iterate through the path and count changes in direction
    for i in range(1, len(path) - 1):
        dir1 = get_direction(path[i - 1], path[i])
        dir2 = get_direction(path[i], path[i + 1])

        if dir1 != dir2:
            direction_changes += 1

    return direction_changes



def can_generate_design(sub_designs, design):
    """
    Determines if the design can be generated using the sub_designs.

    Args:
    - sub_designs (list): List of patterns to be used to generate the design (e.g., ['r', 'wr', 'b', ...]).
    - design (str): The design string to generate (e.g., 'brwrr').

    Returns:
    - bool: True if the design can be generated, False otherwise.
    """
    n = len(design)
    dp = [False] * (n + 1)
    dp[0] = True  # Base case: an empty design can always be generated

    for i in range(1, n + 1):
        for sub_design in sub_designs:
            if dp[i - len(sub_design)] and design[i - len(sub_design):i] == sub_design:
                dp[i] = True
                break

    return dp[n]

def ways_to_generate_design(sub_designs, design):
    """
    Counts the number of ways the design can be generated using the sub_designs.

    Args:
    - sub_designs (list): List of patterns to be used to generate the design (e.g., ['r', 'wr', 'b', ...]).
    - design (str): The design string to generate (e.g., 'brwrr').

    Returns:
    - int: The number of ways the design can be generated.
    """
    n = len(design)
    dp = [0] * (n + 1)
    dp[0] = 1  # Base case: one way to generate an empty design

    for i in range(1, n + 1):
        for sub_design in sub_designs:
            if i >= len(sub_design) and design[i - len(sub_design):i] == sub_design:
                dp[i] += dp[i - len(sub_design)]

    return dp[n]