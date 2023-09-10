def read(path):
    f = open(path,'r')
    data = f.read()
    return data

t = read('OpenText.txt')
# 10000011100
text = ''
# print(t[0])
# print(bin(ord(t[0])))
# print(bin(ord(t[0]))[2:])
for el in t:
 
    add = '0'*(16-len(bin(ord(el))[2:]))
    print(add)
    text +=(add + bin(ord(el))[2:])
    print(len(bin(ord(el))[2:]))
    add=''

# from utils.binary_operations import *
# text = 'мама'
# b1 = bytes(text,'utf-8')
# key = '1234567891234567891234567891234567891234567891234567891234567890'
# print(len(bytes(key,'utf-8')))
# a0 = b1[0:2]
# a1 = b1[2:4]
# a2 = b1[4:6]
# a3 = b1[6:8]
# def F1(a:bytes,b:bytes)->bytes:
#     return (lshift(a,4)) and (rshift(b,2))

# def F2(a:bytes,b:bytes)->bytes:
#     return (lshift(a,7)) ^ (not b)
# print(bin(text))
# print(a0 and a1)
# print(F1(a0,a1))
# a = int(6).to_bytes(2)
# b = int(7).to_bytes(2)
# # print(xor(a,b))
# # print(int(a1_n,8))
