#!/Library/Frameworks/Python.framework/Versions/3.11/bin/python3.11

import json

def is_correct(l, r):
    print(type(l), type(r))
    match l, r:
        case int(l), int(r):
            print(l,r)
            if l < r:
                return True
            elif l > r:
                return False
        case list(l), list(r):
            for j,i in zip(l,r):
                is_correct(j,i)
            if len(l) > len(r):
                return(False)
            elif len(l) < len(r):
                return(True)
        case [list(l), int(r)] | [int(l), list(r)]:
            print(l,r)
            if isinstance(l,list):
                if l[0] < r:
                    return True
                elif l[0] > r:
                    return False
            else:
                if l < r[0]: #pyright: ignore
                        return True
                elif l > r[0]: #pyright: ignore
                        return False


if __name__ == '__main__':
    with open('./test1.txt') as f:
        test = f.read().strip()
    with open('./input.txt') as f:
        input = f.read().strip()

    lines = test.split("\n\n")
    thing = lines[1].split("\n")
    l = json.loads(thing[0])
    r = json.loads(thing[1])
    print(is_correct(l,r))
    # for line in lines:
    #     split = line.split("\n")
    #     l = json.loads(split[0])
    #     r = json.loads(split[1])
    #     print(is_correct(l,r))
        
