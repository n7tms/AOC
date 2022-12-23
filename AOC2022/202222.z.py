# AOC 2022 - Day 22 (Part 2)
# @Tarlitz
# https://topaz.github.io/paste/#XQAAAQCAFwAAAAAAAAA0m0pnuFI8c/T1e0vJBsZpxjrRd3JBPSVmAqTNApA8XmmduHwjYFRcer3jQ+qzy9D2shvKmwTZ8LrK24/W2kqVB+E0h5ETsy+mP+CdoyVsM+qizUdzski4bfEH/ZLEa0uaC+UqrET8EUIZIOnviJjhEMB6TDhOB6gAbsRVQLPWaI9+yKK27NhxRwPDqS1raHGSBeD8PdJIi491GE9ywbDYJ4sCQs/I1/O+h0sABbmieHmSMGnLHb/tUqBKjgIz4IOhJW9ITA6chs5O+OAPeyLNANyMVi4/Bro2ZiztFUL12f4UQciKk7oU29OM/6nUTR7GTLd6fr+aoEl/UtZPNJDIYlpjmPOjNevHLlKAVpnv45wbMiN0Hf7bDbKOgpf8ZfrqAEPhFi1o2Rh8mqaho3BtjgwfaQiK2heqjDG/vyyHLjJoyjitlpeS/in2eY1oCbOuCflc+ELkNSd1U+L9yZLyA6X+GN6fwDx9clf0JZKPu5y1u9JkrF1++UgsHl97/iHQ/ZRx6vCRgMklZqVxqgyIVqN6n7Y2NF6PDLqiDQQxkPRyyuc7/bpBvCkdLtqYCtaIOkBjOR6HbdUi8aPdXvn5gG5ysgJwjXyjICJd2kPX9INC2SgzhQlOZLfXPdsC8spW5RWQ/BjG8L/7TkcdAkt5NJfqdT75E2HD7OuS/muijGOM7PlG6/Q07LmWfkaT5L5q3ynpKHL4KiHs4PV2JnbE2BTAc37hiRUtqY/aLnuJNDtD3gI0fRNf1m9uM5JbIaiWISzUWfFgkrJHjlILaIRQ8l7IIfp6gnrm1tVimF9WWehpRCeoP27P2mnxvZokVVMpew4BtaFo72wGAOaLNCa1dBPubcaKz/bFpGHog4WB77m/iIb3RQt6t2ee91JEesB30u9JlKfuQ3nwUYEIsTa2BJzPZwN51lQrDU1AXGekDmGfjN471QRj2Fy9AOBC0T4pnVL0E8hhf5zIQzJpBHEyOO2bcsbq8Q3M7ABbqWtCedj36MHj9HKWYFLzOHVe7b1pJs6HSVaIe+VxDVBEk5gZUNv/uRWt+OBGHZgdIDz6vIKLpXAzMf1ou3mkcrCRKAGWzblBdG/K5tpbDmlG+raPsRi6QXihuxvgT/7mshhdMiiclnPRJ+IkBa7v9NiCkKlbpmjJryY/UsjL/AJLmtxMqbON/N/qXVQTUGMKUYz+8wGTItvrnKZnfXzM99cx7WOpbwzlYPLQ0zUb0acWgfZ7iAuBPTfSvPIU2nH+S3IiM0e3qT9rSy8HM+Vw9JcJHdntxyvlgbsphjxnEsknNHARpN4xxJZUjvv8I7CSkHTlXmjZZRt7zJ6mR+Bp4QgduvuwIsWllNMQ9fs+YZ8ixfU0dNbdIduNuj/UD8jMRugctYOCXIqKpVr+RMRK4nR/bhZyMPKRlhRQfsURbXnS1ulN9T/8Z3QX0LuAS2g660M/jO7/lpKgwsjx7tAuNqpa8HtLhsnPxB73O6ddC9+vn8QW+jqJyO7uUA/26wyzo510vL4e6gK0eA+GjRvD2p7lXuqy+VJSUKeyCecofPPLS4yo5YRtlHje2GvEyjuAdpA/hGIBE1uXzCDW5TwhCq/C3/fLvD9cVMfCu3+PsnJYQSMjPoPlGPU4Mt1oL9Qd6n9FSCi5UmyRu/NsmitBNoWGhyOs8lzKCcvClv5HHw/NDV5prm0aJLBNKykUZEDm6h4o3edhZ/pmaRMtPJXbPSMxpuNkvOVNBJJHbWYlIfRZcAxkOTu8EB9zB+N2wCFcIyYQPFbtgZLqjIr+nSj/8a/fB36jnIYPiPFu20+62xWsXJB8Sf+5N9C4

import re
from pathlib import Path

import numpy as np


MOVE_PAT = re.compile(r'\d+|[A-Z]')


def parse_board(lines):
    rows = []
    lines = lines.split('\n')

    max_length = max(len(line) for line in lines)

    for line in lines:
        row = [' .#'.index(c) for c in line]
        row.extend([0 for _ in range(max_length - len(row))])
        rows.append(row)

    return np.array(rows)


def parse_route(line):
    line = line.strip()

    route = []

    for step in MOVE_PAT.findall(line):
        try:
            step = int(step)
            route.append(('move', int(step)))
        except ValueError:
            route.append(('turn', step))

    return route


