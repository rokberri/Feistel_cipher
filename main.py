from utils.binary_operations import *

def check_for_data_length(bytes_data, block_size):
    
    """Начальная проверка всего объема данных на кратность размерности блока шифрования block_size"""
    
    out_of_sim = len(bytes_data) % block_size
    if out_of_sim != 0:
        for i in range(block_size - out_of_sim):
            bytes_data += bytes(0x01)
    return bytes(bytes_data)#, out_of_sim

def read_data_from_file(path:str)->bytes:
    
    """Считывание всех данных в бинарной форме из фала path"""
    
    f = open(path, 'br')
    data = f.read()
    return data

def get_clean_data_for_encode(path:str, block_size:int)->bytes:
    data_to_encode = read_data_from_file(path)
    data_to_encode = check_for_data_length(data_to_encode,block_size)
    return data_to_encode
    
    
def generate_round_keys(secret_key,amount_of_rounds:int):
    #простая фигня, пока как заглушка используется 
    return list((i+1) for i in range(secret_key,secret_key+amount_of_rounds))

def F1(a:bytes,b:bytes)->bytes:
    return (lshift(a,4)) and (rshift(b,2))

def F2(a:bytes,b:bytes)->bytes:
    return (lshift(a,7)) ^ (not b)
    

def feistel_net(path, secret_key, block_size, amount_of_rounds,f1,f2)->bytes:
    
    secret_text = bytes()
    #считываем всю информацию для кодирования
    data_to_encode = get_clean_data_for_encode(path,block_size)

    #генерируем раундовые ключи, переписать метод(генераторная функция?)
    round_keys = generate_round_keys(secret_key, amount_of_rounds)
    #определение количества блоков для шифрования 
    am_of_blocks = round(len(data_to_encode)/block_size)
    print(am_of_blocks)
    # запускаем цикл для каждого блока 
    for block_num in range(am_of_blocks):
        # присваиваем блок для шифации 
        block = data_to_encode[block_num*block_size:(block_num*block_size)+block_size]
        # для каждого блока запускаем установленное кол-во раундов шифрования
        for round_num in range(amount_of_rounds):
            b0 = block[0:16]
            b1 = block[16:32]
            b2 = block[32:48]
            b3 = block[48:64]
            # doing something with blocks
            # ///
            b0 = xor(b0,round_keys[round_num].to_bytes(16))
            b1 = xor(b1,(f1(b2,b3)))
            b3 = xor(b3,((round_keys[round_num]>>3).to_bytes(16)))
            b2 = xor(b2,(f2(b0,b1)))
            # ///
            block = b2 + b3 + b1 + b0
        secret_text += block
    print(f'SECRET_TEXT:\n{secret_text}')
     
        
if __name__ == '__main__':
    SUPER_DUPER_SECRET_KEY = 16
    data_to_encode = get_clean_data_for_encode('OpenText.txt',64)
    feistel_net('OpenText.txt',SUPER_DUPER_SECRET_KEY,64,2,F1,F2)
    
    