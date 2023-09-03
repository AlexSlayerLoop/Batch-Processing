import tkinter as tk
from tkinter import ttk
from process import Process
from save_data_interface import SaveDataInterface, FONT, COLOR1


class ProcessInteface(tk.Tk):
    
    def __init__(self):
        super().__init__()
        
        self.process = Process()
        
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


