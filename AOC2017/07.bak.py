# AOC 2017 - Day 07
# tags: #graph #regex

import time
import re

IN_File = "AOC2017/07.z.txt"

class Node:
    def __init__(self, name, weight=0):
        self.name = name
        self.weight = weight
        self.parent = None
        self.children = []
        

    def __str__(self) -> str:
        return f"{self.name!s}"

    def add_child(self,child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            p = p.parent
            level += 1
        return level

    def print_tree(self):
        spaces = " " * self.get_level() * 3
        prefix = spaces + "|---" if self.parent else ''
        print(prefix + self.name)
        if self.children:
            for child in self.children:
                child.print_tree()

def in_tree(node, tree):
    for x in tree:
        if node.name == x.name:
            return x
    return None

def testing():
    tree = []
    a = Node('pbga',66)
    tree.append(a)

    if in_tree(a,tree):
        print('found')

    print(tree)

    x = 3


def parse():
    """Parse input."""
    with open(IN_File) as f:
        out = f.read().split('\n')

    tree = []
    for line in out:
        if '->' not in line:
            nw = re.search(r'(\w+) \((\d+)\)', line)
            name, weight = nw.group(1), nw.group(2)
            print(name,weight)
            tree.append(Node(name,weight))
        else:
            nwc = re.search(r'(\w+) \((\d+)\) -> (.*)', line)
            name,weight = nwc.group(1), nwc.group(2)
            children = nwc.group(3).split(', ')
            aNode = Node(name,weight)
            tree.append(aNode)
            for c in children:
                child = in_tree(Node(c),tree)
                if child:
                    child.parent = aNode
                    aNode.add_child(child)
                else:
                    cNode = Node(c)
                    tree.append(cNode)
                    aNode.add_child(cNode)
    
    for node in tree:
        if node.parent is None:
            print(node.name)

    return tree


def part1(data):    # 
    steps = 0
    return steps

def part2(data):    # 
    steps = 0
    return steps

if __name__ == "__main__":
    timestart = time.time()

    testing()

    data1 = parse()
    # print(data)
    data2 = data1.copy()

    print("part 1:",part1(data1))
    print("part 2:",part2(data2))
    
    timeend = time.time()
    print("Execution time: ", "{:.4f}".format(round(timeend-timestart,7)))