from tkinter import *
from tkinter import ttk
import time

TITLE_FONT = ("Verdana", 24)
FONT = ("Verdana", 12)
COLOR1 = "#191D88"
COLOR2 = "#1450A3"

class BatchInterface:
    
    def __init__(self):
    
        self.window = Tk()
        self.window.title("Batch Processing")
        # self.window.geometry("500x400")
        self.window.config(bg=COLOR1, padx=20, pady=20)
        # self.window.resizable(width=False, height=False)

        # Label title
        self.title = Label(text="New Process", font=TITLE_FONT, fg="white",  bg=COLOR2, 
                           highlightbackground="white", highlightthickness=3, width=20)
        self.title.grid(row=0, column=0, columnspan=3)
        
        # Label name
        self.name_label = Label(text="\nProgrammer's Name", font=FONT, fg="white", bg=COLOR1)
        self.name_label.grid(row=1, column=1)
        
        # Entry name
        self.name_entry = Entry(width=40, font=FONT)
        self.name_entry.grid(row=2, column=0, columnspan=3)
        
        # Label Numero 1 |  Operation  | Numero 2
        self.num1_label = Label(text="\nNumber 1", font=FONT, bg=COLOR1, fg="white")
        self.num1_label.grid(row=3, column=0)
        
        self.num2_label = Label(self.window, text="\nOperator", bg=COLOR1, fg="white", 
                                font=FONT)
        self.num2_label.grid(row=3, column=1)
        
        self.num3_label = Label(self.window, text="\nNumber 2", bg=COLOR1, fg="white", 
                                font=FONT)
        self.num3_label.grid(row=3, column=2)
        
        # entry num 1
        self.num1_entry = Entry(width=10, font=FONT)
        self.num1_entry.grid(row=4, column=0)
        
        # combo box
        self.combo_var = StringVar()
        self.combobox = ttk.Combobox(textvariable=self.combo_var, width=7, font=FONT)
        self.combobox['values'] = ('+', '-', '*', '/', '%')
        self.combobox.bind("<<ComboboxSelected>>") # insert command
        self.combobox.grid(row=4, column=1)
        
        # entry number 2 
        self.num3_entry = Entry(width=10, font=FONT)
        self.num3_entry.grid(row=4, column=2)
        
        # Label Max time 
        self.max_time_label = Label(text="\nMax Time", font=FONT, bg=COLOR1, fg="white")
        self.max_time_label.grid(row=5, column=1)
        # entry Max time
        self.max_time_entry = Entry(width=40, font=FONT)
        self.max_time_entry.grid(row=6, column=0, columnspan=3)
        
        # Label ID
        self.id_label = Label(text="\nUnique ID", font=FONT, bg=COLOR1, fg="white")
        self.id_label.grid(row=7, column=1)
        # entry ID
        self.id_entry = Entry(width=40, font=FONT) 
        self.id_entry.grid(row=8, column=0, columnspan=3)
        
        # Button Save
        self.save_button = Button(text="Save", font=("Verdana 15 bold"), height=2, width=8)
        self.save_button.grid(row=9, column=1, pady=15)
        
        self.window.mainloop()