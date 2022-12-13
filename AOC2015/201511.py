# AOC 2015 - Day 11

import time

input = "hxbxwxba"

def str_to_list(data):
    tmp_list = [x for x in data]
    return tmp_list


def meets_rules(pwd):
    crit1 = False
    crit2 = False
    crit3 = False

    # increasing straight of three consecutive letters (e.g. 'abc', 'pqr', etc.)
    for i in range(len(pwd)-2):
        tmp = ord(pwd[i])
        if "".join(pwd[i:i+3]) == "".join([chr(tmp),chr(tmp+1),chr(tmp+2)]):
            crit1 = True
            break

    # does not contain 'i', 'o', or 'l'
    if 'i' not in pwd and 'o' not in pwd and 'l' not in pwd:
        crit2 = True

    # two different, non-overlapping pairs of letters (e.g. 'aagg', 'ttqq', etc.)
    cnt = 0
    i = 0
    while i < len(pwd)-1:
        if pwd[i] == pwd[i+1]:
            cnt += 1
            i += 1
        i += 1
    if cnt > 1:
        crit3 = True

    return crit1 & crit2 & crit3

def inc_pwd(pwd):
    pwd_rev = list(reversed(pwd))
    for i in range(len(pwd_rev)-1):
        tmp_let = ord(pwd_rev[i]) + 1
        if tmp_let == 105 or tmp_let == 111 or tmp_let == 108:
            pwd_rev[i] = chr(tmp_let+1)
            break
        if  tmp_let > 122:
            pwd_rev[i] = 'a'
        else:
            pwd_rev[i] = chr(tmp_let)
            break
    return list(reversed(pwd_rev))


def part1(data):            # => hxbxxyzz
    """Solve part 1."""
    new_pwd = inc_pwd(data)
    while not meets_rules(new_pwd):
        new_pwd = inc_pwd(new_pwd)
    return "".join(new_pwd)

def part2(data):            # => hxcaabcc
    """Solve part 2."""
    new_pwd = inc_pwd(data)
    while not meets_rules(new_pwd):
        new_pwd = inc_pwd(new_pwd)
    return "".join(new_pwd)


if __name__ == "__main__":
    timestart = time.time()

    in2 = str_to_list(input)
    new_password = part1(in2)
    print("part 1:",new_password)

    new_password = part2(new_password)
    print("part 2:",new_password)
    
    timeend = time.time()
    print("Execution time: ", f"{timeend-timestart:0.4f}")

