#!/Library/Frameworks/Python.framework/Versions/3.11/bin/python3.11
from typing import Callable


with open("./input.txt") as f:
    lines = f.readlines()


def part1(data: list[str], fn: Callable):
    elf_load: list[int] = []
    total_calories = 0
    for line in data:
        if line == "\n":
            elf_load.append(total_calories)
            total_calories = 0
        else:
            total_calories += int(line)
    return fn(elf_load)

def part2fn(l: list[int]) -> int:
    s = sorted(l)
    return sum(s[-3:])

if __name__ == "__main__":
    print(part1(lines, part2fn))
