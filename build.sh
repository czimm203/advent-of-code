#!/bin/sh

DAY=$1

mkdir $DAY
cd $DAY
touch "$DAY.py"
chmod +x "$DAY.py"
echo "#!/Library/Frameworks/Python.framework/Versions/3.11/bin/python3.11

if __name__ == '__main__':
    with open('./test1.txt') as f:
        test = f.readlines().strip()
    with open('./input.txt') as f:
        input = f.readlines().strip()" > "$DAY.py"

touch "input.txt"
touch "test1.txt"
touch "test2.txt"

