from utils.convert import *


def read_data_from_file(path:str)->str:
    
    """Считывание всех данных фала path"""
    
    f = open(path, 'r')
    data = f.read()
    return data


def get_data_for_encode(path:str)->str:
    data_to_encode = read_data_from_file(path)
    return convert_to_binary(data_to_encode)