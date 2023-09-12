from utils.binary_operations import *
from utils.io import *
from math import ceil

class Feistel_Net:

    def encode(self,path, secret_key, block_size, amount_of_rounds,f1,f2)->bytes:
        
        secret_text = ''
        #считываем всю информацию для кодирования
        data_to_encode = get_data_for_encode(path)
        print(f'CLEAN DATA:\n{data_to_encode}')
        # делим ее на блоки
        blocks = self.split_data_into_blocks(data_to_encode,block_size)
        # #генерируем раундовые ключи, переписать метод(генераторная функция?)
        round_keys = self.generate_round_keys(secret_key, amount_of_rounds)

        # # запускаем цикл для каждого блока 
        for block in blocks:
            # для каждого блока запускаем установленное кол-во раундов шифрования
            for round_num in range(amount_of_rounds):
                b0 = block[0:16]
                b1 = block[16:32]
                b2 = block[32:48]
                b3 = block[48:64]
                # doing something with blocks
                # ///
                b0 = XOR(b0,round_keys[round_num])
                b3 = XOR(b3,f1(b0,b1))
                b2 = XOR(b2,NOT(round_keys[round_num]))
                b1 = XOR(b1,(f2(b2,b3)))
                # ///
                block = b2 + b3 + b1 + b0  
            secret_text += block
        print(f'SECRET_TEXT:\n{secret_text}')
        
        
        
        
        
        
    def decode(self, path, secret_key, block_size, amount_of_rounds,f1,f2):
        secret_text = ''
        #считываем всю информацию для кодирования
        data_to_encode = read_data_from_file(path)
        print(f'SECRET_TEXT:\n{data_to_encode}')
        # делим ее на блоки
        blocks = self.split_data_into_blocks(data_to_encode,block_size)
        # #генерируем раундовые ключи, переписать метод(генераторная функция?)
        round_keys = self.generate_round_keys(secret_key, amount_of_rounds)
        round_keys.reverse()
        # # запускаем цикл для каждого блока 
        for block in blocks:
            # для каждого блока запускаем установленное кол-во раундов шифрования
            for round_num in range(amount_of_rounds):
                b2 = block[0:16]
                b3 = block[16:32]
                b1 = block[32:48]
                b0 = block[48:64]
                # doing something with blocks
                # ///
                b1 = XOR(b1,f2(b2,b3))
                b2 = XOR(b2,NOT(round_keys[round_num]))
                b3 = XOR(b3, f1(b0,b1))
                b0 = XOR(b0, round_keys[round_num])
                print(b0,'>>>',)
                # ///
                block = b0 + b1 + b2 + b3  
            secret_text += block
            # print(f'ClEAN BLOCK:{block}')

        print(f'CLEAN DATA:\n{secret_text}')
        
        
    def generate_round_keys(self,secret_key:str,amount_of_rounds:int)->list[str]:
        list_of_keys = list()
        for i in range(amount_of_rounds):
            r_key = XOR(shift(secret_key,i+1),secret_key)[0:16]
            list_of_keys.append(r_key)
        return list_of_keys
    
    
    def split_data_into_blocks(self,data_to_encode:str,block_size:int)->list[str]:
        block_list = list()
        for i in range(ceil(len(data_to_encode)/block_size)):
            block = data_to_encode[i*block_size:((i+1)*block_size)]
            if len(block)< block_size:
                block = '0'*(block_size-len(block)) + block
            block_list.append(block)
        return block_list
        