from utils.convert import Converter
from feistel_net import Feistel_Net
from utils.binary_operations import *



def F1(a:str,b:str)->str:
    return AND(shift(a,4),shift(b,2))

def F2(a:str,b:str)->str:
    return XOR(shift(a,7),NOT(b))


if __name__ == '__main__':
    SUPER_DUPER_SECRET_KEY = '1110010110001111110000101101001001101111000000110111110111110111'
    feistel_net = Feistel_Net()
    # feistel_net.encode('OpenText.txt',SUPER_DUPER_SECRET_KEY,64,1,F1,F2)
    # feistel_net.decode('SecretText.txt',SUPER_DUPER_SECRET_KEY,64,1,F1,F2)
    print('----------------------------------------------------------------------')
    feistel_net.encode('OpenText.txt',SUPER_DUPER_SECRET_KEY,64,1,F1,F2,'OFB')
    feistel_net.decode('SecretText.txt',SUPER_DUPER_SECRET_KEY,64,1,F1,F2,'OFB')
    
    