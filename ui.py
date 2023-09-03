import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from process import Process

TITLE_FONT = ("Verdana", 18)
FONT = ("Verdana", 12)
COLOR1 = "#183D3D"
COLOR2 = "#040D12"
COLOR3 = "#5C8374"
COLOR4 = "#93B1A6"

class ProcessInteface(tk.Tk):
    
    def __init__(self):
        super().__init__()
        
        self.process = Process()
        print(self.process)
        
        self.geometry("640x400")
        
        self.style = ttk.Style()
        self.style.configure('TLabel', background=COLOR1, foreground="white", font=FONT)
        self.style.configure("TFrame", background=COLOR1)

        
        self.layout_frame = ttk.Frame(self, padding=10)
        self.layout_frame.pack(fill=tk.BOTH, expand=True)
        
        
        # Left widgets
        self.lbl_title = ttk.Label(self.layout_frame, text="Batch Processing")
        self.btn_add_process = ttk.Button(self.layout_frame, 
                                          text="Add", 
                                          command=self.on_raise_form_button_clicked)
        self.treeview_process = ttk.Treeview(self.layout_frame)
        

        
        
        self.lbl_title.grid(row=0, column=0)
        self.btn_add_process.grid(row=1, column=0, pady=20, sticky='we')
        self.treeview_process.grid(row=2, column=0)
        
        
        # self.withdraw() # ocular ventana 
        # self.deiconify() # mostrar ventana
        
    
    def on_raise_form_button_clicked(self):
        raise_form = SaveDataInterface(self.process)

class SaveDataInterface(tk.Toplevel):
    
    def __init__(self, object_process):
        super().__init__()
        
        # inherits the Process object
        self.process: Process = object_process
        
        self.title("Form")
        self.main_frame = ttk.Frame(self, padding=10)
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        self.resizable(width=False, height=False)

        # Label title
        self.lbl_title = ttk.Label(self.main_frame, text="New Process", font=TITLE_FONT, foreground="white",  background=COLOR2, width=20)
        self.lbl_title.grid(row=0, column=0, columnspan=3)
        
        # Label name
        self.name_label = ttk.Label(self.main_frame, text="Name")
        # Entry name
        self.name_entry = ttk.Entry(self.main_frame, width=35, font=FONT)
        # grid name wigets
        self.name_entry.grid(row=2, column=0, columnspan=3)
        self.name_label.grid(row=1, column=1)
        
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
        #self.combobox.bind("<<ComboboxSelected>>" ) # insert command
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
        
        self.transient(self.master) # to inherit parent behavior
        self.grab_set() # pause paret window while secondary window works
        self.wait_window(self) 
        

    def create_process(self):
        """add a new process to the list"""
        
        name = self.name_entry.get()
        operator = self.combo_var.get()
        id = self.id_entry.get()
        
        num1 = int(self.num1_entry.get())
        num2 = int(self.num2_entry.get())
        max_time = int(self.max_time_entry.get())
        
        result = self.process.operation_result(operator, num1, num2)
        
        self.process.add_process(
                                    id=id,
                                    name=name, 
                                    operator=operator, 
                                    max_time=max_time, 
                                    num1=num1, 
                                    num2=num2, 
                                    result=result
                                )
         
                
    def on_save_button_clicked(self):
        """Validate information and if is correct calls create_process method"""
        
        result = self.validate_data()
        if result:
            self.create_process()
            #TODO show a message window
            self.destroy()


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
            elif self.process.is_unique(id):
                messagebox.showerror(title="Error", message="This id already exists")
            
            else:
                return True
                

if __name__ == "__main__":
    window = ProcessInteface()
    window.mainloop()