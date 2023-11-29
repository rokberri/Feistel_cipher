from utils.convert import *
from utils import io
from feistel_net.feistel_net import Feistel_Net
from utils.binary_operations import *

class HashFunction:
    def __init__(self, f1, f2,iter_num=8, IV = '1111000110100110011101001011101101010100000110010110011110101100') -> None:
        self.__f1 = f1
        self.__f2 = f2
        self.__IV = IV
        self.__iter_num = iter_num
    
    @property
    def iter_num(self)->int:
        return self.__iter_num
    @property
    def IV(self)->str:
        return self.__IV
    
    @IV.setter
    def IV(self,salt:str)->None:
        self.__IV = salt

    def get_hash(self,filepath:str, bin_data:False, use_fin_func=False):
        if filepath.count('.txt')==1:
            data_blocks = Feistel_Net.split_data_into_blocks(io.get_data_for_encode(filepath,bin_data),64)
        else:
            data_blocks = Feistel_Net.split_data_into_blocks(convert_to_binary(filepath),64)
        return hash(data_blocks,use_fin_func)

    def hash(self, data_blocks, use_fin_func=False)->str:
        f = Feistel_Net()
        hash_code = ''
        for block in data_blocks:
            if len(hash_code) == 0:
                hash_code = XOR(block,self.__IV)
                hash_code = f.encode_default([hash_code],self.__IV,64,self.__iter_num,self.__f1,self.__f2)
                hash_code = XOR(self.__IV,hash_code)
                hash_code = XOR(block,hash_code)
            else:
                prev_hash = hash_code
                hash_code = XOR(block,prev_hash)
                hash_code = f.encode_default([hash_code],prev_hash,64,self.__iter_num,self.__f1,self.__f2)
                hash_code = XOR(prev_hash,hash_code)
                hash_code = XOR(block,hash_code)
        if use_fin_func:
            return self.finalization_func(hash_code)
        else: return hash_code


    def finalization_func(self, hash_code:str)->str:
        return hash_code[56:64]