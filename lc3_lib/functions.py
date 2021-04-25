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
def get_opcode(opcode, lc3b = False) -> str:
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
                    'XOR'    : '', 
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
                    'TRAP'   : '1111', 
                  }
    if lc3b:
        return lc3b_opcodes[opcode] if opcode in lc3b_opcodes.keys() else None
    return lc3_opcodes[opcode] if opcode in lc3_opcodes.keys() else None


