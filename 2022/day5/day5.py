#!/Library/Frameworks/Python.framework/Versions/3.11/bin/python3.11

from collections import deque, namedtuple
import re

Instruction = namedtuple("Instruction",["num", "stack", "dest"])

def parse(data: str) -> None:
    stacks = get_stacks(data)
    ins = get_instructions(data)
    for i in ins:
        move_crate(i, stacks)

    ans = ""
    for i in stacks:
        ans += i[0]
    print(ans)

def parse2(data: str) -> None:
    stacks = get_stacks(data)
    ins = get_instructions(data)
    for i in ins:
        move_crate2(i, stacks)

    ans = ""
    for i in stacks:
        if len(i) != 0:
            ans += i[0]
    print(ans)

def get_stacks(data: str) -> list[deque]:
    lines = data.split('\n\n')[0].split("\n")
    num_cols = len(lines[-1].replace(" ",""))
    stacks: list[deque] = []
    for _ in range(num_cols):
        stacks.append(deque())
        
    for line in lines[:-1]:
        for i in range(num_cols):
            char = line[i*4+1]
            if char != " ":
                stacks[i].append(line[i*4+1])
    return stacks

def get_instructions(data:str) -> list[Instruction]:
    inst: list[Instruction] = []
    lines = data.split("\n\n")[1].split('\n')
    for line in lines:
        if line.strip() != "":
            nums = re.findall(r"[0-9]?[0-9]",line)
            nums = list(map(int,nums))
            inst.append(Instruction(*nums))
    return inst
        
def move_crate(ins: Instruction, stack: list[deque]):
    for _ in range(ins.num):
        crate = stack[ins.stack-1].popleft()
        stack[ins.dest-1].appendleft(crate)

def move_crate2(ins: Instruction, stack: list[deque]):
    acc = []
    s = stack[ins.stack-1]
    d = stack[ins.dest-1]
    for _ in range(ins.num):
        c = s.popleft()
        acc.append(c)

    acc.reverse()
    for item in acc:
        d.appendleft(item)
        

if __name__ == "__main__":
    with open("test1.txt") as f:
        test = f.read()

    with open("./input.txt") as f:
        input = f.read()
    parse(test)
    parse(input)
    parse2(test)
    parse2(input)
