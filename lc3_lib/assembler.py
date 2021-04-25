from parsing import parse, get_symbols, replace_symbols, translate
from util_func import get_start_addr
from copy import deepcopy

def print_symbol_table(symbol_table: dict):
    for key, value in symbol_table.items():
        print("Symbol: ", key, "Value: ", hex(value))

def assemble(filename: str, o_filename = "main.asm"):
    if ((buffer := parse(filename)) == None):
        return

    for string in buffer:
        print(string)

    starting_address = get_start_addr(buffer)
    symbol_table = get_symbols(buffer, starting_address)

    buffer_w_symbols = deepcopy(buffer)
    buffer_w_symbols.pop(0)

    buffer_w_symbols = replace_symbols(buffer_w_symbols, symbol_table, starting_address)

    print(buffer_w_symbols)

    output_buffer = []
    for instruction in buffer_w_symbols:
        output_buffer.append(translate(instruction))


    print(output_buffer)



assemble("input")
import sys
print(sys.argv)
