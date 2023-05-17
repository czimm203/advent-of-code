#!/Library/Frameworks/Python.framework/Versions/3.11/bin/python3.11

import json

def is_correct(l, r):
    print(l,r, "\n",sep="\n")
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
                    return out
                        
            if len(l) < len(r):
                return True
            elif len(l) > len(r):
                return False

        case [list(l), int(r)] | [int(l), list(r)]:
            if isinstance(l,list):
                if len(l) == 0:
                    return True
                for item in l:
                    if isinstance(item, list):
                        if len(item) != 0:
                            return is_correct(item,r)
                        else:
                            return True
                    elif isinstance(item,int):
                        if item < r: #pyright: ignore
                            return True
                        elif item > r: #pyright: ignore
                            return False
                        else:
                            break

            elif isinstance(r,list):
                if len(r) == 0:
                    return False
                for item in r:
                    if isinstance(item, list):
                        if len(item) != 0:
                            return is_correct(l,item)
                        else:
                            return False
                    elif isinstance(item, int):
                        if l < item:
                                return True
                        elif l > item:
                                return False
                        else:   
                            break
    return None


def part1(data: str):
    lines = data.split("\n\n")
    thing = 0
    for i,line in enumerate(lines):
        split = line.split("\n")
        l = json.loads(split[0])
        r = json.loads(split[1])
        correct = is_correct(l,r)
        if correct:
            print(l,r,i+1,"\n", sep="\n")
            # print("aah")
            # arr.append(i+1)
            thing += i+1

    print(thing)
    # arr.clear()

if __name__ == '__main__':
    with open('./test1.txt') as f:
        test = f.read().strip()
    with open('./input.txt') as f:
        input = f.read().strip()
    with open('./me.txt') as f:
        me = f.read().strip()
    
    part1(me)
    # part1(input)
