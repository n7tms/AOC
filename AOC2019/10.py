# AOC 2019 Day 10
#
import getaoc as ga
from intcode_c import Intcode
import numpy as np


def get_input():
    data = ga.get_input(10,2019).splitlines()
    # data = ga.get_input(10,2019,False,"AOC2019/10_sample_a.txt").splitlines()

    # --- do other parsing here if necessary ---
    # convert the lines of strings to list of numbers
    # data = [int(line) for line in data[0].split(',')]

    # data = ['.#..#','.....','#####','....#','...##']


    # return the parsed data
    data = ga.rotate_cw(data)
    data = np.fliplr(data)
    return data


def blocked(galaxy: list, points: list) -> bool:
    """If any of the 'points' in the 'galaxy' contain an
    asteroid '#', then return True (blocked); otherwise 
    return False (not blocked)."""

    for point in points:
        x,y = point
        if galaxy[x][y] == "#":
            return True
    return False


def intersecting_points(src: list, dst:list) -> list:
    """intersecting_points uses a modified version of Bresenham's
    algorithm to plot points that intersect a line between two 
    given points. The list of points returned includes the end
    points.
    As a side benefit, this returns the points IN ORDER from the
    source to the destination."""
    
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

# I might be able to improve the performance by creating a set or list of
# all the points in the galaxy that have an asteroid. Then I could just 
# do something like "if point in asteroids:..."

def part1(data):            # -> <248

    detected = {}

    # print(intersecting_points(src,dst)[1:-1])

    for src_r in range(len(data)):
        for src_c in range(len(data[src_r])):
            # we don't need to check this point if there is no asteroid there
            if data[src_r][src_c] == '.':
                continue
            # There is an asteroid at the src. Add it to detected.
            detected[(src_r,src_c)] = 0
            for dst_r in range(len(data)):
                for dst_c in range(len(data[dst_r])):
                    # if the src and dst are the same, ignore this iteration
                    if src_c == dst_c and src_r == dst_r:
                        continue

                    # if there is an asteroid at this point, then generate
                    # a list of every point between src and dst. Then check
                    # the intersecting points between then. If an asteroid
                    # does not exist at any of the points, then increment
                    # the detected count.
                    if data[dst_r][dst_c] == '#':
                        points_between = intersecting_points([src_r,src_c],[dst_r,dst_c])
                        if not blocked(data,points_between[1:-1]):
                            detected[(src_r,src_c)] += 1
    # print(detected)
    # print(detected[(5,8)])
    print(sorted(detected.items(),key=lambda x:x[1]))
    print(max(zip(detected.values(), detected.keys())))
    


def part2(data):            # -> ?
    ...


if __name__ == "__main__":
    part1(get_input())
    part2(get_input())


# Samples

# .7..7
# .....
# 67775
# ....7
# ...87


# This code might come in handy
# import numpy as np
# arr = np.array([[1,2,3,4],[5,6,7,8]])
# for idx, x in np.ndenumerate(arr):
#     print(idx,x)
# outputs
#  (0,0) 1
#  (0,1) 2
# etc
# consider NetworkX package




