#!/Library/Frameworks/Python.framework/Versions/3.11/bin/python3.11

WIDTH = 30000
HEIGHT = 600

class Point:
    def __init__(self, pair: str):
        x,y = pair.split(',')
        self.x = int(x)
        self.y = int(y)

class Cave:
    def __init__(self):
        self.buf = [[0]*WIDTH for _ in range(HEIGHT)]
        self.max_y = 0
        self.max_x = 0
        self.min_y = HEIGHT
        self.min_x = WIDTH
        self.sand_total = 0
        self.full = False

    def add_wall(self, p1: Point, p2: Point):
        dx = p2.x - p1.x
        dy = p2.y - p1.y

        if dx == 0:
            for i in range(min(p1.y, p2.y),max(p1.y, p2.y)+1):
                self.buf[i][p1.x] = 3
            self.max_y = (max(self.max_y, max(p1.y, p2.y)))
            self.min_y = (min(self.min_y, min(p1.y, p2.y)))
        elif dy == 0:
            for i in range(min(p1.x, p2.x),max(p1.x, p2.x)):
                self.buf[p1.y][i] = 3

            self.max_x = (max(self.max_x, max(p1.x, p2.x)))
            self.min_x = (min(self.min_x, min(p1.x, p2.x)))


    def add_floor(self):
        self.buf[self.max_y +2] = [3]*WIDTH

    def add_sand(self):
        self.sand_total += 1
        can_move = True
        sand = [500, 0]

        max_iter = 10000
        i = 0
        
        while(can_move):
            if sand[1]+1 >= HEIGHT:
                print("full")
                can_move = False
                self.full = True

            elif sand[1] + 1 < HEIGHT and self.buf[sand[1]+1][sand[0]] == 0:
                sand[1] += 1

            elif sand[0] - 1 >= 0 and self.buf[sand[1]+1][sand[0]-1] == 0:
                sand[0] -= 1
                sand[1] += 1

            elif sand[0] + 1 < WIDTH and self.buf[sand[1]+1][sand[0]+1] == 0:
                sand[0] += 1
                sand[1] += 1
            elif sand != [500,0]:
                self.buf[sand[1]][sand[0]] = 1
                can_move = False
            else:
                can_move = False
                self.full = True


if __name__ == '__main__':
    with open('./test1.txt') as f:
        test = f.read().strip()
    with open('./input.txt') as f:
        input = f.read().strip()

    c = Cave()

    lines = test.split("\n")
    for line in lines:
        pts = line.split(" -> ")
        for i in range(len(pts) - 1):
            p1 = Point(pts[i])
            p2 = Point(pts[i+1])
            c.add_wall(p1, p2)
    c.add_floor()

    while(not c.full):
        c.add_sand()
    # for line in c.buf[:c.max_y+2]:
    #     print(line[:c.max_x + 500])
    print(c.sand_total)

    c = Cave()

    lines = input.split("\n")
    for line in lines:
        pts = line.split(" -> ")
        for i in range(len(pts) - 1):
            p1 = Point(pts[i])
            p2 = Point(pts[i+1])
            c.add_wall(p1, p2)
    c.add_floor()

    while(not c.full):
        c.add_sand()
    # for line in c.buf[:c.max_y+2]:
    #     print(line[:c.max_x + 500])
    print(c.sand_total)
