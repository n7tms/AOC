# https://github.com/b-locke/aoc-23/blob/cd6032f196830b137c5f7bf760c15184d6918b7c/day-5-pt-2.py
# courtesy of b-locke

import pathlib
from functools import reduce


with open("AOC2023/inputs/202305.in") as fp:
    out = []
    puzzle_input = fp.read().split("\n\n")
# puzzle_input = pathlib.Path('/Users/benjamin/Documents/GitHub/aoc-23/day-5-input-1.txt').read_text().split('\n\n')
puzzle_input = [line.split('\n') for line in puzzle_input]

def seed_locations(puzzle_input):
	seed_list = [int(seed) for seed in puzzle_input[0][0].split(':')[1].split()]
	seeds = [[seed_list[a], seed_list[a] + seed_list[a+1]-1] for a in range(0, len(seed_list), 2)]
	maps = puzzle_input[1:]
	for m in maps:
		i = 0
		while i < len(seeds):
			f = False
			seed_start, seed_end = seeds[i]
			for line in m[1:]:
				d, s, r = [int(x) for x in line.split()]
				if seed_start >= s and seed_start < (s + r) and f == False:
					f = True
					seeds[i][0] = d + (seed_start - s)
					if seed_end < s + r:
						seeds[i][1] = d + (seed_end - s)
					else:
						seeds[i][1] = d + r - 1
						seeds.append([s + r, seed_end])
						
				elif seed_end >= s and seed_end < (s + r) and f == False:
					f = True
					seeds[i][1] = d + (seed_end - s)
					if seed_start > s:
						seeds[i][0] = d + (seed_start - s)
					else:	
						seeds[i][0] = d
						seeds.append([seed_start, s-1])
			i += 1
	return min(min(s) for s in seeds)
	
output = seed_locations(puzzle_input)
print(output)