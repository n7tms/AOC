# Algorithms for path finding
# adopted and adapted from redblobgames.com
from implementation import *

diagram4 = GridWithWeights(10, 10)
# diagram4.walls = [(1, 7), (1, 8), (2, 7), (2, 8), (3, 7), (3, 8)]
# diagram4.weights = {loc: 5 for loc in [(3, 4), (3, 5), (4, 1), (4, 2),
#                                        (4, 3), (4, 4), (4, 5), (4, 6),
#                                        (4, 7), (4, 8), (5, 1), (5, 2),
#                                        (5, 3), (5, 4), (5, 5), (5, 6),
#                                        (5, 7), (5, 8), (6, 2), (6, 3),
#                                        (6, 4), (6, 5), (6, 6), (6, 7),
#                                        (7, 3), (7, 4), (7, 5)]}
diagram4.weights = {loc: 5 for loc in [(1,5),(2,4),0,4]}

start, goal = (1,4),(8,9)
came_from, cost_so_far = a_star_search(diagram4, start, goal)
draw_grid(diagram4, point_to=came_from,start=start, goal=goal)
print()
draw_grid(diagram4, path=reconstruct_path(came_from,start=start,goal=goal))
print("Cost: ",cost_so_far[goal])