def read_data_from_file(path:str)->str:
    
    """Считывание всех данных фала path"""
    
    f = open(path, 'r')
    data = f.read()
    return data

def convert_to_binary(data:str)->str:
    binary_data = ''
    for el in data:
        cur_sim = bin(ord(el)).replace('0b','')
        binary_data += '0'*(16-len(cur_sim)) + cur_sim
    return binary_data

def get_data_for_encode(path:str)->str:
    data_to_encode = read_data_from_file(path)
    return convert_to_binary(data_to_encode)