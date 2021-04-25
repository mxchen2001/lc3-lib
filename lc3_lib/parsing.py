from os import close
from util_func import get_start_addr, get_opcode, get_register, get_num

def file_check(fn):
    try:
        open(fn, 'r').close()
        return 1
    except IOError:
        print("Error: File does not appear to exist.")
        return 0


def parse(filename: str):
    if(file_check(filename) == 0):
        return None
    
    with open(filename, 'r') as file:
        buffer = []
        while True:
            line = file.readline()
            if not line or line.strip().upper() == ".END": 
                break # stop the loop if no line was read
            line = line.strip()
            valid_code = ""
            for char in line:
                if char == ';':
                    break
                valid_code += char
            if len(valid_code) != 0:
                buffer.append(valid_code)
        return buffer


def get_symbols(buffer: list) -> dict:
    for line in buffer:
        if get line[0]

    


import sys
print(sys.argv)

temp = parse(sys.argv[1])


for string in temp:
    print(string)

print(get_start_addr(temp))

    

