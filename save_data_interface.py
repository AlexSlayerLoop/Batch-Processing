import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from process import Process

TITLE_FONT = ("Verdana", 18)
FONT = ("Verdana", 12)
COLOR1 = "#61677A"
COLOR2 = "#272829"
COLOR3 = "#5C8374"
COLOR4 = "#93B1A6"


class SaveDataInterface(tk.Toplevel):
    
    def __init__(self, master, object_process):
        super().__init__(master)
        # inherits the Process object
        self.process: Process = object_process

        # Set main_frame config
        self.title("Form")
        self.main_frame = ttk.Frame(self, padding=10)
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        self.resizable(width=False, height=False)

        # Labels
        self.lbl_title = ttk.Label(self.main_frame,
                                   text="New Process",
                                   font=TITLE_FONT,
                                   foreground="white",
                                   background=COLOR2,
                                   width=20,
                                   padding=5)
        self.lbl_name = ttk.Label(self.main_frame, text="Name")
        self.lbl_num1 = ttk.Label(self.main_frame, text="\nNumber 1")
        self.lbl_operator = ttk.Label(self.main_frame, text="\nOperator")
        self.lbl_num2 = ttk.Label(self.main_frame, text="\nNumber 2")
        self.lbl_max_time = ttk.Label(self.main_frame, text="\nMax Time\n(secs.)")
        self.lbl_id = ttk.Label(self.main_frame, text="\nUnique ID")

        # grid Labels
        self.lbl_title.grid(row=0, column=0, columnspan=3)
        self.lbl_name.grid(row=1, column=1)
        self.lbl_num1.grid(row=3, column=0)
        self.lbl_operator.grid(row=3, column=1)
        self.lbl_num2.grid(row=3, column=2)
        self.lbl_max_time.grid(row=5, column=1)
        self.lbl_id.grid(row=7, column=1)

        # entries
        self.name_entry = ttk.Entry(self.main_frame, width=30, font=FONT)
        self.num1_entry = ttk.Entry(self.main_frame, width=9, font=FONT)
        self.num2_entry = ttk.Entry(self.main_frame, width=9, font=FONT)
        self.max_time_entry = ttk.Entry(self.main_frame, width=30, font=FONT)
        self.id_entry = ttk.Entry(self.main_frame, width=30, font=FONT)

        # grid entries
        self.name_entry.grid(row=2, column=0, columnspan=3)
        self.num1_entry.grid(row=4, column=0)
        self.num2_entry.grid(row=4, column=2)
        self.max_time_entry.grid(row=6, column=0, columnspan=3)
        self.id_entry.grid(row=8, column=0, columnspan=3)

        # Buttons
        self.save_btn = ttk.Button(self.main_frame, text="Save", command=self.on_save_button_clicked)
        # grid button
        self.save_btn.grid(row=9, column=1, pady=15)

        # combo box
        self.combo_var = tk.StringVar()
        self.combobox = ttk.Combobox(self.main_frame, textvariable=self.combo_var, width=7, font=FONT)
        self.combobox['values'] = ('+', '-', '*', '/', '%')
        self.combobox.insert(0, '+')
        self.combobox.grid(row=4, column=1)

        # window settings
        self.transient(self.master)  # to inherit parent behavior
        self.grab_set()              # pause parent window while secondary window works
        self.wait_window(self)       # wait main window while secondary is working
        
    def create_process(self):
        """add a new process to the list"""
        name = self.name_entry.get()
        operator = self.combo_var.get()
        p_id = self.id_entry.get()
        
        num1 = int(self.num1_entry.get())
        num2 = int(self.num2_entry.get())
        max_time = int(self.max_time_entry.get())
        result = self.process.operation_result(operator, num1, num2)
        
        self.process.add_process(
                                    id=p_id,
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
            messagebox.showinfo(title="Form", message="Process successfully added to the queue")
            self.destroy()

    def validate_data(self) -> bool: 
        """Validate all fields to move forward"""
        name = self.name_entry.get()
        operator = self.combo_var.get()
        new_id = self.id_entry.get()
        
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
            elif name == "" or new_id == "":
                messagebox.showerror(title="Error", message="Do not leave empty spaces")
                return False
            elif operator not in ('+', '-', '*', '/', '%'):
                messagebox.showerror(title="Error", message="You must use an operator")
                return False
            elif not self.process.is_unique(new_id):
                messagebox.showerror(title="Error", message="This id already exists")
                return False
            else:
                return True
