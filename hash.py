from utils.convert import *
from utils import io
from feistel_net.feistel_net import Feistel_Net
from utils.binary_operations import *

def hash(filepath:str,f1,f2)->str:
    IV = '1111000110100110011101001011101101010100000110010110011110101100'
    f = Feistel_Net()
    hash_code = ''
    data_blocks = f.split_data_into_blocks(io.get_data_for_encode(filepath),64)
    for block in data_blocks:
        if len(hash_code) == 0:
            hash_code = XOR(block,IV)
            hash_code = f.encode_default([hash_code],IV,64,8,f1,f2)
            hash_code = XOR(IV,hash_code)
            hash_code = XOR(block,hash_code)
        else:
            prev_hash = hash_code
            hash_code = XOR(block,prev_hash)
            hash_code = f.encode_default([hash_code],prev_hash,64,8,f1,f2)
            hash_code = XOR(prev_hash,hash_code)
            hash_code = XOR(block,hash_code)
    return hash_code