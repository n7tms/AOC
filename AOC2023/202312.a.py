import re
from functools import lru_cache
import os

non_dot_regex = re.compile('[^\.]')

# I abbreviated the variables as
# "spring_status" (ss) - the row
# "damage_runs" (dr) - the blocks


@lru_cache(maxsize=None)
def count(ss, dr):
    # if dr fully placed, this is valid iff no other certain '#' exist
    if not dr:
        return '#' not in ss
    # minimum space check
    elif sum(dr) + len(dr) - 1 > len(ss):
        return 0
    elif ss[0] == '#':
        # in order to fit this block
        # we must have no certain '.' in the first len(block) characters
        # then, if not the end of string, no certain '#' in the character after.
        if len(ss) >= dr[0] and '.' not in ss[: dr[0]] and (len(ss) == dr[0] or ss[dr[0]] != '#'):
            return count(ss[dr[0] + 1 :], dr[1:])
        # otherwise, impossible - can return 0 early
        else:
            return 0
    elif ss[0] == '.':
        # skip over as many certain '.' as possible
        if m := re.search(non_dot_regex, ss):
            return count(ss[m.start() :], dr)
        else:
            # end of string while still having dr
            return 0
    else:
        # cover both cases of what this '?' can be
        return count(ss[1:], dr) + count('#' + ss[1:], dr)

IN_FILE = os.path.join("AOC2023","inputs","202312.in")
with open(IN_FILE) as f:
    txt = f.read()

lines = txt.split('\n')


def parse_line(l, fold=1):
    ss, dr = l.split(' ')
    return '?'.join([ss] * fold), tuple(int(i) for i in (','.join([dr] * fold)).split(','))


print(sum(count(*parse_line(l)) for l in lines))
# out of curiosity
print(count.cache_info())

print(sum(count(*parse_line(l, 5)) for l in lines))
# out of curiosity
print(count.cache_info())
