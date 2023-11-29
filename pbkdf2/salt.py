from utils.binary_operations import NOT

def salt_by_user(salt:int|str)->str:
    res = ''
    if type(salt) == int:
        res =  NOT(bin(salt).replace('0b',''))
    else:
        for el in salt:
            res += str(ord(el))
        res = bin(int(res)).replace('0b','')
    return res