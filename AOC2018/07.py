# AOC 2018 day 07: 
#

import aoc_utils as aoc
import time
import os
# import re
import networkx as nx


DAY = '07'
IN_FILE = os.path.join("AOC2018","inputs","2018-"+str(DAY)+".in")
# IN_FILE = os.path.join("AOC2018","inputs","2018-"+str(DAY)+".sample.txt")

def parse(puzzle_input):
    """
    Parse
    """
    aoc.get_input(2018,DAY,False)

    with open(IN_FILE) as fp:
        data = fp.read().strip().splitlines()
    
    # instructions = [re.match(r"Step (.+) must be finished before step (.+) can begin.", line).groups() for line in data]

    # because each job is only one character, we can get a way with this simplier method and avoid regex
    instructions = [(line[5], line[36]) for line in data]
    return instructions


def fix(rules, pages):
    sorted = False
    while not sorted:
        sorted = True
        for f,s in rules:
            if f in pages and s in pages:
                idx_f = pages.index(f)
                idx_s = pages.index(s)
                if idx_f > idx_s:
                    pages[idx_f], pages[idx_s] = pages[idx_s], pages[idx_f]
                    sorted = False

    return pages


def part1(data):        # => EBICGKQOVMYZJAWRDPXFSUTNLH
    # the networkx module has a cool routine that does this exact thing!!
    graph = nx.DiGraph()
    graph.add_edges_from(data)
    order = list(nx.lexicographical_topological_sort(graph))

    return ''.join(order)


def part2(data, job_order):        # => 906
    # put the jobs in a "queue"
    # keep track of seconds (timer) (each job takes 60 + ord(job_letter))
    # if workers < 5, pop a job out of the queue onto workers
    # at each tick of the timer, decrement the duration on the worker jobs
    # if a job is complete (duration=0), put it in completed
    # see if the next job can start (if it's dependency are completed[])


    jobs = [j for j in job_order]
    workers = {}        # {job: duration}
    completed = []
    timer = 0

    while True:

        # search for completed jobs
        for k in list(workers.keys()):
            workers[k] -= 1
            if workers[k] == 0:
                completed.append(k)
                del workers[k]

        # add next job
        if len(workers) < 5:
            for job in list(jobs):
                # get a list of dependencies
                dp = [f for f,s in data if s==job]

                # see if all of the dependencies are already completed
                if all(e in completed for e in dp):
                    duration = ord(job) - ord("A") + 1 + 60
                    workers[job] = duration
                    jobs.remove(job)
                    if len(workers) >= 5: break
        
        # if there are no more workers, then we're done.
        if not workers:
            return timer
        else:
            timer += 1


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)

    start_time = time.time()
    p1 = str(part1(data))
    exec_time = time.time() - start_time
    print(f"part 1: {p1} ({exec_time:.4f} sec)")

    start_time = time.time()
    p2 = str(part2(data,p1))
    exec_time = time.time() - start_time
    print(f"part 2: {p2} ({exec_time:.4f} sec)")



if __name__ == "__main__":
    solve(IN_FILE)

