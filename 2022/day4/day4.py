#!/Library/Frameworks/Python.framework/Versions/3.11/bin/python3.11
from typing import Tuple

def parse_line(line: str) -> Tuple[set,set]:
    pairs = line.replace(',','-').split('-')
    first = (int(pairs[0]),int(pairs[1]))
    second = (int(pairs[2]),int(pairs[3]))
    p1 = set(range(first[0],first[1]+1))
    p2 = set(range(second[0],second[1]+1))
    return (p1, p2)

def nested(pairs: Tuple[set,set]) -> bool:
    if pairs[0].issubset(pairs[1]) or pairs[1].issubset(pairs[0]):
        return True
    else:
        return False

def overlaps(pairs: Tuple[set,set]) -> bool:
    p1 = pairs[0]
    p2 = pairs[1]
    if len(p1.intersection(p2)) > 0:#len(p1):
        return True
    else:
        return False

def part1(lines: list[str]):
    total = 0
    for line in lines:
        pairs = parse_line(line)
        if nested(pairs):
            total += 1
    return total

def part2(lines: list[str]):
    total = 0
    for line in lines:
        pairs = parse_line(line)
        if overlaps(pairs):
            total += 1
    return total


if __name__ == "__main__":
    with open("./test1.txt") as f:
        test = f.readlines()
    with open("./input.txt") as f:
        input = f.readlines()


    print(part1(test))
    print(part1(input))
    print(part2(test))
    print(part2(input))



