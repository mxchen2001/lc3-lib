from numpy import lib
from lc3_lib import util_func


"""
This is the example code for the haversine function

def test_haversine():
    assert functions.haversine(52.370216, 4.895168, 52.520008, 13.404954) == 945793.4375088713
"""

def test_opcodes():
    assert util_func.get_opcode('AND') == '0101'
    assert util_func.get_opcode('awdawdawd') == None