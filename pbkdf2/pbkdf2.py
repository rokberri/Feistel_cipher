from random import randint
from math import ceil
from feistel_net.feistel_net import Feistel_Net
from hash import HashFunction
from utils.io import get_data_for_encode
from utils.binary_operations import XOR,AND

class PBKDF2:
    def __init__(self, algorithm:HashFunction,password:str, salt=randint(0,65536)) -> None:
        self.__algorithm = algorithm
        self.__iterations =  self.__algorithm.iter_num
        self.__password = password
        self.__salt = salt


    def pbkdf2_algorithm(self,filepath:str,password:str):
        self.__algorithm.IV = password
        key = get_data_for_encode(filepath, False)

        length = ceil(len(key)/64) # декоратор, приводящий все аутпуты к стандартной длине??
        am_of_bits = len(key) - (length -1) * 64

        blocks = Feistel_Net.split_data_into_blocks(key,64)
        encoded_blocks = list()

        for c,block in enumerate(blocks):
            tmp = ''
            for iter in range(c+1):
                if len(tmp) == 0:
                    tmp = AND(self.__salt,XOR(self.__algorithm.hash(list(block)),self.__salt))
                else:
                    tmp = AND(tmp,XOR(self.__algorithm.hash(list(block)),self.__salt))
            encoded_blocks.append(tmp)
        last_el = len(encoded_blocks)
        key_res = encoded_blocks[0]#тут пока весь последний блок берется 
        for el in encoded_blocks:
            key_res = AND(key_res,el)
        return key_res

    def print_salt(self):
        print(bin(self.__salt).replace('0b',''))
    