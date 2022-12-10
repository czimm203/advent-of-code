#!/Library/Frameworks/Python.framework/Versions/3.11/bin/python3.11

from __future__ import annotations
from dataclasses import dataclass, field
from pprint import pprint
from typing import Optional

@dataclass
class Knot:
    x:int
    y:int
    next: Optional[Knot] = None
    path: list[tuple[int,int]] = field(default_factory=list) 

    def __post_init__(self):
        if self.next == None:
            self.next = self

    def __add__(self, p: Knot):
        return Knot(self.x + p.x, self.y + p.y,self.next,self.path)

    def __sub__(self, p: Knot):
        return Knot(self.x - p.x, self.y - p.y,self.next,self.path)
        
    def move(self, cmd:str):
        match cmd.split(" "):
            case ["U", num]:
                for _ in range(int(num)):
                    self.y += 1
                    self._update_next()
                    self.update_path()
            case ["D", num]:
                for _ in range(int(num)):
                    self.y -= 1
                    self._update_next()
                    self.update_path()
            case ["L", num]:
                for _ in range(int(num)):
                    self.x -= 1
                    self._update_next()
                    self.update_path()
            case ["R", num]:
                for _ in range(int(num)):
                    self.x += 1
                    self._update_next()
                    self.update_path()

    def ht_sq_dist(self) -> int:
        if self.next is not None:
            d = self - self.next
            return d.x**2+d.y**2
        return -1

    def add_next(self, k: Knot):
        self.next = k

    def update_path(self):
        xy = (self.x,self.y)
        if xy not in self.path:
            self.path.append(xy)

    def _update_next(self):
        if self.next == None:
            return
        if self.ht_sq_dist() > 2:
            x = self.x - self.next.x
            y = self.y - self.next.y
            if x > 0:
                self.next.x += 1
            if x < 0:
                self.next.x -= 1
            if y > 0:
                self.next.y += 1
            if y < 0:
                self.next.y -= 1
        self.update_path()
        self.next.update_path()
        self.next._update_next()

class Rope:
    def __init__(self, segments: int = 1):
        if segments < 1:
            raise ValueError
        self.head = Knot(0,0,None,[(0,0)])
        self.tail = self.head
        for _ in range(segments - 1):
            self.add_segment()
    
    def __len__(self) -> int:
        acc = 1
        cur = self.head
        while cur.next != None:
            acc += 1
            cur = cur.next
        return acc

    def add_segment(self):
        if self.tail != None:
            self.tail.add_next(Knot(0,0, None))
            self.tail = self.tail.next

        
if __name__ == '__main__':
    with open('./test1.txt') as f:
        test1 = f.read().strip()
    with open('./test2.txt') as f:
        test2= f.read().strip()
    with open('./input.txt') as f:
        input = f.read().strip()


    tk = Rope(2)
    for i in test1.split("\n"):
        tk.head.move(i)
    print(len(tk.tail.path)) #type: ignore


    tk = Rope(2)
    for i in input.split("\n"):
        tk.head.move(i)
    print(len(tk.tail.path)) #type: ignore


    tk = Rope(10)
    for i in test2.split("\n"):
        tk.head.move(i)
    print(len(tk.tail.path)) #type: ignore
    
    # tk = Rope(10)
    # for i in input.split("\n"):
    #     tk.head.move(i)
    # print(len(tk.tail.path))  #type: ignore

