from os import close
from util_func import valid_symbol, check_offset_limit, check_immediate_limit

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
                buffer.append(valid_code.replace(',', ''))
        return buffer


def get_symbols(buffer: list, starting_addr: int) -> dict:
    symbol_table = dict()
    for i in range(0, len(buffer)):
        line = buffer[i].split()
        try:
            if valid_symbol(line[0]):
                symbol_table[line[0]] = i + starting_addr - 1
        except IndexError as e:
            print(e)
    return symbol_table

def replace_symbols(buffer: list, symbol_table: dict, starting_addr: int) -> list:
    return_buffer = []
    for i in range(0, len(buffer)):
        tokens = buffer[i].split()
        if (tokens[0] in symbol_table.keys()):
            tokens.pop(0)
        if ((symbol_reference := tokens[len(tokens) - 1]) in symbol_table.keys()):
            pc_ofs = symbol_table[symbol_reference] - (i + starting_addr) - 1
            tokens[len(tokens) - 1] = "#" + str(pc_ofs)

        temp = ""
        for token in tokens:
            temp += token + ' '
        temp.strip()
        return_buffer.append(temp)
        # print(tokens)
    return return_buffer

            # # TODO check opcode is valid
            # if (check_offset_limit(tokens[0], pc_ofs) == False and check_immediate_limit(tokens[0], pc_ofs)):
            #     print("PC offset is out of bounds")
            #     return None



    

