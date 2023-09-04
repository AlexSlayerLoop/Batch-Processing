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
        
        # Label title 
        self.lbl_title = ttk.Label(self.layout_frame, text="Batch Processing")
        # Button add
        self.btn_add_process = ttk.Button(self.layout_frame, 
                                          text="Add", 
                                          command=self.on_raise_form_button_clicked)
        # Treeview widget
        self.column_values = ("max_time")
        self.treeview_process = ttk.Treeview(self.layout_frame)
        self.treeview_process.configure(columns=self.column_values)
        # add column names 
        self.treeview_process.heading("#0", text="ID")
        self.treeview_process.heading("max_time", text="Max Time") 
        # use column method to modify the width
        self.treeview_process.column("#0", width=80)
        self.treeview_process.column("max_time", width=80)
        
        
        
        # Label batch pending
        self.lbl_pending_batches = ttk.Label(self.layout_frame, text="Pending Batches: 0")
        
        self.lbl_title.grid(row=0, column=0)
        self.btn_add_process.grid(row=1, column=0, pady=20, sticky='we')
        self.treeview_process.grid(row=2, column=0)
        self.lbl_pending_batches.grid(row=3, column=0, pady=(15, 0))
        
        
    def on_raise_form_button_clicked(self):
        # raise a Form with the fiels to create a new process
        raise_form = SaveDataInterface(self, object_process=self.process)
        
        # insert the new brand process in the treeview widget
        self.insert_on_treeview()
        
        # if batch_size is not specified wil be 5
        self.process.separate_in_batches()
        
        # clear treeview every time batch increments
        self.clear_treeview_items()
    
    
    def update_lbl_pending_batches(self):
        self.lbl_pending_batches.config(text=f"Pending Batches: {self.process.get_batch_len()}")
        
    
    def clear_treeview_items(self):
        
        items_displayed = len(self.treeview_process.get_children())
        if items_displayed == 5:
            # Delete all items in the treeview
            self.treeview_process.delete(*self.treeview_process.get_children())
            self.update_lbl_pending_batches()
            
    
    def insert_on_treeview(self):
        
        item_dict = self.process.get_last_process_added()
        id = item_dict['id']
        max_time = item_dict['max_time']
        self.treeview_process.insert(parent="",
                                     index=tk.END,
                                     text=id,
                                     values=(max_time, ))

    
if __name__ == '__main__':
    window = ProcessInteface()
    window.mainloop()


