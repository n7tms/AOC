# AOC 2022 - Day 17
# @STheShadow
# https://topaz.github.io/paste/#XQAAAQCVDAAAAAAAAAA0m0pnuFI8c/z1tMiiq70jZKydaS+YAJkX6EweptKzs73FbdtQFWDpAePaTd5VIzpHBxeBo8gxHLYL6PpFJi32Fm0FSyoOthSbkrwi66gGzR9W0Nyo/4Iidb+p9Xcbb7ubGR09wsUZDgUIBbn64eVB42bexNEckIZBUigve8hnv1ckVnAMLKwfPFoBuQm/EtvCNV3OUhYprlWInCaBLZOwPl0UfhSubJDlRjsDb/3Go1u9mV0WYbQz3XzEUjepqjeJX78k+VATQSY8dHMcMs9ikXYXbZDFTQXZjivu30TrRYrfH1MAyzZlP5mEhmdi6b9cSFwONZzjBULhyCjaB9f+b7Ex9KCwUQ75THt66vkj77O0l8D+AUUxzNOmnudreMaQT54kNHFbIoUoo/GziyxdIHWAoXdbnaRoIlyhJK8r2w7269HP14nfYg9xsLdObE6NxX+eshgOkM2kS/8m7gGJTqMuGVu4ZVDdqYcWzqokx93ZhdQqM9FgKDXqmQY+5n+4HM9BkDx5KRKrEmMBfxh2cQe9YUNnKGxOy//5gdX+iGbJyJLhDbQ2yYVFEnbBx4R00u/1/VBgV9jmMJZ/Rz289lWfqSfpxwlbWr19EmoFS9ApkWorfQJDDoqceQAUywrhkOrtkcu8pWjbi5QGbgpAeEDJU7fzkRcq/s3w52wjOaPxjSX4sPR/N6FO2VtNnDfYmArLjTmkqXI0kDZtGHZHlxavtM+0e1OXM/2wOpUQEMr5qeZYh9zdMu2QlCCk5GR+JDlaaTdK8Y2w02PRey1uOCh2v6NEYq3K7AuxI3kIrTLhG7d/wnKj8QLlPUla8GEpJMG2V/p/CNnbiwbwj0jYJIPCish6P1sKzbVBfDVNuCJjOKvFS5tw02e2Bi4b5fgVLE5cm6x8DPlMtBn3JlNhLFOtHjBE0by7+Op143P9UHw0USX4k8lWx4pyhbGJYhZC7hFVLn2qxBRX8EV2SClaXBC4G9IIzaOINsyAsARk0eWLG6QalB1E1m296LT5HzDUGBpDIyU/6NJURwfGPPrGShUAY3ukogpnCq8h2P+nt6GyC8/FlYju1ZRelrA/HHO0VKyQsq97LFYf0aYqkQ/6gMxoDDyEV6nUBfy9KZ4OdAnhkqnVw9OxLyIobLXHFr4REHoimZUGm0BFwIA4LxAQmA9l0KCo3CFbOEdVoWe0gg9hFwGZaLUOsB0g2N1bHNwEgU9r6k3R3WhW0Yo6hybbhYsK6xUVXD0qQDG4ssGPXJEj/CeUP+4BBg4gOhdlSiIUWIpX9Yrao95xcCwENLMkY/JChnxOxVc12uLM6wHnLKp5bBRwf9Eoe11MZWO2n8WCQ7Y8HNe31GVdBiAzQIhusMSEvo411itq+9KijCng0RxPyaqmvfhXWOK6jakuBFfC/C/2gA==

# This solution gives a WRONG part 1 answer, but a correct part 2 answer.

import sys
import re
import numpy
import math
import time


def get_rock(h, cycle):
    m = cycle % 5
    a = 2 + 1j
    h += 4
    if m == 0:
        return {2 + h * 1j, 3 + h * 1j, 4 + h * 1j, 5 + h * 1j}
    elif m == 1:
        return {3 + h * 1j, 2 + (h+1) * 1j, 3 + (h+1) * 1j, 4 + (h+1) * 1j, 3 + (h+2) * 1j}
    elif m == 2:
        return {2 + h * 1j, 3 + h * 1j, 4 + h * 1j, 4 + (h+1) * 1j, 4 + (h+2) * 1j}
    elif m == 3:
        return {2 + h * 1j, 2 + (h+1) * 1j, 2 + (h+2) * 1j, 2 + (h+3) * 1j}
    elif m == 4:
        return {2 + h * 1j, 3 + h * 1j, 2 + (h+1) * 1j, 3 + (h+1) * 1j}


def move_rock_left(rock):
    if any([x.real == 0 for x in list(rock)]):
        return rock
    return set([complex(x. real - 1, x.imag) for x in list(rock)])


def move_rock_right(rock):
    if any([x.real == 6 for x in list(rock)]):
        return rock
    return set([complex(x. real + 1, x.imag) for x in list(rock)])


def move_rock_down(rock):
    return set([complex(x.real, x.imag - 1) for x in list(rock)])


def visualize_trench(trench, max_height):
    numpy.set_printoptions(threshold=sys.maxsize)
    vis = numpy.full((int(max_height) + 1, 7), 1)
    for occ in trench:
        vis[int(occ.imag), int(occ.real)] = 8
    print(numpy.flipud(vis))


if __name__ == '__main__':
    start_time = time.time()
    IN_FILE = "AOC2022\\inputs\\202217.txt"
    # IN_FILE = "AOC2022\\inputs\\202216.sample.txt"
    sample = ">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"

    with open(IN_FILE) as f:
        out = f.read()
    data = [-1 if x == "<" else 1 for x in list(out)]
    stop_time = time.time()
    print(f"Initialization time: {stop_time - start_time} seconds")
    # Parsing starts at 0+1i => real from the left, imag from the bottom. 1i = 1str row
    start_time = stop_time
    height, moves = 0, 0
    occupied = set([x + 0j for x in range(7)])
    num_rocks_todo = 1000000000000
    tracked_cycle = []
    # cache = 50
    height_offset = 0
    det_loop = False
    i = 0
    while i < num_rocks_todo:
        new_rock = get_rock(height, i)
        while True:
            # move
            new_rock_tmp = move_rock_left(new_rock) if data[moves] == -1 else move_rock_right(new_rock)
            if not new_rock_tmp & occupied:
                new_rock = new_rock_tmp
            moves = (moves + 1) % len(data)
            new_rock_tmp = move_rock_down(new_rock)
            if not new_rock_tmp & occupied:
                new_rock = new_rock_tmp
            else:
                occupied.update(new_rock)
                height = max(height, max([x.imag for x in list(new_rock)]))
                break
        i += 1
        if i == 2021:
            stop_time = time.time()
            print(f"pt1 solution: {height}  time: {stop_time - start_time}")
            tracked_cycle = [i % 5, moves, height, i]
        if i > 2021:
            if i % 5 == tracked_cycle[0] and moves == tracked_cycle[1] and not det_loop:
                # loop detected
                dh = height - tracked_cycle[2]
                di = i - tracked_cycle[3]
                num_future_cycles = math.floor((num_rocks_todo - i)/di)
                i += di*num_future_cycles
                height_offset = dh*num_future_cycles
                det_loop = True

    stop_time = time.time()
    print(f"pt2 solution: {height + height_offset} time overall: {stop_time - start_time}")