#!/Library/Frameworks/Python.framework/Versions/3.11/bin/python3.11
from sys import getrefcount
from typing import Tuple


def get_prio(a: str) -> int:
    prio = ord(a)
    if prio >= 97:
        return prio-96
    else:
        return prio - 38

def unpack(line: str) -> Tuple[str,str]:
    line = line.strip()
    l = int(len(line)/2)
    packs = (line[:l],line[l:])
    return packs

def get_repeat(pack: Tuple[str,str]) -> str:
    for char1 in pack[0]:
        for char2 in pack[1]:
            if char1 == char2:
                return char1
    return ""

def part1(lines: list[str]) -> int:
    p1_score = 0
    for line in lines:
        pack = unpack(line)
        dupe = get_repeat(pack)
        p1_score += get_prio(dupe)
    return p1_score


def find_badge(group: list[str]) -> str:
    for char in group[0].strip():
        if char in group[1].strip() and char in group[2].strip():
            return char
    return ""
def part2(lines: list[str]) -> int:
    iters = int(len(lines)/3)

    score = 0
    for i in range(iters):
        group = [lines[3*i], lines[3*i+1], lines[3*i+2]]
        badge = find_badge(group)
        score += get_prio(badge)


    return score

if __name__ == "__main__":
    with open("./test1.txt") as f:
        test1 = f.readlines()
    with open("./input.txt") as f:
        p1 = f.readlines()

    test_score = part1(test1)
    print(test_score)

    p1_score = part1(p1)
    print(p1_score)

    with open("./test2.txt") as f:
        test2 = f.readlines()

    p2_test = part2(test2)
    p2_score = part2(p1)
    print(p2_test, p2_score)
