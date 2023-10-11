from random import choice
from hash import hash
from utils.io import write_to_file
from utils.convert import convert

ALPH =list("""0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
               АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя""")

def test_alph():
     for el in ALPH:
          print(bin(ord(el)))


def birthday_paradox(hash_len:int,f1,f2):
    path = 'DataSet.txt'
    # data_set = [generate_text(hash_len) for text in range(4294967296)]
    # for i in range(4294967296):
        # t = ALPH[el1]+ALPH[el2]+ALPH[el3]+ALPH[el4]
    # write_to_file(path,bin(i).replace("0b",''))
    el_hash = hash(path,f1,f2)
    return el_hash
    # if el_hash in set(hash_db.keys()):
    #     # write_to_file('coll.txt',str(hash_db[convert(el_hash,2)]+'|<---->|'+str(i)))
        
    #     return
    # else:
    #     hash_db[convert(el_hash,2)] = i
            # print(str(convert(el_hash,2))+':'+str(i))

    # print(hash_db)

def generate_text(hash_len:int)->str:
    text = ''
   
    for i in range(hash_len):
        text += choice(ALPH)

    return text