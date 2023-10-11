from feistel_net.feistel_net import Feistel_Net
from utils.binary_operations import *
from utils.io import *
from hash import hash
from crack import birthday_paradox
import multiprocessing as mp
from multiprocessing import Pool

def F1(a:str,b:str)->str:
    return AND(shift(a,4),shift(b,2))

def F2(a:str,b:str)->str:
    return XOR(shift(a,7),NOT(b))

if __name__ == '__main__':
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

    # print(birthday_paradox(64,F1,F2))
    print(hash("OpenText.txt",F1,F2))
    # print(convert(hash("OpenText.txt",F1,F2),2))
    # with mp.Pool(26) as p:
    #     p.map(birthday_paradox(64,F1,F2), sorted_alph)

    # 1001001110110111010111010001110110000011110100011010100101001001 -> 1110101011010101110110100001010100011010100101011010110101010111
    # 1111100000100110010110000011000000010110011111011000010010110011 -> 1111111111111111111111111111111111111111111111111111111111111111
    # 1111100000100110010110000011000000010110011111011000010010110011 -> 0000000000000000000000000000000000000000000000000000000000000000
    # 1111100000100110010110000011000000010110011111011000010010110011 -> 0000000000000000111111111111111100000000000000001111111111111111
    # 1111100000100110010110000011000000010110011111011000010010110011 -> 1111111111111111000000000000000011111111111111110000000000000000                                                                   
    # 1111100000100110010110000011000000010110011111011000010010110011 -> 01...
    # 1111100000100110010110000011000000010110011111011000010010110011 -> 10..