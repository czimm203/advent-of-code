#!/Library/Frameworks/Python.framework/Versions/3.11/bin/python3.11

from collections import namedtuple
from typing import Union

File = namedtuple("File", ["size", "name"])

class Directory:
    def __init__(self, name: str, files: list[File], top: Union['Directory',None], nested:dict[str,'Directory'] = {}):
        self.name = name
        self.files = files
        self.top = top
        self.nested = nested

    def __repr__(self) -> str:
        top_name = self.top.name if self.top else "/"
        return f"Directory(name={self.name}, files={self.files}, top={top_name},nested={','.join([n for n in self.nested])})"

    def add_subdir(self, d: str):
        tmp = Directory(d,[], self, {})
        self.nested[d] = tmp#update(tmp)
    
    def add_file(self, f: File):
        self.files.append(f)

    def size(self) -> int:
        sum = 0
        for file in self.files:
            sum += file.size
        for k in self.nested:
            sum = sum + self.nested[k].size()
        return sum
        
class FS:
    def __init__(self):
        self.root = Directory("/",[],None, {})
        self.cur = self.root
        self.directories: dict[str,Directory] = {"/":self.root}

    def _handle_cmd(self, cmd: str):
        arr = cmd.split(" ")
        match arr[1]:
            case "ls":
                # print("ls", arr)
                pass
            case "cd":
                if arr[2] == '/':
                    self.cur = self.root
                elif arr[2] == "..":
                    self.cur = self.cur.top if self.cur.top is not None else self.root
                else:
                    self.cur = self.cur.nested[f"{self.cur.name}/{arr[2]}"]

    def parse_tree(self, data: str):
        lines = data.split("\n")
        # cmds: list[str] = []
        for line in lines:
            line = line.strip()
            if is_cmd(line):
                self._handle_cmd(line)
                # cmds.append(cmd)
            elif is_dir(line):
                #cmds.append(line.split(" ")[1].strip())
                arr = line.split(" ")
                # print(f"Adding {arr[1]} to {self.cur}")
                n = f"{self.cur.name}/{arr[1]}"
                self.cur.add_subdir(n)
                self.directories[n] = self.cur.nested[n]
                # print(self.cur.nested)
            else:
                # cmds.append(line.split(" ")[1].strip())
                arr = line.split(" ")
                self.cur.files.append(File(int(arr[0]), arr[1]))

    def get_dir_sizes(self) -> dict[str,int]:
        sizes = {}
        for _,d in self.directories.items():
            sizes[d.name] = d.size()
        return sizes
            
def is_cmd(line: str) -> bool:
    if line.startswith("$"):
        return True
    else:
        return False

def is_dir(line: str) -> bool:
    if line.startswith("dir"):
        return True
    else:
        return False 

def part1(data: str):
    fs = FS()
    fs.parse_tree(data)
    sizes = fs.get_dir_sizes()
    sum = 0
    for k in sizes:
        if sizes[k] <= 100000:
            sum += sizes[k]
    print(sum)

def part2(data: str):
    fs = FS()
    fs.parse_tree(data)
    sizes = fs.get_dir_sizes()
    used = fs.root.size() 
    s = 9999999999
    for k in sizes:
        if used - sizes[k] < 40_000_000 and sizes[k] < s:
            s = sizes[k]
    print(s)

if __name__ == '__main__':
    with open('./test1.txt') as f:
        test = f.read().strip()
    with open('./input.txt') as f:
        input = f.read().strip()

    part1(test)
    part1(input)
    part2(test)
    part2(input)
