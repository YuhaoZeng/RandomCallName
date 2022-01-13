import random
from tkinter import Tk, Label, Button, Frame, StringVar, messagebox
from tkinter.filedialog import askopenfilename
from tkinter.font import Font

class Application(Frame):
    def __init__(self, master):
        super().__init__(master)
        self._name_list = []
        self._name_select = StringVar()
        self.pack()
        self.set_window()

    def set_window(self):
        """set window widget
        """
        self.master.title('点名器') # window name
        self.master.geometry('360x160+10+10') # window size and position, size (290, 160), initial position (10, 10)
        
        name_font = Font(family='黑体', size=60, weight='bold') # set label font
        self.name_label = Label(self.master, textvariable=self._name_select, font=name_font) # label to show name
        self.file_button = Button(self.master, text='导入', width=20, command=self.read_file) # button to import txt
        self.random_button = Button(self.master, text='点名', width=20, command=self.random_select) # button to random name 

        self.name_label.pack(side='top', expand='yes', fill='x')
        self.file_button.pack(side='left')
        self.random_button.pack(side='right')

    def read_file(self):
        """read file from given path and set name list
        """
        filepath = askopenfilename(defaultextension='.txt', filetypes=[('txt','*.txt')])
        with open(filepath, 'r', encoding='utf-8') as f:
            for line in f.readlines():
                self._name_list.append(line.strip())

    def random_select(self):
        """select a name from name_list
        """
        if len(self._name_list) < 1:
            messagebox.showwarning(title='warning', message='姓名列表为空')
        self._name_select.set(random.choice(self._name_list))


if __name__ == '__main__':
    window = Tk()
    RandomCall = Application(window)
    RandomCall.mainloop()
    
