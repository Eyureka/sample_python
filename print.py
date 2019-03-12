'''import re
m=re.findall(r"[A-Za-z]*[^ .]","Airline is west.")
print(m)'''

class Retail:
    def __init__(self,num):
        self.__num=num

    def get_num(self):
        return self.__num


    def set_num(self, value):
        self.__num = value

    num = property(get_num, set_num, None, None)
        
    
