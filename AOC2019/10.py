# AOC 2019 Day 10
#
import getaoc as ga
from intcode_c import Intcode
import numpy as np


def get_input():
    # data = ga.get_input(10,2019).splitlines()
    data = ga.get_input(10,2019,False,"AOC2019/10_sample_a.txt").splitlines()

    # --- do other parsing here if necessary ---
    # convert the lines of strings to list of numbers
    # data = [int(line) for line in data[0].split(',')]

    # data = ['.#..#','.....','#####','....#','...##']

    # return the parsed data
    # data = ga.rotate_cw(data)
    # data = np.fliplr(data)
    return data

def identify_asteroids(galaxy: list) -> list:
    asteroids = []
    for r,row in enumerate(galaxy):
        for c,col in enumerate(row):
            if col == "#":
                asteroids.append([c,r])
    return asteroids


def old_blocked(galaxy: list, points: list) -> bool:
    """If any of the 'points' correspond to an asteroid "#"
    in the 'galaxy', then return True (blocked); otherwise 
    return False (not blocked)."""

    for point in points:
        x,y = point
        if galaxy[x][y] == "#":
            return True
    return False

def blocked(asteroids: list, points: list) -> bool:
    for point in points:
        if point in asteroids:
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

def part1(data):            # -> <248
    asteroids = identify_asteroids(data)

    detected = {}

    for sr, src_r in enumerate(data):
        for sc, src_c in enumerate(src_r):
            # we don't need to check this point if there is no asteroid there
            if src_c == '.':
                continue
            # There is an asteroid at the src. Add it to detected.
            detected[(sc, sr)] = 0

            # now iterate through the galaxy again and determine which asteroids
            # can be seen from THIS asteroid.
            for dr, dst_r in enumerate(data):
                for dc, dst_c in enumerate(dst_r):
                    # if the src and dst are the same, ignore this iteration
                    if sr == dr and sc == dc:
                        continue

                    # if there is an asteroid at this point, then generate
                    # a list of every point between src and dst. Then check
                    # the intersecting points between then. If an asteroid
                    # does not exist at any of the points, then increment
                    # the detected count.
                    if dst_c == '#':
                        points_between = intersecting_points([sc,sr],[dc,dr])
                        print(points_between)
                        if not blocked(asteroids,points_between[1:-1]):
                            detected[(sc,sr)] += 1
    print(detected)
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