def part2(s: str):
    board_lines, route_line = s.split('\n\n')

    full_board = parse_board(board_lines)
    route = parse_route(route_line)

    ln = 50
    origins = {
        'top': (0 * ln, 1 * ln),
        'right': (0 * ln, 2 * ln),

        'front': (1 * ln, 1 * ln),

        'left': (2 * ln, 0 * ln),
        'bot': (2 * ln, 1 * ln),

        'back': (3 * ln, 0 * ln),
    }

    subboards = {key: full_board[ro:ro + ln, co:co + ln] for key, (ro, co) in origins.items()}

    right = (0, 1)
    down = (1, 0)
    left = (0, -1)
    up = (-1, 0)

    facings = (right, down, left, up)

    def rotate_right(facing):
        i = facings.index(facing)
        return facings[(i + 1) % 4]

    def rotate_left(facing):
        i = facings.index(facing)
        return facings[(i - 1) % 4]

    def teleport(pos, facing, side):
        r, c = pos

        if (side, facing) == ('top', up):
            new_side, new_facing = 'back', right
            r = c
            c = 0

        elif (side, facing) == ('top', down):
            new_side, new_facing = 'front', down
            r = 0

        elif (side, facing) == ('top', left):
            new_side, new_facing = 'left', right
            r = ln - 1 - r

        elif (side, facing) == ('top', right):
            new_side, new_facing = 'right', right
            c = 0

        elif (side, facing) == ('bot', up):
            new_side, new_facing = 'front', up
            r = ln - 1

        elif (side, facing) == ('bot', down):
            new_side, new_facing = 'back', left
            r = c
            c = ln - 1

        elif (side, facing) == ('bot', left):
            new_side, new_facing = 'left', left
            c = ln - 1

        elif (side, facing) == ('bot', right):
            new_side, new_facing = 'right', left
            r = ln - 1 - r

        elif (side, facing) == ('left', up):
            new_side, new_facing = 'front', right
            r = c
            c = 0

        elif (side, facing) == ('left', down):
            new_side, new_facing = 'back', down
            r = 0

        elif (side, facing) == ('left', left):
            new_side, new_facing = 'top', right
            r = ln - 1 - r

        elif (side, facing) == ('left', right):
            new_side, new_facing = 'bot', right
            c = 0

        elif (side, facing) == ('right', up):
            new_side, new_facing = 'back', up
            r = ln - 1

        elif (side, facing) == ('right', down):
            new_side, new_facing = 'front', left
            r = c
            c = ln - 1

        elif (side, facing) == ('right', left):
            new_side, new_facing = 'top', left
            c = ln - 1

        elif (side, facing) == ('right', right):
            new_side, new_facing = 'bot', left
            r = ln - 1 - r

        elif (side, facing) == ('front', up):
            new_side, new_facing = 'top', up
            r = ln - 1

        elif (side, facing) == ('front', down):
            new_side, new_facing = 'bot', down
            r = 0

        elif (side, facing) == ('front', left):
            new_side, new_facing = 'left', down
            c = r
            r = 0

        elif (side, facing) == ('front', right):
            new_side, new_facing = 'right', up
            c = r
            r = ln - 1

        elif (side, facing) == ('back', up):
            new_side, new_facing = 'left', up
            r = ln - 1

        elif (side, facing) == ('back', down):
            new_side, new_facing = 'right', down
            r = 0

        elif (side, facing) == ('back', left):
            new_side, new_facing = 'top', down
            c = r
            r = 0

        elif (side, facing) == ('back', right):
            new_side, new_facing = 'bot', up
            c = r
            r = ln - 1

        new_pos = (r, c)

        return new_pos, new_facing, new_side

    def find_new_pos(pos, facing, side, *, max_n):
        accepted = (pos, facing, side)
        board = subboards[side]

        for n in range(max_n):
            dr, dc = facing
            r, c = pos
            new_side = side

            tr = r + dr
            tc = c + dc

            if tr in (-1, ln) or tc in (-1, ln):
                (tr, tc), (dr, dc), new_side = teleport((r, c), (dr, dc), side)
                board = subboards[new_side]

            if board[tr, tc] == 1:  # open
                pos = (tr, tc)
                facing = (dr, dc)
                side = new_side

                accepted = (pos, facing, side)

            elif board[tr, tc] == 2:  # rock
                break

            elif board[tr, tc] == 0:
                raise ValueError('This should no longer happen')

        return accepted

    side = 'top'
    pos = 0, 0
    facing = facings[0]

    for i, instruction in enumerate(route):
        match instruction:
            case 'move', n:
                (pos, facing, side) = find_new_pos(pos, facing, side, max_n=n)
            case 'turn', 'L':
                facing = rotate_left(facing)
            case 'turn', 'R':
                facing = rotate_right(facing)

    ro, rc = origins[side]
    r, c = pos

    return 1000 * (ro + r + 1) + 4 * (rc + c + 1) + facings.index(facing)


if __name__ == '__main__':
    with open('AOC2022\\inputs\\202222.txt') as f:
        DATA = f.read()
    # DATA = Path(__file__).with_name('AOC2022\\inputs\\202222.txt').read_text()

    print(part2(DATA))
