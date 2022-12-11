#!/Library/Frameworks/Python.framework/Versions/3.11/bin/python3.11

from types import EllipsisType


SCREEN = "\n".join("."*40 for _ in range(6))
class CRT:
    def __init__(self) -> None:
        self.reg = 1
        self.cycle = 1
        self.signals: list[int] = []
        self.screen = ""
        

    def parse_cmd(self, cmd: str):
        match cmd.split():
            case ["noop"]:
                self.signals.append(self.reg*self.cycle)
                self.update_screen()
                self.cycle += 1
            case ["addx", num]:
                i = int(num)
                self.signals.append(self.reg*self.cycle)
                self.update_screen()
                self.cycle += 1
                self.signals.append(self.reg*self.cycle)
                self.update_screen()
                self.cycle += 1
                self.reg += i

    def get_sprite(self) -> list[int]:
        return [self.reg-1, self.reg, self.reg+1]
    
    def update_screen(self):
        if (self.cycle-1)%40 in self.get_sprite():
            self.screen += "#"
        else:
            self.screen += "."

    def display(self):
        for i in range(len(self.screen)//40):
            print(self.screen[40*i: 40*i + 40])
        

def part1(data: str):
    crt = CRT()
    for cmd in data.split("\n"):
        crt.parse_cmd(cmd)
    print(sum(crt.signals[19::40]))
    crt.display()

if __name__ == '__main__':
    with open('./test1.txt') as f:
        test = f.read().strip()
    with open('./input.txt') as f:
        input = f.read().strip()

    part1(test)
    part1(input)
