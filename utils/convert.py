def convert(num:str, base):
    """
    Конвертация строки в число из системы с указанным основанием
    """
    num_new_base = 0
    size = len(num)-1
    for sim in enumerate(num):
        num_new_base += int(int(sim[1])*(base**(size-sim[0])))
    return num_new_base

def convert_to_binary(data:str)->str:
    """
    Конвертиция символьной строки в бинарное представление
    """
    binary_data = ''
    for el in data:
        cur_sim = bin(ord(el)).replace('0b','')
        binary_data += '0'*(16-len(cur_sim)) + cur_sim
    return binary_data

def convert_from_binary(data:str, letter_size)->str:
    if data.count('0b') > 0:
        data = data.replace('0b','')
    result=  ''
    for i in range(len(data)):
        sim = chr(convert(data[(i*letter_size):((i+1)*letter_size)],2))
        result += sim
    return result