#!/Library/Frameworks/Python.framework/Versions/3.11/bin/python3.11
def find_packet_start(data: str) -> int:
    data = data.strip()
    buf = set()
    for i in range(len(data[3:])):
        buf = data[i:i+4]
        str_set = {*buf}
        if len(str_set) == 4:
            return i+4
    return -1

def find_message_start(data: str):
    data = data.strip()
    for i in range(len(data[13:])):
        buf = data[i:i+14]
        str_set = {*buf}
        if len(str_set) == 14:
            return i+14
    return -1
        

if __name__ == "__main__":
    with open("./test1.txt") as f:
        test = f.read()
    with open("./input.txt") as f:
        input = f.read()

    print(find_packet_start(test))
    print(find_message_start(test))
    print(find_packet_start(input))
    print(find_message_start(input))


