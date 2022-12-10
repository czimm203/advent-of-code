#!/Library/Frameworks/Python.framework/Versions/3.11/bin/python3.11

class Grid:
    def __init__(self, data:str):
        self.grid = get_grid(data)
        self.r = len(self.grid[0])
        self.c = len(self.grid[:][0])
        self.local_maxes = []
        self.get_local_maxes()

    def get_local_maxes(self):
        for i in range(self.r):
            idx = get_lines_of_sight(self.grid[i])
            for id in idx:
                if (i,id) not in self.local_maxes:
                    self.local_maxes.append((i,id))
        for i in range(self.c):
            line = [line[i] for line in self.grid]
            idx = get_lines_of_sight(line)
            for id in idx:
                if (id,i) not in self.local_maxes:
                    self.local_maxes.append((id,i))

    def find_high_score(self) -> int:
        high = 0
        for pt in self.local_maxes:
            score = self.get_scenic_score(pt)
            if score > high:
                high = score
        return high

    def get_scenic_score(self, pt) -> int:
        x,y = pt
        if x < 1 or y < 1 or x >= self.c - 1 or y >= self.r - 1:
            return 0 
        left = 1
        right = 1
        up = 1
        down = 1

        idx = x - 1
        while idx > 0 and self.grid[x][y] > self.grid[idx][y]:
            left += 1
            idx -= 1
        idx = x + 1
        while idx < self.c -1 and self.grid[x][y] > self.grid[idx][y]:
            right += 1
            idx += 1
        idx = y - 1
        while idx > 0 and self.grid[x][y] > self.grid[x][idx]:
            up += 1
            idx -= 1
        idx = y + 1
        while  idx < self.r - 1 and self.grid[x][y] > self.grid[x][idx]:
            down += 1
            idx += 1

        return left*right*up*down
        

def get_grid(data: str) -> list[list[int]]:
    rows = data.split("\n")
    lines = []
    for row in rows:
        chars = [char for char in row]
        lines.append(list(map(int,chars)))
    return lines

def get_lines_of_sight(line: list[int]) -> list[int]:
    l = len(line)
    points = []
    for i in range(l-2):
        x = i+1
        val = line[x]
        if val > max(line[x+1:]) or val > max(line[:x]):
            points.append(x)
    points.append(0)
    points.append(l-1)
    return points

def part1(data: str):
    grid = Grid(data)
    count = len(grid.local_maxes)
    print(count)
    print(grid.find_high_score())

if __name__ == '__main__':
    with open('./test1.txt') as f:
        test = f.read().strip()
    with open('./input.txt') as f:
        input = f.read().strip()

    part1(test)
    part1(input)

