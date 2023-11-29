from utils.convert import *


def read_data_from_file(path:str)->str:
    
    """Считывание всех данных фала path"""
    
    f = open(path, 'r')
    data = f.read()
    return data


def get_data_for_encode(path:str, bin:bool)->str:
    data_to_encode = read_data_from_file(path)
    if bin:
        return data_to_encode
    else: 
        return convert_to_binary(data_to_encode)


def write_to_file(path:str,data:str)->None:
    with open(path,'w',encoding='utf-8') as f:
        f.write(data)