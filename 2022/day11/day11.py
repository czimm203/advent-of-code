#!/Library/Frameworks/Python.framework/Versions/3.11/bin/python3.11

from collections import namedtuple, deque

Targets = namedtuple("Targets", ["success", "fail"])

class Monkey:
    def __init__(self, name: str, items: deque, op: str, test: int, targets: Targets):
        self.name = name
        self.items = items
        self.op = op
        self.test = test
        self.targets = targets
        self.count = 0

    def toss_item(self) -> tuple[str, int]:
        self.count += 1
        item = self.items.popleft()
        match self.op.split(" "):
            case ["*", "old"]:
                item *= item
            case ["+", "old"]:
                item += item
            case ["+", num]:
                item += int(num)
            case ["*", num]:
                item *= int(num)
            case _:
                raise ValueError
        item = item // 3
        if item % self.test == 0:
            target = self.targets[0]
        else:
            target = self.targets[1]
        return (target, item)
    
    def toss_item2(self, lcm: int) -> tuple[str, int]:
        self.count += 1
        item = self.items.popleft()
        match self.op.split(" "):
            case ["*", "old"]:
                item *= item
            case ["+", "old"]:
                item += item
            case ["+", num]:
                item += int(num)
            case ["*", num]:
                item *= int(num)
            case _:
                raise ValueError
        item %= lcm
        if item % self.test == 0:
            target = self.targets[0]
        else:
            target = self.targets[1]
        return (target, item)

class Game:
    def __init__(self):
        self.monkies: dict[str, Monkey] = {}

    def add_monkey(self, monkey: Monkey):
        self.monkies[monkey.name] = monkey

    def play_round(self):
        for monkey in self.monkies:
            mnky = self.monkies[monkey]
            for x in range(len(mnky.items)):
                if len(mnky.items) == 0:
                    continue
                target, loot = mnky.toss_item()
                self.monkies[target].items.append(loot)
    def play_round2(self, lcm: int):
        for monkey in self.monkies:
            mnky = self.monkies[monkey]
            for _ in range(len(mnky.items)):
                if len(mnky.items) == 0:
                    continue
                target, loot = mnky.toss_item2(lcm)
                self.monkies[target].items.append(loot)
            
                

def parse_monkey(data: str) -> Monkey:
# Monkey 0:
#   Starting items: 79, 98
#   Operation: new = old * 19
#   Test: divisible by 23
#     If true: throw to monkey 2
#     If false: throw to monkey 3
    lines = data.split("\n")
    name = lines[0].strip().lower()[:-1]
    items = lines[1].strip().split(": ")[1].split(", ")
    op = lines[2].split("old ")[1]
    test = int(lines[3].split("by ")[1])
    if len(items) >0:
        items = deque(map(int,items))
    else:
        items = deque([])
    p = lines[4].split("to ")[1]
    f = lines[5].split("to ")[1]

    return Monkey(name, items, op, test, Targets(p,f))

def part1(data:str):
    game = Game()
    monkey_bidness = data.split("\n\n")
    for m in monkey_bidness:
        mnky = parse_monkey(m)
        game.add_monkey(mnky)

    for _ in range(20):
        game.play_round()

    counts = [game.monkies[m].count for m in game.monkies]
    counts.sort()
    print(counts[-1]*counts[-2])

def part2(data:str):
    game = Game()
    monkey_bidness = data.split("\n\n")
    lcm = 1
    for m in monkey_bidness:
        mnky = parse_monkey(m)
        game.add_monkey(mnky)
        lcm *= mnky.test

    for _ in range(10000):
        game.play_round2(lcm)

    counts = [game.monkies[m].count for m in game.monkies]
    counts.sort()
    print(counts)
    print(counts[-1]*counts[-2])

if __name__ == '__main__':
    with open('./test1.txt') as f:
        test = f.read().strip()
    with open('./input.txt') as f:
        input = f.read().strip()

    part1(test)
    part1(input)

    part2(test)
    part2(input)
