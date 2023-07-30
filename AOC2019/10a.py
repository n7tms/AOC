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
    # data = ga.get_input(10,2019,False,"AOC2019/10_sample_1.txt").splitlines()

    # --- do other parsing here if necessary ---
    # convert the lines of strings to list of numbers
    # data = [int(line) for line in data[0].split(',')]

    # data = ['.#..#','.....','#####','....#','...##']

    # return the parsed data
    # data = ga.rotate_cw(data)
    # data = np.fliplr(data)
    return data

def identify_asteroids(galaxy: list) -> set:
    asteroids = set()
    for r,row in enumerate(galaxy):
        for c,col in enumerate(row):
            if col == "#":
                asteroids.add((c,r))
    return asteroids


def calc_angle(src, dst):
    heading = math.atan2(dst[0] - src[0], src[1] - dst[1]) * 180 / math.pi
    if heading < 0:
        return 360 + heading
    return heading



def part1(data):
    asteroids = identify_asteroids(data)

    best_asteroid = None
    seen_asteroids = 0

    for source in asteroids:

        a = []
        for destination in asteroids:
            if source != destination:
                a.append(calc_angle(source,destination))

        b = {calc_angle(source, destination) for destination in asteroids if source != destination}


        # cnt = len({angle(start, end) for end in asteroids if start != end})
        cnt = len(set(calc_angle(source, destination) for destination in asteroids if source != destination))
        if cnt > seen_asteroids:
            seen_asteroids = cnt
            best_asteroid = source

    print('x {} y {}'.format(*best_asteroid))
    print('visible {}'.format(seen_asteroids))

    return asteroids, best_asteroid


# my part2 might not work. I am storing the asteroids as a set. If I remove a
# heading from the "set", it removes all the asteroids on that heading. What
# about the asteroids that might exist behind it??
def part2(asteroids, best_asteroid):
    # remove the "best_asteroid" from the list of asteroids; we don't want to 
    # vaporize the rock we're sitting on!
    asteroids.remove(best_asteroid)

    # sort the headings so we vaporize asteroids starting at 0 and around clockwise
    angles = sorted(
        ((calc_angle(best_asteroid, destination), destination) for destination in asteroids),
        key=lambda x: (x[0], abs(best_asteroid[0] - x[1][0]) + abs(best_asteroid[1] - x[1][1]))
    )

    idx = 0
    last = angles.pop(idx)
    last_angle = last[0]
    cnt = 1

    while cnt < 200 and angles:
        if idx >= len(angles):
            idx = 0
            last_angle = None
        if last_angle == angles[idx][0]:
            idx += 1
            continue
        last = angles.pop(idx)
        last_angle = last[0]
        cnt += 1
    print('vaporized {}: {} {}'.format(cnt, last[1], last[1][0] * 100 + last[1][1]))


def main():
    asteroids, best_asteroid = part1(get_input())
    part2(asteroids, best_asteroid)

if __name__ == "__main__":
    main()