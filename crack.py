import io
from random import choice
from hash import HashFunction
from utils import io
from utils.binary_operations import *
from utils.convert import convert

ALPH =list("""0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя""")

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

def generate_text(length:int)->str:
    text = ''
   
    for i in range(length):
        text += choice(ALPH)

    return text

def F1(a:str,b:str)->str:
    return AND(shift(a,4),shift(b,2))

def F2(a:str,b:str)->str:
    return XOR(shift(a,7),NOT(b))


def find_similat_text(new_word):
    filepath = 'OpenText.txt'
    open_text = io.read_data_from_file(filepath)
    list_of_word = open_text.split()
    origin_hash = hash(filepath,F1,F2,use_fin_func=True)
    for ind, word in enumerate(list_of_word):
        modified_words = list_of_word.copy()
        modified_words[ind] = new_word
        modified_text = " ".join(modified_words)
        # io.write_to_file("DataSet.txt",modified_text)
        new_hash = hash(modified_text,F1,F2,use_fin_func=True)
        if new_hash == origin_hash :
            io.write_to_file('coll.txt', modified_text)
            return modified_text
        print(f"{new_word}----{new_hash}")
    return "Fail"


def find_diff(origin:str, new_txt:str)->int:
    am = 0 
    for el in range(len(origin)):
        if not origin[el] == new_txt[el]:
            am += 1

    return am
