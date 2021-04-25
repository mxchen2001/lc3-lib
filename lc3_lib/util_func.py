import numpy as np

"""
The example starter code

def haversine(lon1: float, lat1: float, lon2: float, lat2: float) -> float:
    # Calculate the great circle distance between two points on the 
    # earth (specified in decimal degrees), returns the distance in
    # meters.
    # All arguments must be of equal length.
    # :param lon1: longitude of first place
    # :param lat1: latitude of first place
    # :param lon2: longitude of second place
    # :param lat2: latitude of second place
    # :return: distance in meters between the two sets of coordinates

    # Convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(np.radians, [lon1, lat1, lon2, lat2])
    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = np.sin(dlat/2.0)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon/2.0)**2
    c = 2 * np.arcsin(np.sqrt(a))
    km = 6367 * c
    return km * 1000
"""
"""

"""
def get_opcode(opcode: str, lc3b = False) -> str:
    opcode = opcode.upper()
    lc3b_opcodes = {
                    'ADD'    :  '0001', 
                    'AND'    :  '0101', 

                    'BR'     :  '0000',
                    'BRN'    :  '0000',
                    'BRZ'    :  '0000',
                    'BRP'    :  '0000',
                    'BRNZ'   :  '0000',
                    'BRZP'   :  '0000',
                    'BRNP'   :  '0000',
                    'BRNZP'  :  '0000',

                    'HALT'   :  '', 
                    'JMP'    :  '', 
                    'JSR'    :  '', 
                    'JSRR'   :  '', 
                    'LDB'    :  '', 
                    'LDW'    :  '',
                    'LEA'    :  '', 
                    'NOP'    :  '',
                    'NOT'    :  '', 
                    'RET'    :  '', 
                    'LSHF'   :  '', 
                    'RSHFL'  :  '', 
                    'RSHFA'  :  '', 
                    'RTI'    :  '', 
                    'STB'    :  '', 
                    'STW'    :  '', 
                    'TRAP'   :  '', 
                    'XOR'    :  '', 
                    }


    lc3_opcodes = {
                    'ADD'    :  '0001',
                    'AND'    :  '0101',

                    'BR'     :  '0000',
                    'BRN'    :  '0000',
                    'BRZ'    :  '0000',
                    'BRP'    :  '0000',
                    'BRNZ'   :  '0000',
                    'BRZP'   :  '0000',
                    'BRNP'   :  '0000',
                    'BRNZP'  :  '0000',

                    'JMP'    :  '1100',
                    'JSR'    :  '0100',
                    'JSRR'   :  '0100',
                    'LD'     :  '0010',
                    'LDI'    :  '1010',
                    'LDR'    :  '0110',
                    'LEA'    :  '1110',
                    'NOT'    :  '1001',
                    'RET'    :  '1100',
                    'RTI'    :  '1000',
                    'ST'     :  '0011',
                    'STI'    :  '1011',
                    'STR'    :  '0111',
                    'TRAP'   :  '1111', 
                  }
    if lc3b:
        return lc3b_opcodes[opcode] if opcode in lc3b_opcodes.keys() else None
    return lc3_opcodes[opcode] if opcode in lc3_opcodes.keys() else None

def get_register(register: str):
    registers = {
                    'R0': '000',
                    'R1': '001',
                    'R2': '010',
                    'R3': '011',
                    'R4': '100',
                    'R5': '101',
                    'R6': '110',
                    'R7': '111',
               }
    return registers[register.upper()] if register.upper() in registers.keys() else None

def get_num(num: str):
    try:
        if (num[0] == '#'):
            # decimal
            return int(num[1:], 10)
        elif (num[0] == '0' and num[1] == 'x'):
            # hexidecimal
            return int(num[2:], 16)
            # hexidecimal
        elif (num[0] == 'x'):
            return int(num[2:], 16)
        elif (num[0] == 'b'):
            # binary
            return int(num[1:], 2)
    except IndexError as e:
        print(e)
    except ValueError as e:
        print(e)
    return None


def get_start_addr(buffer: list):
    start_arr = buffer[0].split()
    if (start_arr[0].upper() != '.ORIG'):
        print('First Token must be ".orig"')
        return None
    try:
        return get_num(start_arr[1])
    except IndexError as e:
        print(e)

    return None

def valid_symbol(token: str):
    keywords = [
                    'ADD',
                    'AND',
                    'BR' ,
                    'BRN',
                    'BRZ',
                    'BRP',
                    'BRNZ',
                    'BRZP',
                    'BRNP',
                    'BRNZP',
                    'JMP',
                    'JSR',
                    'JSRR',
                    'LD',
                    'LDI',
                    'LDR',
                    'LEA',
                    'NOT',
                    'RET',
                    'RTI',
                    'ST',
                    'STI',
                    'STR',
                    'TRAP', 
                    'R0', 
                    'R1', 
                    'R2', 
                    'R3', 
                    'R4', 
                    'R5', 
                    'R6', 
                    'R7', 
                    '.ORIG',
                    '.FILL',
                    '.BLKW',
                    '.STRINGZ',
                    '.END',
                    'HALT'
                  ]

    if token.upper() in keywords:
        return False
    if not token[0].isalpha():
        return False
    return True

def perform_psuedo_op(instruction_list: list) -> list:
    opcode = instruction_list[0].upper()
    return_list = []
    if opcode == '.ORIG':
        return_list.append(hex(get_num(instruction_list[1])))
        return return_list
    elif opcode == '.FILL':
        return_list.append(hex(get_num(instruction_list[1])))
        return return_list
    elif opcode == '.BLKW':
        return_list.append(hex(get_num(instruction_list[1])))
        return return_list
    elif opcode == '.STRINGZ':
        # TODO
        pass
    elif opcode == '.END':
        # TODO
        pass
    elif opcode == 'HALT':
        return_list.append('0xF025')
        return return_list


def check_offset_limit(opcode: str, ofs_val: int) -> bool:
    offset_limits = {

                    'BR'     :  9,
                    'BRN'    :  9,
                    'BRZ'    :  9,
                    'BRP'    :  9,
                    'BRNZ'   :  9,
                    'BRZP'   :  9,
                    'BRNP'   :  9,
                    'BRNZP'  :  9,

                    'JSR'    :  11,

                    'LD'     :  9,
                    'LDI'    :  9,
                    'LDR'    :  6,

                    'LEA'    :  9,

                    'ST'     :  9,
                    'STI'    :  9,
                    'STR'    :  6,
                  }
    if opcode.upper() not in offset_limits.keys():
        return False

    ofs_limit = offset_limits[opcode.upper()]
    lower_bound = (-1 * (2**ofs_limit // 2)) + 1
    upper_bound = (2**ofs_limit // 2)

    return (ofs_val >= lower_bound and ofs_val <= upper_bound )

def check_immediate_limit(opcode: str, imm_val: int) -> bool:
    immediate_limits = {
                    'ADD'    :  5,
                    'AND'    :  5,
                    'TRAP'   :  8, 
                  }

    if opcode.upper() not in immediate_limits.keys():
        return False

    imm_limit = immediate_limits[opcode.upper()]
    lower_bound = (-1 * (2**imm_limit // 2)) + 1
    upper_bound = (2**imm_limit // 2)

    return (imm_val >= lower_bound and imm_val <= upper_bound )