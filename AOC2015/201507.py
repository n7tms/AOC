# AOC 2015 - Day 7

import time

IN_FILE = "AOC2015\\201507.txt"
# IN_FILE = "AOC2015\\201507.sample.txt"


# literal
# NOT literal
# a AND b
# a OR b
# a LSHIFT literal
# a RSHIFT literal

memory = {}

def parse():
    """Parse input."""
    # pi = [line for line in puzzle_input.split("\n")]
    with open(IN_FILE) as f:
        out = [(line) for line in f.read().split('\n')]
    return out

def parse_instruction(instruction):
    print(instruction)
    
# while None values exist
#   see if values in the operands (a,b) exist (a OP b -> c)
#   if both exist, execute the operation and store result in c
def execute(program):

    while len([k for (k,v) in memory.items() if v == None]) > 0 or len(memory) == 0:
        for instruction in program:
            instr, dst = [x.strip() for x in instruction.split('->')]
            instr2 = instr.split()

            # check if dst is in memory; if not, add it.
            if dst not in memory:
                memory[dst] = None

            # literal
            if len(instr2) == 1 and instr[0].isnumeric():
                memory[dst] = int(instr)

            # a
            elif len(instr2) == 1 and instr2[0] not in memory:
                break
            elif len(instr2) == 1 and instr2[0] in memory and memory[instr2[0]] is not None:
                memory[dst] = memory[instr2[0]]
            
                
            # NOT a
            elif instr2[0] == "NOT":
                if instr2[1] in memory and memory[instr2[1]] is not None:
                    memory[dst] = int(memory[instr2[1]]) ^ 65535
                    
            
            # a AND b
            elif instr2[1] == 'AND':
                if instr2[0].isnumeric() and instr2[2] in memory and memory[instr2[2]] is not None:
                    memory[dst] = int(instr2[0]) & memory[instr2[2]]
                elif instr2[0] in memory and instr2[2] in memory and memory[instr2[2]] is not None:
                    memory[dst] = memory[instr2[0]] & memory[instr2[2]]
            
            # a OR b
            elif instr2[1] == 'OR':
                if instr2[0] in memory and instr2[2] in memory:
                    if memory[instr2[0]] is not None and memory[instr2[2]] is not None:
                        memory[dst] = memory[instr2[0]] | memory[instr2[2]]

            # a LSHIFT literal
            elif instr2[1] == 'LSHIFT':
                if instr2[0] in memory and memory[instr2[0]] is not None:
                    memory[dst] = memory[instr2[0]] << int(instr2[2])

            # a RSHIFT literal
            elif instr2[1] == 'RSHIFT':
                if instr2[0] in memory and memory[instr2[0]] is not None:
                    memory[dst] = memory[instr2[0]] >> int(instr2[2])

    return memory['a'] 


def part1(data):            # => 
    """Solve part 1."""
    return execute(data)


def part2(data):            # => 
    """Solve part 2."""
    

if __name__ == "__main__":
    timestart = time.time()
    
    puzzle_input = parse()
    # print(puzzle_input)
    print("part 1:",part1(puzzle_input))
    print("part 2:",part2(puzzle_input))
    
    timeend = time.time()
    print("Execution time: ", "{:.7f}".format(round(timeend-timestart,7)))
