
def shift(data:str,shift:int):
    """
    Побитовый сдвиг
    если shift > 0: вправо
    если shift < 0: влево
    """
    
    return data[-shift:] + data[:-shift]        

def AND(a:str, b:str)->str:
    result = ''
    for el in range(len(a)):
        if a[el] == b[el]:
            result += '1'
        else: 
            result += '0'
    return result


def XOR(a:str,b:str)-> str:
    """a XOR b"""
    
    result = ''
    for el in range(len(a)):
        if a[el]==b[el]:
            result += '0'
        else:
            result += '1'
    return result

def NOT(a:str)->str:
    result = ''
    for el in a:
        if el =='0':
            result += '1'
        else:
            result += '0'
    return result