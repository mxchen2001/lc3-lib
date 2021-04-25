from os import close
from util_func import valid_symbol, check_offset_limit, check_immediate_limit, get_opcode, perform_psuedo_op, get_register, get_num

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

def translate(instruction: str):
    instr_tokens = instruction.split()
    opcode = instr_tokens[0]
    if ((el := perform_psuedo_op(instr_tokens)) != None):
        return el
    if ((opcode_bin := get_opcode(instr_tokens[0])) != None):
        if opcode == 'ADD':
            SR2 = get_register(instr_tokens[len(instr_tokens) - 1])
            if (SR2 != None): # does not use immediate
                return format(int(opcode_bin + get_register(instr_tokens[1]) + get_register(instr_tokens[2]) + '000' + SR2, base=2), '04x')
            else:
                return format(int(opcode_bin + get_register(instr_tokens[1]) + get_register(instr_tokens[2]) + '1' + format(get_num(instr_tokens[len(instr_tokens) - 1]), '07b' )[2:], base=2), '04x')
        if opcode == 'AND':
            SR2 = get_register(instr_tokens[len(instr_tokens) - 1])
            if (SR2 != None): # does not use immediate
                return format(int(opcode_bin + get_register(instr_tokens[1]) + get_register(instr_tokens[2]) + '000' + SR2, base=2), '04x')
            else:
                return format(int(opcode_bin + get_register(instr_tokens[1]) + get_register(instr_tokens[2]) + '1' + format(get_num(instr_tokens[len(instr_tokens) - 1]), '07b' )[2:], base=2), '04x')

        if opcode == 'BR':
            return format(int(opcode_bin + '111' + format(get_num(instr_tokens[len(instr_tokens) - 1]), '011b' )[2:], base=2), '04x')
        if opcode == 'BRN':
            return format(int(opcode_bin + '100' + format(get_num(instr_tokens[len(instr_tokens) - 1]), '011b' )[2:], base=2), '04x')
        if opcode == 'BRZ':
            return format(int(opcode_bin + '010' + format(get_num(instr_tokens[len(instr_tokens) - 1]), '011b' )[2:], base=2), '04x')
        if opcode == 'BRP':
            return format(int(opcode_bin + '001' + format(get_num(instr_tokens[len(instr_tokens) - 1]), '011b' )[2:], base=2), '04x')
        if opcode == 'BRNZ':
            return format(int(opcode_bin + '110' + format(get_num(instr_tokens[len(instr_tokens) - 1]), '011b' )[2:], base=2), '04x')
        if opcode == 'BRZP':
            return format(int(opcode_bin + '011' + format(get_num(instr_tokens[len(instr_tokens) - 1]), '011b' )[2:], base=2), '04x')
        if opcode == 'BRNP':
            return format(int(opcode_bin + '101' + format(get_num(instr_tokens[len(instr_tokens) - 1]), '011b' )[2:], base=2), '04x')
        if opcode == 'BRNZP':
            return format(int(opcode_bin + '111' + format(get_num(instr_tokens[len(instr_tokens) - 1]), '011b' )[2:], base=2), '04x')

        if opcode == 'JMP':
            return format(int(opcode_bin + '000' + get_register(instr_tokens[1]) + '000000', base=2), '04x')
        if opcode == 'JSR':
            return format(int(opcode_bin + '1' + format(get_num(instr_tokens[len(instr_tokens) - 1]), '013b' )[2:], base=2), '04x')
        if opcode == 'JSRR':
            return format(int(opcode_bin + '000' + get_register(instr_tokens[1]) + '000000', base=2), '04x')

        if opcode == 'LD':
            return format(int(opcode_bin + get_register(instr_tokens[1]) + format(get_num(instr_tokens[len(instr_tokens) - 1]), '011b' )[2:], base=2), '04x')
        if opcode == 'LDI':
            return format(int(opcode_bin + get_register(instr_tokens[1]) + format(get_num(instr_tokens[len(instr_tokens) - 1]), '011b' )[2:], base=2), '04x')
        if opcode == 'LDR':
            return format(int(opcode_bin + get_register(instr_tokens[1]) + get_register(instr_tokens[2]) + format(get_num(instr_tokens[len(instr_tokens) - 1]), '08b' )[2:], base=2), '04x')

        if opcode == 'LEA':
            return format(int(opcode_bin + get_register(instr_tokens[1]) + format(get_num(instr_tokens[len(instr_tokens) - 1]), '011b' )[2:], base=2), '04x')
        if opcode == 'NOT':
            return format(int(opcode_bin + get_register(instr_tokens[1]) + get_register(instr_tokens[2]) + '111111', base=2), '04x')
        if opcode == 'RET':
            return format(int(opcode_bin + '000111000000',base=2), '04x')
        if opcode == 'RTI':
            return format(int(opcode_bin + '000000000000',base=2), '04x')

        if opcode == 'ST':
            return format(int(opcode_bin + get_register(instr_tokens[1]) + format(get_num(instr_tokens[len(instr_tokens) - 1]), '011b' )[2:], base=2), '04x')
        if opcode == 'STI':
            return format(int(opcode_bin + get_register(instr_tokens[1]) + format(get_num(instr_tokens[len(instr_tokens) - 1]), '011b' )[2:], base=2), '04x')
        if opcode == 'STR':
            return format(int(opcode_bin + get_register(instr_tokens[1]) + get_register(instr_tokens[2]) + format(get_num(instr_tokens[len(instr_tokens) - 1]), '08b' )[2:], base=2), '04x')

        if opcode == 'TRAP':
            return format(int(opcode_bin + '0000' + format(get_num(instr_tokens[1]), '08b' )[2:], base=2), '04x')
    # return opcode


    

