from feistel_net.feistel_net import Feistel_Net
from utils.binary_operations import *
from utils.io import *
from hash import HashFunction
import multiprocessing as mp
from crack import find_similat_text, generate_text
from multiprocessing import Pool
from pbkdf2.pbkdf2 import PBKDF2

def F1(a:str,b:str)->str:
    return AND(shift(a,4),shift(b,2))

def F2(a:str,b:str)->str:
    return XOR(shift(a,7),NOT(b))

def task_6():
    password = convert_to_binary('pass')
    h = HashFunction(F1,F2)
    o = PBKDF2(h,2,16)
    o.pbkdf2_algorithm('key.txt',password)

if __name__ == '__main__':
    task_6()
    # SUPER_DUPER_SECRET_KEY = '1110010110001111110000101101001001101111000000110111110111110111'
    # feistel_net = Feistel_Net()
    # print('----------------------------------------------------------------------')
    # print(get_data_for_encode("OpenText.txt"))
    # print('----------------------------------------------------------------------')
    # secret_text = feistel_net.encode('OpenText.txt',SUPER_DUPER_SECRET_KEY,64,8,F1,F2)
    # print(f"SECRET TEXT: {secret_text}")
    # open_text = feistel_net.decode('SecretText.txt',SUPER_DUPER_SECRET_KEY,64,8,F1,F2)
    # print(f"OPEN TEXT: {open_text}")
    # print(convert_from_binary(open_text,16))
    
    # print(find_similat_text("OpenText.txt",F1,F1))
    # print(hash("OpenText.txt",F1,F2,bin_data=True ,use_fin_func=False))

    # new_words = set(generate_text(8) for el in range(65537))
    # with mp.Pool(32) as p:
    #     p.map(find_similat_text, new_words)


    # 1001001110110111010111010001110110000011110100011010100101001001 -> 1110101011010101110110100001010100011010100101011010110101010111
    # 1111100000100110010110000011000000010110011111011000010010110011 -> 1111111111111111111111111111111111111111111111111111111111111111
    # 1111100000100110010110000011000000010110011111011000010010110011 -> 0000000000000000000000000000000000000000000000000000000000000000
    # 1111100000100110010110000011000000010110011111011000010010110011 -> 0000000000000000111111111111111100000000000000001111111111111111
    # 1111100000100110010110000011000000010110011111011000010010110011 -> 1111111111111111000000000000000011111111111111110000000000000000                                                                   
    # 1111100000100110010110000011000000010110011111011000010010110011 -> 01...
    # 1111100000100110010110000011000000010110011111011000010010110011 -> 10..
    