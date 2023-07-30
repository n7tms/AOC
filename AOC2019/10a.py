# Trying to calculate lines was not working; some were not being counted at all; 
# many were being calculated multiple times.
# Let's try a new approach!!
# Let's calculate a heading from one asteroid to every other asteroid. 
# We'll store the headings in a set.
# If there are multiple asteroids on that heading, only one will be recorded.
# ... meaning any asteroids 'behind' other asteroids will be ignored.
# The asteroid with the most 'headings' will be the best asteroid.

import math
import getaoc as ga

def get_input():
    data = ga.get_input(10,2019).splitlines()
    return data

def identify_asteroids(galaxy: list) -> set:
    asteroids = set()
    for r,row in enumerate(galaxy):
        for c,col in enumerate(row):
            if col == "#":
                asteroids.add((c,r))
    return asteroids


def calc_heading(src, dst):
    heading = math.atan2(dst[0] - src[0], src[1] - dst[1]) * 180 / math.pi
    if heading < 0:
        return 360 + heading
    return heading



def part1(data: list) -> list:
    asteroids = identify_asteroids(data)

    best_asteroid = None
    seen_asteroids = 0

    for source in asteroids:

        a = []
        for destination in asteroids:
            if source != destination:
                a.append(calc_heading(source,destination))

        b = {calc_heading(source, destination) for destination in asteroids if source != destination}


        # cnt = len({angle(start, end) for end in asteroids if start != end})
        cnt = len(set(calc_heading(source, destination) for destination in asteroids if source != destination))
        if cnt > seen_asteroids:
            seen_asteroids = cnt
            best_asteroid = source

    print(f"Part1: Asteroids seen from {best_asteroid}: {seen_asteroids}")

    # The list of asteroids and the best asteroid will be used in part2.
    return asteroids, best_asteroid



def part2(asteroids: list, best_asteroid: list) -> None:
    # remove the "best_asteroid" from the list of asteroids; we don't want to 
    # vaporize the rock we're sitting on!
    asteroids.remove(best_asteroid)

    # Sort the headings so we vaporize asteroids starting at 0 and proceed clockwise
    # These will be sorted first on heading, then on distance from "best_asteroid".
    # This will ensure that the closest asteroid is vaporized before the ones behind it.
    headings = sorted(
        ((calc_heading(best_asteroid, destination), destination) for destination in asteroids),
        key=lambda x: (x[0], abs(best_asteroid[0] - x[1][0]) + abs(best_asteroid[1] - x[1][1]))
    )


    # Iterating through the headings. We'll vaporize the first asteroid by taking
    # it off the list. If there are more asteroids on that same heading, they will be 
    # behind the first. So, continue iterating through the headings until we find the 
    # next different heading. Vaporize that one. Then continue to the next different
    # heading....until we've vaporized 199 asteroids. Which asteroid will be the 200th?

    # Initialize the heading_index to 0 and vaporize the first asteroid.
    heading_index = 0
    last_asteroid = headings.pop(heading_index)
    last_heading = last_asteroid[0]
    vaporized = 1

    while vaporized < 200 and headings:
        if heading_index >= len(headings):
            # We've gone all the way around; start over at 0.
            heading_index = 0
            last_heading = None
        if last_heading == headings[heading_index][0]:
            # This asteroid is on the same heading as the last; skip it.
            heading_index += 1
            continue

        # This asteroid must be on a new heading; vaporize it!
        last_asteroid = headings.pop(heading_index)
        last_heading = last_asteroid[0]
        vaporized += 1

    # 199 have been vaporized. Print the 200th!
    print(f"Part2: 200th to be Vaporized - {last_asteroid[1][0] * 100 + last_asteroid[1][1]} {last_asteroid[1]}")


def main():
    asteroids, best_asteroid = part1(get_input())
    part2(asteroids, best_asteroid)

if __name__ == "__main__":
    main()