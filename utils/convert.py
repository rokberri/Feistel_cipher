class Converter():
    def __init__(self, num_base:int):
        self.base = num_base

    def convert(self, num:str):
        num_new_base = 0
        size = len(num)-1
        for sim in enumerate(num):
            num_new_base += int(int(sim[1])*(self.base**(size-sim[0])))
        return num_new_base
    
    