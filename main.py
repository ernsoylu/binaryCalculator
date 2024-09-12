import tkinter as tk
from tkinter import ttk, StringVar


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Binary Calculator")
        self.geometry("405x300+250+250")
        self.resizable(False, False)

        #Adding Mainframe to Application Window
        self.mainframe = Mainframe(self)
        self.mainloop()

class Mainframe(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.grid()
        # Initialize Tkinter Variables as Base Variables
        self.entryTxt = StringVar()
        self.bitArray = [tk.BooleanVar(), tk.BooleanVar(), tk.BooleanVar(), tk.BooleanVar(), tk.BooleanVar(),
                         tk.BooleanVar(), tk.BooleanVar(), tk.BooleanVar(), tk.BooleanVar(), tk.BooleanVar(),
                         tk.BooleanVar(), tk.BooleanVar(), tk.BooleanVar(), tk.BooleanVar(), tk.BooleanVar(),
                         tk.BooleanVar(), tk.BooleanVar(), tk.BooleanVar(), tk.BooleanVar(), tk.BooleanVar(),
                         tk.BooleanVar(), tk.BooleanVar(), tk.BooleanVar(), tk.BooleanVar(), tk.BooleanVar(),
                         tk.BooleanVar(), tk.BooleanVar(), tk.BooleanVar(), tk.BooleanVar(), tk.BooleanVar(),
                         tk.BooleanVar(), tk.BooleanVar()]
        self.create_widgets()
    # Initialize base functions for working on Bit Array
    # list_to_bin : convert bitArray boolean array to decimal than write decimal value to textbox
    def list_to_bin(self):
        dec = 0
        for i in range(0, len(self.bitArray)):
            if self.bitArray[i].get():
                dec += 1 << i
        self.entryTxt.set(str(dec))

    # dec_to_bin_list: convert textbox value decimal than binary, populate binary value to bit array bit by bit as boolean value
    def dec_to_bin_list(self):
        if not (self.entryTxt.get().isnumeric()) or int(self.entryTxt.get()) > 4294967295:
            self.entryTxt.set("4294967295")
        bin_val = bin(int(self.entryTxt.get()))[2:]
        for ind, val in enumerate(bin_val[::-1]):
            if val == "1":
                self.bitArray[ind].set(True)
            else:
                self.bitArray[ind].set(False)

    # clear_all: clear textbox and checkboxes via setting all values False in bit array
    def clear_all(self):
        for i in self.bitArray:
            i.set(False)
        self.entryTxt.set("0")

    def create_widgets(self):
        self.columnconfigure((0,1,2,3), weight=1, uniform = 'a')
        self.rowconfigure((0,1,2,3,4,5,6,7,8), weight=1, uniform = 'a')
        # Add components spread across 4 column
        # text box spanned 2 columns ( 0 and 1 )
        ttk.Entry(self, textvariable=self.entryTxt).grid(column=0, row=0, columnspan=2, padx=3, pady=10)
        # buttons start from column 2
        # Convert button invoke dec_to_bin_list function
        ttk.Button(self, text="Convert", command=self.dec_to_bin_list).grid(column=2, row=0, padx=3, pady=10)
        # Clear button invoke clear_all function
        ttk.Button(self, text="Clear", command=self.clear_all).grid(column=3, row=0, padx=3, pady=10)
        # 32 Check button added to the grid, each checkbox value attached to bit Array and click event command list_to_bin invoked
        ttk.Checkbutton(self, text="Bit 0", width=6, variable=self.bitArray[0], command=self.list_to_bin).grid(column=0, row=1, padx=3,
                                                                                                pady=3)
        ttk.Checkbutton(self, text="Bit 1", width=6, variable=self.bitArray[1], command=self.list_to_bin).grid(column=0, row=2, padx=3,
                                                                                                pady=3)
        ttk.Checkbutton(self, text="Bit 2", width=6, variable=self.bitArray[2], command=self.list_to_bin).grid(column=0, row=3, padx=3,
                                                                                                pady=3)
        ttk.Checkbutton(self, text="Bit 3", width=6, variable=self.bitArray[3], command=self.list_to_bin).grid(column=0, row=4, padx=3,
                                                                                                pady=3)
        ttk.Checkbutton(self, text="Bit 4", width=6, variable=self.bitArray[4], command=self.list_to_bin).grid(column=0, row=5, padx=3,
                                                                                                pady=3)
        ttk.Checkbutton(self, text="Bit 5", width=6, variable=self.bitArray[5], command=self.list_to_bin).grid(column=0, row=6, padx=3,
                                                                                                pady=3)
        ttk.Checkbutton(self, text="Bit 6", width=6, variable=self.bitArray[6], command=self.list_to_bin).grid(column=0, row=7, padx=3,
                                                                                                pady=3)
        ttk.Checkbutton(self, text="Bit 7", width=6, variable=self.bitArray[7], command=self.list_to_bin).grid(column=0, row=8, padx=3,
                                                                                                pady=3)
        ttk.Checkbutton(self, text="Bit 8", width=6, variable=self.bitArray[8], command=self.list_to_bin).grid(column=1, row=1, padx=3,
                                                                                                pady=3)
        ttk.Checkbutton(self, text="Bit 9", width=6, variable=self.bitArray[9], command=self.list_to_bin).grid(column=1, row=2, padx=3,
                                                                                                pady=3)
        ttk.Checkbutton(self, text="Bit 10", width=6, variable=self.bitArray[10], command=self.list_to_bin).grid(column=1, row=3,
                                                                                                  padx=3, pady=3)
        ttk.Checkbutton(self, text="Bit 11", width=6, variable=self.bitArray[11], command=self.list_to_bin).grid(column=1, row=4,
                                                                                                  padx=3, pady=3)
        ttk.Checkbutton(self, text="Bit 12", width=6, variable=self.bitArray[12], command=self.list_to_bin).grid(column=1, row=5,
                                                                                                  padx=3, pady=3)
        ttk.Checkbutton(self, text="Bit 13", width=6, variable=self.bitArray[13], command=self.list_to_bin).grid(column=1, row=6,
                                                                                                  padx=3, pady=3)
        ttk.Checkbutton(self, text="Bit 14", width=6, variable=self.bitArray[14], command=self.list_to_bin).grid(column=1, row=7,
                                                                                                  padx=3, pady=3)
        ttk.Checkbutton(self, text="Bit 15", width=6, variable=self.bitArray[15], command=self.list_to_bin).grid(column=1, row=8,
                                                                                                  padx=3, pady=3)
        ttk.Checkbutton(self, text="Bit 16", width=6, variable=self.bitArray[16], command=self.list_to_bin).grid(column=2, row=1,
                                                                                                  padx=3, pady=3)
        ttk.Checkbutton(self, text="Bit 17", width=6, variable=self.bitArray[17], command=self.list_to_bin).grid(column=2, row=2,
                                                                                                  padx=3, pady=3)
        ttk.Checkbutton(self, text="Bit 18", width=6, variable=self.bitArray[18], command=self.list_to_bin).grid(column=2, row=3,
                                                                                                  padx=3, pady=3)
        ttk.Checkbutton(self, text="Bit 19", width=6, variable=self.bitArray[19], command=self.list_to_bin).grid(column=2, row=4,
                                                                                                  padx=3, pady=3)
        ttk.Checkbutton(self, text="Bit 20", width=6, variable=self.bitArray[20], command=self.list_to_bin).grid(column=2, row=5,
                                                                                                  padx=3, pady=3)
        ttk.Checkbutton(self, text="Bit 21", width=6, variable=self.bitArray[21], command=self.list_to_bin).grid(column=2, row=6,
                                                                                                  padx=3, pady=3)
        ttk.Checkbutton(self, text="Bit 22", width=6, variable=self.bitArray[22], command=self.list_to_bin).grid(column=2, row=7,
                                                                                                  padx=3, pady=3)
        ttk.Checkbutton(self, text="Bit 23", width=6, variable=self.bitArray[23], command=self.list_to_bin).grid(column=2, row=8,
                                                                                                  padx=3, pady=3)
        ttk.Checkbutton(self, text="Bit 24", width=6, variable=self.bitArray[24], command=self.list_to_bin).grid(column=3, row=1,
                                                                                                  padx=3, pady=3)
        ttk.Checkbutton(self, text="Bit 25", width=6, variable=self.bitArray[25], command=self.list_to_bin).grid(column=3, row=2,
                                                                                                  padx=3, pady=3)
        ttk.Checkbutton(self, text="Bit 26", width=6, variable=self.bitArray[26], command=self.list_to_bin).grid(column=3, row=3,
                                                                                                  padx=3, pady=3)
        ttk.Checkbutton(self, text="Bit 27", width=6, variable=self.bitArray[27], command=self.list_to_bin).grid(column=3, row=4,
                                                                                                  padx=3, pady=3)
        ttk.Checkbutton(self, text="Bit 28", width=6, variable=self.bitArray[28], command=self.list_to_bin).grid(column=3, row=5,
                                                                                                  padx=3, pady=3)
        ttk.Checkbutton(self, text="Bit 29", width=6, variable=self.bitArray[29], command=self.list_to_bin).grid(column=3, row=6,
                                                                                                  padx=3, pady=3)
        ttk.Checkbutton(self, text="Bit 30", width=6, variable=self.bitArray[30], command=self.list_to_bin).grid(column=3, row=7,
                                                                                                  padx=3, pady=3)
        ttk.Checkbutton(self, text="Bit 31", width=6, variable=self.bitArray[31], command=self.list_to_bin).grid(column=3, row=8,
                                                                                                  padx=3, pady=3)




App()