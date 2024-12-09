# Borrowed code from "https://github.com/vggm/Advent-of-Code/blob/main/2024/Day06/day06.py"

def read_file(filename: str) -> list[str]:
  with open(filename, "r") as rfile:
    lines = []
    
    line = rfile.readline().removesuffix("\n")
    while line != '':
      lines.append(line)
      line = rfile.readline().removesuffix("\n")
      
    return lines
  
WALL, GUARD, VOID = "#", "^", "."
DIR = [(-1, 0), (0, 1), (1, 0), (0, -1)]
#        UP      RIGHT   DOWN    LEFT

def get_guard_coords(maze: list[str]) -> tuple[int, int]:
  for i, row in enumerate(maze):
    for j, val in enumerate(row):
      if val == GUARD:
        return i, j  

  return -1, -1


def part_one(maze: list[str]) -> int:
  
  n, m = len(maze), len(maze[0])
  i, j = get_guard_coords(maze)
    
  seen = set() # to avoid count a cross twice use set
  curr_dir = 0
  di, dj = DIR[0]
  while 0 <= i < n and 0 <= j < m: # if False, found the escape
    seen.add((i, j))

    ni, nj = i + di, j + dj
    if not(0 <= ni < n and 0 <= nj < m): # found escape from the maze
      break
    
    # use while to avoid walk through the wall when there is
    # a wall at the right
    # 
    #    #      #      #
    #    ^# ->  ># ->  v#
    #
    while maze[ni][nj] == WALL:
      # using mod can make the process:
      # 0 1 2 3 0 1 2 3 ... up right down left up right down left ...
      curr_dir = (curr_dir + 1) % len(DIR)
      di, dj = DIR[curr_dir]
      ni, nj = i+di, j+dj
    
    i, j = ni, nj
      
  return len(seen)


def check_loop(curr_dir: int, obstacle: tuple[int, int], maze: list[str]) -> bool:
  n, m = len(maze), len(maze[0])
  
  oi, oj = obstacle
  di, dj = DIR[curr_dir]
  i, j = oi-di, oj-dj # previous position, where is the guard
  
  maze[oi][oj] = WALL # set the wall
  visited = set()
  
  while 0 <= i < n and 0 <= j < m:
    if (i, j, curr_dir) in visited: # loop found 
      maze[oi][oj] = VOID # remove the wall
      return True

    if maze[i][j] == WALL: # yapping
      print('o fac')
      
    visited.add((i, j, curr_dir)) # save all the states
    
    ni, nj = i+di, j+dj
    if not(0 <= ni < n and 0 <= nj < m):
      break 
    
    while maze[ni][nj] == WALL:
      curr_dir = (curr_dir + 1) % len(DIR)
      di, dj = DIR[curr_dir]
      ni, nj = i+di, j+dj
    
    i, j = ni, nj
  
  maze[oi][oj] = VOID # remove wall
  return False
    

def part_two(maze: list[str]) -> int:
  # in this case have to make the tuple as a list instead of str
  # because python doesnt allow str assigment: str are inmutable
  maze = list(map(lambda s: [x for x in s], maze))
  
  n, m = len(maze), len(maze[0])
  i, j = get_guard_coords(maze)
    
  curr_dir = 0
  di, dj = DIR[0]
  visited = set() # where the guard pass
  obstacles_that_make_loops = 0 # solution
  while 0 <= i < n and 0 <= j < m:
    visited.add((i, j))
    
    ni, nj = i + di, j + dj
    if not(0 <= ni < n and 0 <= nj < m): # end of path
      break
      
    # same method as before
    while maze[ni][nj] == WALL:
      curr_dir = (curr_dir + 1) % len(DIR)
      di, dj = DIR[curr_dir]
      ni, nj = i+di, j+dj
    
    # the wall cannot be set in a place where the guard has been
    #   he could notice it and we dont want that
    if (ni, nj) not in visited and check_loop(curr_dir, (ni, nj), maze):
      obstacles_that_make_loops += 1
    
    i, j = ni, nj
    
  return obstacles_that_make_loops


if __name__ == '__main__':
#   test = read_file("test.in")
  
#   sol = part_one(test)
#   assert sol == 41, f"Expected 41, but got {sol}."
  
  in1 = read_file("AOC2024/inputs/2024-06.in")
  print(f"Part One: {part_one(in1)}")
  
#   sol = part_two(test)
#   assert sol == 6, f"Expected 6, but got {sol}."
  
  print(f"Part Two: {part_two(in1)}")
  