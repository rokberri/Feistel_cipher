from feistel_net.feistel_net import Feistel_Net
from utils.binary_operations import *
from utils.io import *
from hash import hash


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

    print(convert(hash('OpenText.txt',F1,F2),2))
    # 4807014621125135592
    # 13603019358187758587
    