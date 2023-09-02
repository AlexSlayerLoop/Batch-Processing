import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from process import Process

TITLE_FONT = ("Verdana", 24)
FONT = ("Verdana", 12)
COLOR1 = "#183D3D"
COLOR2 = "#040D12"
COLOR3 = "#5C8374"
COLOR4 = "#93B1A6"

class ProcessInteface(tk.Tk):
    
    def __init__(self):
        super().__init__()
        
        # print(self.main_frame.winfo_class())
        self.style = ttk.Style()
        self.style.configure('TLabel', 
                             background=COLOR1, 
                             foreground="white",
                             font=FONT)
        self.style.configure("TFrame",
                             background=COLOR1)
        
        
        
        self.geometry("640x400")
        self.main_frame = ttk.Frame(self)
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        self.lbl_title = ttk.Label(self.main_frame, text="Process")
        self.lbl_title.grid(row=0, column=0)
        
        self.btn_add = ttk.Button(self.main_frame, text="Add", command=self.on_raise_form_button_clicked)
        self.btn_add.grid(row=0, column=1)
        

    
    def on_raise_form_button_clicked(self):
        raise_form = SaveDataInterface()

class SaveDataInterface(tk.Toplevel):
    
    def __init__(self):
        super().__init__()
        
        # self.geometry("600x400")
        
        self.main_frame = ttk.Frame(self, padding=10, style='TFrame')
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        # self.window.title("Batch Processing")
        # self.window.config(bg=COLOR1, padx=20, pady=20)
        self.resizable(width=False, height=False)

        # Label title
        self.lbl_title = ttk.Label(self.main_frame, text="New Process", font=TITLE_FONT, foreground="white",  background=COLOR2, width=20)
        self.lbl_title.grid(row=0, column=0, columnspan=3)
        
        # Label name
        self.name_label = ttk.Label(self.main_frame, text="Name")
        self.name_label.grid(row=1, column=1)
        # Entry name
        self.name_entry = ttk.Entry(self.main_frame, width=35, font=FONT)
        self.name_entry.grid(row=2, column=0, columnspan=3)
        
        # Label Number 1
        self.lbl_num1 = ttk.Label(self.main_frame, text="\nNumber 1")
        # Label operator 
        self.lbl_operator = ttk.Label(self.main_frame, text="\nOperator")
        # Label number 2
        self.lbl_num2 = ttk.Label(self.main_frame, text="\nNumber 2")
        # grid Labels
        self.lbl_num1.grid(row=3, column=0)
        self.lbl_operator.grid(row=3, column=1)
        self.lbl_num2.grid(row=3, column=2)
        
        # entry num 1
        self.num1_entry = ttk.Entry(self.main_frame, width=9, font=FONT)
        self.num1_entry.grid(row=4, column=0)
        # combo box operator
        self.combo_var = tk.StringVar()
        self.combobox = ttk.Combobox(self.main_frame, textvariable=self.combo_var,width=7, font=FONT)
        self.combobox['values'] = ('+', '-', '*', '/', '%')
        self.combobox.insert(0, '+')
        #self.combobox.bind("<<ComboboxSelected>>") # insert command
        self.combobox.grid(row=4, column=1)
        # entry number 2 
        self.num2_entry = ttk.Entry(self.main_frame, width=9, font=FONT)
        self.num2_entry.grid(row=4, column=2)
        
        # Label Max time 
        self.max_time_label = ttk.Label(self.main_frame, text="\nMax Time\n(secs.)")
        self.max_time_label.grid(row=5, column=1)
        # entry Max time
        self.max_time_entry = ttk.Entry(self.main_frame, width=35, font=FONT)
        self.max_time_entry.grid(row=6, column=0, columnspan=3)
        
        # Label ID
        self.id_label = ttk.Label(self.main_frame, text="\nUnique ID")
        self.id_label.grid(row=7, column=1)
        # entry ID
        self.id_entry = ttk.Entry(self.main_frame, width=35, font=FONT) 
        self.id_entry.grid(row=8, column=0, columnspan=3)
        
        # btn Save
        self.save_btn = ttk.Button(self.main_frame, text="Save", command=self.on_save_button_clicked)
        self.save_btn.grid(row=9, column=1, pady=15)
    
        # self.withdraw() # ocular ventana 
        # self.deiconify() # mostrar ventana
        
    
    def hide_main_window(self):
        self.withdraw() # Hide the main window
        

    def create_process(self):
        pass
        # new_process = Process( name=name,
                #                        operator=operator,
                #                        max_time=max_time,
                #                        num1=num1,
                #                        num2=num2,
                #                        id=id
                #                      )
                # d = new_process.get_dict()
                # print(d)
                
    def on_save_button_clicked(self):
        
        result = self.validate_data()
        if result:
            #TODO create Process
            print("<Create Process>")
            self.clear_entries()


    def validate_data(self): 
        """Validate all fields to move forward"""
        name = self.name_entry.get()
        operator = self.combo_var.get()
        id = self.id_entry.get()
        
        try:
            num1 = int(self.num1_entry.get())
            num2 = int(self.num2_entry.get())
            max_time = int(self.max_time_entry.get())
            
        except ValueError:
            messagebox.showerror(title="Error", message="You must use numbers")
            return False
        
        else:
            
            if max_time < 1:
                messagebox.showerror(title="Error", message="(max time) must be greater than zero")
                return False
            elif (operator == '/' or operator == '%') and num2 == 0:
                messagebox.showerror(title="Error", message="You're trying division by zero")
                return False
            elif name == "" or id == "":
                messagebox.showerror(title="Error", message="Do not leave empty spaces")
                return False
            elif operator not in ('+', '-', '*', '/', '%'):
                messagebox.showerror(title="Error", message="You must use an operator")
                return False
            #TODO add validation to verify unique ID
            
            else:
                return True
                
    
    def create_process(self):
        pass
    
    
    def clear_entries(self):
        """clear all entries once you save a process"""
        
        self.name_entry.delete(0, 'end')
        self.num1_entry.delete(0, 'end')
        self.num2_entry.delete(0, 'end')
        self.max_time_entry.delete(0, 'end')
        self.id_entry.delete(0, 'end')
                


        
        
if __name__ == "__main__":
    window = ProcessInteface()
    window.mainloop()