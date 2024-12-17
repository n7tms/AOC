import heapq
import aoc_utils as aoc
import os

# Define directions: (dx, dy) corresponds to North, East, South, West
DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # N, E, S, W
# IN_FILE = os.path.join("AOC2024","inputs","2024-"+str(16)+".sample.txt")
IN_FILE = os.path.join("AOC2024","inputs","2024-"+str(16)+".in")

def parse_maze():
    aoc.get_input(2024,16,False)

    with open(IN_FILE) as fp:
        data = fp.read()
    maze = [list(line) for line in data.strip().split("\n")]
    start, end = None, None
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if cell == 'S':
                start = (x, y)
            elif cell == 'E':
                end = (x, y)
    return maze, start, end

def heuristic(pos, end):
    return abs(pos[0] - end[0]) + abs(pos[1] - end[1])

def find_min_score():
    maze, start, end = parse_maze()
    start_state = (0, start[0], start[1], 1)  # (score, x, y, direction)
    pq = [start_state]
    visited = set()
    
    while pq:
        score, x, y, direction = heapq.heappop(pq)
        if (x, y, direction) in visited:
            continue
        visited.add((x, y, direction))
        
        # Check if we reached the end
        if (x, y) == end:
            return score
        
        # Try moving forward
        nx, ny = x + DIRECTIONS[direction][0], y + DIRECTIONS[direction][1]
        if maze[ny][nx] != '#':  # Open tile
            heapq.heappush(pq, (score + 1, nx, ny, direction))
        
        # Try rotating clockwise
        heapq.heappush(pq, (score + 1000, x, y, (direction + 1) % 4))
        
        # Try rotating counterclockwise
        heapq.heappush(pq, (score + 1000, x, y, (direction - 1) % 4))

print(find_min_score()) 