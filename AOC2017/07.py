# AOC 2017 - Day 07
# tags: #graph #regex

import time
import re

# IN_File = "AOC2017/07.z.txt"
IN_File = "AOC2017/07.txt"

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

tree = list()

# def in_tree(node_name, tree):
def in_tree(node_name, t = tree):
    for x in t:
        if node_name == x.name:
            return x
    return None


def parse():
    """Parse input."""
    with open(IN_File) as f:
        out = f.read().split('\n')

    # tree = []
    for line in out:
        if '->' not in line:
            nw = re.search(r'(\w+) \((\d+)\)', line)
            name, weight = nw.group(1), int(nw.group(2))
            # print(name,weight)
            dNode = in_tree(name)
            if dNode:
                dNode.weight = weight
            else:
                tree.append(Node(name,weight))
        else:
            nwc = re.search(r'(\w+) \((\d+)\) -> (.*)', line)
            name,weight = nwc.group(1), int(nwc.group(2))
            children = nwc.group(3).split(', ')
            aNode = in_tree(name)
            if aNode:
                aNode.weight = weight
            else:
                aNode = Node(name,weight)
                tree.append(aNode)
            for c in children:
                child = in_tree(c)
                if child:
                    child.parent = aNode
                    aNode.add_child(child)
                else:
                    cNode = Node(c)
                    tree.append(cNode)
                    aNode.add_child(cNode)


def sum_of_branch(branch_node):
    total = branch_node.weight
    for child in branch_node.children:
        if len(child.children) == 0:
            total += child.weight
        else:
            total += sum_of_branch(child)
            # print(child.name,' - ',total)
    return total

def part1():    # hlqnsbe
    for node in tree:
        if node.parent is None:
            return node.name

def part2():    # 1993    (jriph (1998) -> cqrqt, kibpy)
    # I brute-forced this....seeing which branch did not balance
    # and widdling down the branch until I identified which node
    # was wrong. 
    # In my data, 'jriph' needs to be 5 units lighter, 1998 -> 1993.
    root_node = None
    for node in tree:
        if node.parent is None:
            root_node = node
    
    # root_node = in_tree('rilyl')
    # root_node = in_tree('aurik')
    # root_node = in_tree('jriph')

    for child in root_node.children:
        print(child.name,' - ',sum_of_branch(child))
    
    return 0

if __name__ == "__main__":
    timestart = time.time()

    parse()
    # print(data)


    print("part 1:",part1())
    print("part 2:",part2())
    
    timeend = time.time()
    print("Execution time: ", "{:.4f}".format(round(timeend-timestart,7)))