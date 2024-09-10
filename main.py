from tkinter import *
#Initialize Tkinter Instance
root = Tk()
root.title("Binary Calculator")
root.geometry("370x300+250+250")
root.resizable(False, False)
frm = Frame(root)
frm.grid()
#Initialize Tkinter Variables as Base Variables
txt = StringVar()
bitArray = [BooleanVar(),BooleanVar(),BooleanVar(),BooleanVar(),BooleanVar(),BooleanVar(),BooleanVar(),BooleanVar(),BooleanVar(),BooleanVar(),BooleanVar(),BooleanVar(),BooleanVar(),BooleanVar(),BooleanVar(),BooleanVar(),BooleanVar(),BooleanVar(),BooleanVar(),BooleanVar(),BooleanVar(),BooleanVar(),BooleanVar(),BooleanVar(),BooleanVar(),BooleanVar(),BooleanVar(),BooleanVar(),BooleanVar(),BooleanVar(),BooleanVar(),BooleanVar()]
#Initialize base functions for working on Bit Array
#list_to_bin : convert bitArray boolean array to decimal than write decimal value to textbox
def list_to_bin():
    dec = 0
    for i in range(0,len(bitArray)):
        if bitArray[i].get():
            dec += 1<<i
    txt.set(str(dec))

#dec_to_bin_list: convert textbox value decimal than binary, populate binary value to bit array bit by bit as boolean value
def dec_to_bin_list():
    if not(txt.get().isnumeric()) or int(txt.get()) > 4294967295:
        txt.set("4294967295")
    bin_val = bin(int(txt.get()))[2:]
    for ind, val in enumerate(bin_val[::-1]):
        if val == "1":
            bitArray[ind].set(True)
        else:
            bitArray[ind].set(False)

#clear_all: clear textbox and checkboxes via setting all values False in bit array
def clear_all():
   for i in bitArray:
       i.set(False)
   txt.set("0")

#Add components
#components spread across 4 column
#text box spanned 2 columns ( 0 and 1 )
entry_box = Entry(frm, textvariable=txt)
entry_box.grid(column=0, row=0, columnspan=2,padx = 3, pady = 10)
#buttons start from column 2
#Convert button invoke dec_to_bin_list function
Button(frm, text="Convert", command=dec_to_bin_list).grid(column=2, row=0,padx = 3, pady = 10)
#Clear button invoke clear_all function
Button(frm, text="Clear", command=clear_all).grid(column=3, row=0,padx = 3, pady = 10)
#32 Check button added to the grid, each checkbux value attached to bit Array and click event command list_to_bin invoked
Checkbutton(frm, text="Bit 0", width=6, variable=bitArray[0], command=list_to_bin).grid(column=0, row=1, padx=3, pady=3)
Checkbutton(frm, text="Bit 1", width=6, variable=bitArray[1], command=list_to_bin).grid(column=0, row=2, padx=3, pady=3)
Checkbutton(frm, text="Bit 2", width=6, variable=bitArray[2], command=list_to_bin).grid(column=0, row=3, padx=3, pady=3)
Checkbutton(frm, text="Bit 3", width=6, variable=bitArray[3], command=list_to_bin).grid(column=0, row=4, padx=3, pady=3)
Checkbutton(frm, text="Bit 4", width=6, variable=bitArray[4], command=list_to_bin).grid(column=0, row=5, padx=3, pady=3)
Checkbutton(frm, text="Bit 5", width=6, variable=bitArray[5], command=list_to_bin).grid(column=0, row=6, padx=3, pady=3)
Checkbutton(frm, text="Bit 6", width=6, variable=bitArray[6], command=list_to_bin).grid(column=0, row=7, padx=3, pady=3)
Checkbutton(frm, text="Bit 7", width=6, variable=bitArray[7], command=list_to_bin).grid(column=0, row=8, padx=3, pady=3)
Checkbutton(frm, text="Bit 8", width=6, variable=bitArray[8], command=list_to_bin).grid(column=1, row=1, padx=3, pady=3)
Checkbutton(frm, text="Bit 9", width=6, variable=bitArray[9], command=list_to_bin).grid(column=1, row=2, padx=3, pady=3)
Checkbutton(frm, text="Bit 10", width=6, variable=bitArray[10], command=list_to_bin).grid(column=1, row=3, padx=3, pady=3)
Checkbutton(frm, text="Bit 11", width=6, variable=bitArray[11], command=list_to_bin).grid(column=1, row=4, padx=3, pady=3)
Checkbutton(frm, text="Bit 12", width=6, variable=bitArray[12], command=list_to_bin).grid(column=1, row=5, padx=3, pady=3)
Checkbutton(frm, text="Bit 13", width=6, variable=bitArray[13], command=list_to_bin).grid(column=1, row=6, padx=3, pady=3)
Checkbutton(frm, text="Bit 14", width=6, variable=bitArray[14], command=list_to_bin).grid(column=1, row=7, padx=3, pady=3)
Checkbutton(frm, text="Bit 15", width=6, variable=bitArray[15], command=list_to_bin).grid(column=1, row=8, padx=3, pady=3)
Checkbutton(frm, text="Bit 16", width=6, variable=bitArray[16], command=list_to_bin).grid(column=2, row=1, padx=3, pady=3)
Checkbutton(frm, text="Bit 17", width=6, variable=bitArray[17], command=list_to_bin).grid(column=2, row=2, padx=3, pady=3)
Checkbutton(frm, text="Bit 18", width=6, variable=bitArray[18], command=list_to_bin).grid(column=2, row=3, padx=3, pady=3)
Checkbutton(frm, text="Bit 19", width=6, variable=bitArray[19], command=list_to_bin).grid(column=2, row=4, padx=3, pady=3)
Checkbutton(frm, text="Bit 20", width=6, variable=bitArray[20], command=list_to_bin).grid(column=2, row=5, padx=3, pady=3)
Checkbutton(frm, text="Bit 21", width=6, variable=bitArray[21], command=list_to_bin).grid(column=2, row=6, padx=3, pady=3)
Checkbutton(frm, text="Bit 22", width=6, variable=bitArray[22], command=list_to_bin).grid(column=2, row=7, padx=3, pady=3)
Checkbutton(frm, text="Bit 23", width=6, variable=bitArray[23], command=list_to_bin).grid(column=2, row=8, padx=3, pady=3)
Checkbutton(frm, text="Bit 24", width=6, variable=bitArray[24], command=list_to_bin).grid(column=3, row=1, padx=3, pady=3)
Checkbutton(frm, text="Bit 25", width=6, variable=bitArray[25], command=list_to_bin).grid(column=3, row=2, padx=3, pady=3)
Checkbutton(frm, text="Bit 26", width=6, variable=bitArray[26], command=list_to_bin).grid(column=3, row=3, padx=3, pady=3)
Checkbutton(frm, text="Bit 27", width=6, variable=bitArray[27], command=list_to_bin).grid(column=3, row=4, padx=3, pady=3)
Checkbutton(frm, text="Bit 28", width=6, variable=bitArray[28], command=list_to_bin).grid(column=3, row=5, padx=3, pady=3)
Checkbutton(frm, text="Bit 29", width=6, variable=bitArray[29], command=list_to_bin).grid(column=3, row=6, padx=3, pady=3)
Checkbutton(frm, text="Bit 30", width=6, variable=bitArray[30], command=list_to_bin).grid(column=3, row=7, padx=3, pady=3)
Checkbutton(frm, text="Bit 31", width=6, variable=bitArray[31], command=list_to_bin).grid(column=3, row=8, padx=3, pady=3)
#Pack up root instance and start software.
root.mainloop()