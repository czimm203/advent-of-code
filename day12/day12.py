#!/Library/Frameworks/Python.framework/Versions/3.11/bin/python3.11

from __future__ import annotations
import sys
from dataclasses import dataclass

# sys.setrecursionlimit(2000)

@dataclass
class Point:
    x: int
    y: int
    def hash(self):
        return f"{self.x},{self.y}"

@dataclass
class branch:
    u: Loc | None
    d: Loc | None
    l: Loc | None
    r: Loc | None

class Loc:
    def __init__(self, p: Point, val: str):
        self.point: Point = p
        self.value: str = val
        self.branches: branch = branch(None, None, None, None)
    
    def add_branches(self, grid: list[str]):
        x = self.point.x
        y = self.point.y
        u = Loc(Point(x,y-1),grid[y-1][x]) if y > 0 else None
        d = Loc(Point(x,y+1),grid[y+1][x]) if y < len(grid)-1 else None
        g = grid[y]
        l = Loc(Point(x-1,y),g[x-1]) if x > 0 else None
        r = Loc(Point(x+1,y),g[x+1]) if x < len(grid[0])-1 else None

        if u is not None and is_navigable(self.value, u.value):
            self.branches.u = u
        else:
            self.branches.u = None
        if d is not None and is_navigable(self.value, d.value):
            self.branches.d = d
        else:
            self.branches.d = None
        if l is not None and is_navigable(self.value, l.value):
            self.branches.l = l
        else:
            self.branches.l = None
        if r is not None and is_navigable(self.value, r.value):
            self.branches.r = r
        else:
            self.branches.r = None

    def find(self, dest: Loc, grid: list[str], visit: list[Point] = [], step = 0) -> int:
        visit.append(self.point)
        if self.point != dest.point:
            if self.branches.u is not None and self.branches.u.point not in visit:
                self.branches.u.add_branches(grid)
                return self.branches.u.find(dest, grid, visit, step+1)
            elif self.branches.l is not None and self.branches.l.point not in visit:
                self.branches.l.add_branches(grid)
                return self.branches.l.find(dest, grid, visit, step+1)
            elif self.branches.d is not None and self.branches.d.point not in visit:
                self.branches.d.add_branches(grid)
                return self.branches.d.find(dest, grid, visit, step+1)
            elif self.branches.r is not None and self.branches.r.point not in visit:
                self.branches.r.add_branches(grid)
                return self.branches.r.find(dest, grid, visit, step+1)
        return step

    def valid_steps(self) -> list[Loc]:
        locs = []
        if self.branches.u is not None:
            locs.append(self.branches.u)
        if self.branches.d is not None:
            locs.append(self.branches.d)
        if self.branches.l is not None:
            locs.append(self.branches.l)
        if self.branches.r is not None:
            locs.append(self.branches.r)
        return locs
        
    def hash(self):
        return f"{self.point.x},{self.point.y}"

class Graph:
    def __init__(self, grid: str):
        grid_str = grid.split("\n")
        self.grid: dict[str, Loc] = {}
        for y, j in enumerate(grid_str):
            for x, i in enumerate(j):
                p = Point(x,y)
                l = Loc(p,i)
                l.add_branches(grid_str)
                self.grid[l.hash()] = l 

    def shortest_path(self, start: Point, end: Point) -> int:
        s = self.grid[start.hash()]
        visited = set()
        count = 0
        visited.add(s.point.hash())

        while end.hash() not in visited and count < 500:
            tmp = set()
            for p in visited:
                for l in self.grid[p].valid_steps():
                    tmp.add(l.point.hash())
            if len(tmp) == 0:
                return 999
            for i in tmp:
                visited.add(i)
            count +=1
        #Need to clear the set so it doesn't affect next call
        visited.clear()
        return count

def is_navigable(cur: str, dest: str) -> bool:
    vc = ord(cur)
    vd = ord(dest)
    if cur == "S":
        vc = ord("a")
    if dest == "E":
        vd = ord("z")

    if vd - vc <=1:
        return True
    else:
        return False

def find_start(data: list[str])->Point:
    for i, line in enumerate(data):
        if "S" in line: return Point(line.find("S"), i)
    return Point(-1,-1)

def find_end(data: list[str])->Point:
    for i, line in enumerate(data):
        if "E" in line:
            return Point(line.find("E"), i)
    return Point(-1,-1)

def part1(data: str):
    grid = data.split("\n")
    graph = Graph(data)
    start = Loc(find_start(grid), "S")
    end = Loc(find_end(grid),"E")
    dist = graph.shortest_path(start.point, end.point)
    print(dist)

def part2(data: str):
    grid = data.split("\n")
    a = []
    graph = Graph(data)
    for k in graph.grid:
        if graph.grid[k].value == "a":
            a.append(k)
    m = 9999
    end = Loc(find_end(grid),"E")
    #This is a dumb way to do this. Should re-write the shortest_path algo to look for first value (i.e. "a")
    #then just start at the End and find the steps to the nearest "a"
    for i,k in enumerate(a):
        print(f"{i+1}/{len(a)}")
        dist = graph.shortest_path(graph.grid[k].point, end.point)
        if dist < m:
            m = dist
    print(m)

if __name__ == '__main__':
    with open('./test1.txt') as f:
        test = f.read().strip()
    with open('./input.txt') as f:
        input = f.read().strip()
    with open('./me.txt') as f:
        me = f.read().strip()

    part1(test)
    part1(input)
    part2(test)
    part2(input)
