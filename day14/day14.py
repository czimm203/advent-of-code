#!/Library/Frameworks/Python.framework/Versions/3.11/bin/python3.11

from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int
    material: str

class Cave:
    def __init__(self, data:str):
        self.walls = []
        lines = data.split("\n")
        for line in lines:
            ps = line.split(" -> ")
            for p in range(len(ps)-1):
                p0 = ps[p].split(',')
                p1 = ps[p+1].split(',')
                x0 = int(p0[0])
                x1 = int(p0[1])
                y0 = int(p1[0])
                y1 = int(p1[1])
                dx = x1 - x0
                dy = y1 - y0
                if dx != 0:
                    for i in range(dx):
                        self.walls.append(Point(x0+i,y0,"rock"))
                if dy != 0:
                    for i in range(dy):
                        self.walls.append(Point(x0,y0+i,"rock"))

if __name__ == '__main__':
    with open('./test1.txt') as f:
        test = f.read().strip()
    with open('./input.txt') as f:
        input = f.read().strip()

    c = Cave(test)
    print(c.walls)
