#!/Library/Frameworks/Python.framework/Versions/3.11/bin/python3.11

if __name__ == '__main__':
    with open('./test1.txt') as f:
        test = f.readlines().strip()
    with open('./input.txt') as f:
        input = f.readlines().strip()
