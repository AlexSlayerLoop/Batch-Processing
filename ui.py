from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from process import Process

TITLE_FONT = ("Verdana", 24)
FONT = ("Verdana", 12)
COLOR1 = "#183D3D"
COLOR2 = "#040D12"
COLOR3 = "#5C8374"
COLOR4 = "#93B1A6"

class SaveDataInterface:
    
    def __init__(self):
    
        self.window = Tk()
        self.window.title("Batch Processing")
        #self.window.geometry("500x500")
        self.window.config(bg=COLOR1, padx=20, pady=20)
        self.window.resizable(width=False, height=False)

        # Label title
        self.title = Label(self.window, text="New Process", font=TITLE_FONT, fg="white",  bg=COLOR2, 
                           highlightbackground="white", highlightthickness=3, width=20)
        self.title.grid(row=0, column=0, columnspan=3)
        
        # Label name
        self.name_label = Label(self.window, text="\nProgrammer's Name", font=FONT, fg="white", bg=COLOR1)
        self.name_label.grid(row=1, column=1)
        # Entry name
        self.name_entry = Entry(self.window, width=40, font=FONT)
        self.name_entry.grid(row=2, column=0, columnspan=3)
        
        # Label Number 1
        self.num1_label = Label(self.window, text="\nNumber 1", font=FONT, bg=COLOR1, fg="white")
        self.num1_label.grid(row=3, column=0)
        # Label operator 
        self.num2_label = Label(self.window, text="\nOperator", bg=COLOR1, fg="white", 
                                font=FONT)
        self.num2_label.grid(row=3, column=1)
        # Label number 2
        self.num2_label = Label(self.window, text="\nNumber 2", bg=COLOR1, fg="white", 
                                font=FONT)
        self.num2_label.grid(row=3, column=2)
        
        # entry num 1
        self.num1_entry = Entry(self.window, width=10, font=FONT)
        self.num1_entry.grid(row=4, column=0)
        # combo box operator
        self.combo_var = StringVar()
        self.combobox = ttk.Combobox(textvariable=self.combo_var, width=7, font=FONT)
        self.combobox['values'] = ('+', '-', '*', '/', '%')
        self.combobox.insert(0, '+')
        self.combobox.bind("<<ComboboxSelected>>") # insert command
        self.combobox.grid(row=4, column=1)
        # entry number 2 
        self.num2_entry = Entry(self.window, width=10, font=FONT)
        self.num2_entry.grid(row=4, column=2)
        
        # Label Max time 
        self.max_time_label = Label(self.window, text="\nMax Time (secs.)", font=FONT, bg=COLOR1, fg="white")
        self.max_time_label.grid(row=5, column=1)
        # entry Max time
        self.max_time_entry = Entry(self.window, width=40, font=FONT)
        self.max_time_entry.grid(row=6, column=0, columnspan=3)
        
        # Label ID
        self.id_label = Label(self.window, text="\nUnique ID", font=FONT, bg=COLOR1, fg="white")
        self.id_label.grid(row=7, column=1)
        # entry ID
        self.id_entry = Entry(self.window, width=40, font=FONT) 
        self.id_entry.grid(row=8, column=0, columnspan=3)
        
        # btn Save
        self.save_btn = Button(self.window, text="Save", font=("Verdana 15 bold"), height=2, width=8,
                                  bg=COLOR3, command=self.save)
        self.save_btn.grid(row=9, column=1, pady=15)
    
        #======================================== Second window ==========================================
        self.second_window = Toplevel(self.window)
        self.second_window.title("Process Viewer")
        self.second_window.geometry("600x500")
        # self.second_window.withdraw()
        
        #=================================== Data ========================================================
        
        
        
    
    def run(self):
        self.window.mainloop()
    
    
    def hide_main_window(self):
        self.window.withdraw() # Hide the main window

        
    
    def save(self):
        """validate and saves entries"""
        
        name = self.name_entry.get()
        operator = self.combobox.get()
        id = self.id_entry.get()
        
        try:
            num1 = int(self.num1_entry.get())
            num2 = int(self.num2_entry.get())
            max_time = int(self.max_time_entry.get())
            
        except ValueError:
            messagebox.showerror(title="Error", message="You must use numbers")
        
        else:
            
            if max_time < 1:
                messagebox.showerror(title="Error", message="(max time) must be greater than zero")
                
            elif (operator == '/' or operator == '%') and num2 == 0:
                messagebox.showerror(title="Error", message="You're trying division by zero")
                
            elif name == "" or id == "":
                messagebox.showerror(title="Error", message="Do not leave empty spaces")
                
            elif operator not in ('+', '-', '*', '/', '%'):
                messagebox.showerror(title="Error", message="You must use an operator")
            
            else:
                new_process = Process( name=name,
                                       operator=operator,
                                       max_time=max_time,
                                       num1=num1,
                                       num2=num2,
                                       id=id
                                     )
                d = new_process.get_dict()
                
                self.clear_entries()
                self.second_window.deiconify()
                self.hide_main_window()
    
    def create_process(self):
        pass
    
    
    def clear_entries(self):
        """clear all entries once you save a process"""
        
        self.name_entry.delete(0, 'end')
        self.num1_entry.delete(0, 'end')
        self.num2_entry.delete(0, 'end')
        self.max_time_entry.delete(0, 'end')
        self.id_entry.delete(0, 'end')
                
        