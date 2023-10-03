
from utils.binary_operations import *


def F1(a:str,b:str)->str:
    return AND(shift(a,4),shift(b,2))
def F1_r(a:str,b:str)->str:
    return AND(shift(a,-4),shift(b,-2))
print(XOR('10011','10101'))
print(XOR('10101','00110'))
print(f'')