
def lshift(data:bytes,shift:int):
    """<<"""
    
    data = data[shift:]
    for i in range(shift):
        data += b'\x00'
    return data
            
def rshift(data:bytes,shift:int):
    """>>"""
    
    add = bytes()
    data = data[:shift]
    for i in range(shift):
        add += b'\x00'
    return add+data            

def xor(a,b):
    """a XOR b"""
    
    result = bytes()
    for el in range(len(a)):
        if a[el]==b[el]:
            result += b'\x00'
        else:
            result += b'\x01'
    return result