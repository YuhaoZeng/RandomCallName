import tkinter
import random
import os

class Application_box():
    def __init__(self, master=None):
        super(self, tkinter.Frame).__init__()
        self.master.title('点名器')
        self
    def read_file(self,filepath):
        name_list = []
        with open(filepath, 'r') as f:
            for line in f.readlines():
                name_list.append(line.strip())

        return name_list        

if __name__ == '__main__':
    filepath = '/home/zengyuhao/zengyuhao/test_name_list.txt'
    print(read_file(filepath))

    
