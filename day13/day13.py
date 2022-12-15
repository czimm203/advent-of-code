#!/Library/Frameworks/Python.framework/Versions/3.11/bin/python3.11

import json

def is_correct(l, r):
    # print(l,r)
    match l, r:
        case int(l), int(r):
            if l < r:
                return True
            elif l > r:
                return False
        case list(l), list(r):
            for j,i in zip(l,r):
                out = is_correct(j,i)
                if out != None:
                    return is_correct(j,i)
                
            if len(l) > len(r):
                return(False)
            elif len(l) < len(r):
                return(True)
        case [list(l), int(r)] | [int(l), list(r)]:
            if isinstance(l,list):
                if len(l) == 0:
                    return True
                if isinstance(l[0], list):
                    if len(l[0]) != 0:
                        return is_correct(l[0],r)
                    else:
                        return True
                if l[0] < r:
                    return True
                elif l[0] > r:
                    return False
            else:
                if len(r) == 0:
                    return False
                if isinstance(r[0], list):
                    if len(r[0]) != 0:
                        return is_correct(l,r[0])
                    else:
                        return False
                if l < r[0]: #pyright: ignore
                        return True
                elif l > r[0]: #pyright: ignore
                        return False
    return None


def part1(data: str):
    lines = data.split("\n\n")
    # thing = lines[5].split("\n")
    # l = json.loads(thing[0])
    # r = json.loads(thing[1])
    # print(is_correct(l,r))
    arr = []
    for i,line in enumerate(lines):
        split = line.split("\n")
        l = json.loads(split[0])
        r = json.loads(split[1])
        correct = is_correct(l,r)
        if correct:
            arr.append(i+1)
    print(arr)
    print(sum(arr))

if __name__ == '__main__':
    with open('./test1.txt') as f:
        test = f.read().strip()
    with open('./input.txt') as f:
        input = f.read().strip()
    
    part1(test)
    part1(input)
        
