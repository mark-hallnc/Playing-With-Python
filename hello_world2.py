# This program displays two labels with text.

import tkinter

class MyGUI:
    def __init__(self):
        # Create the main window widget.
        self.main_window = tkinter.Tk()

        # Create two Label widget.
        self.label1 = tkinter.Label(self.main_window, \
                                    text='1')
        self.label2 = tkinter.Label(self.main_window, \
                         text='2.')
        self.label3 = tkinter.Label(self.main_window, \
                         text='3')
        self.label4 = tkinter.Label(self.main_window, \
                         text='4')

        # Call both Label widgets' pack method.
        self.label1.pack(side='left')
        self.label2.pack(side='right')
        self.label3.pack(side='top')
        self.label4.pack(side='bottom')

        # Enter the tkinter main loop.
        tkinter.mainloop()

# Create an instance of the MyGUI class.
my_gui = MyGUI()

