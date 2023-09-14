import tkinter as tk
from tkinter import ttk
from process import Process
from threading import Thread
from threading import Event
from time import sleep
from tkinter import messagebox

TITLE_FONT = ("Verdana", 18)
FONT = ("Verdana", 13)
COLOR1 = "#61677A"
COLOR2 = "#272829"
COLOR3 = "#5C8374"
COLOR4 = "#93B1A6"

class ProcessInterface(tk.Tk):

    def __init__(self):
        super().__init__()
        # instantiate Process
        self.process = Process()

        # window background
        self.config(background=COLOR1)
        self.resizable(width=False, height=False)
    
        # Styling widgets
        self.style = ttk.Style() 
        self.style.configure('TLabel', background=COLOR1, foreground="white", font=FONT)
        self.style.configure('Title.TLabel', background=COLOR1, foreground="white", font=TITLE_FONT)
        self.style.configure("TFrame", background=COLOR1)
        self.style.configure("TButton", font=FONT)
        
        # Threads
        self.thread1 = Thread(target=self.init_main_timer, daemon=True)
        self.thread2 = Thread(target=self.execute_process, daemon=True)
        
        # self.pause_flag = Event()
        # self.pause_flag.set()
        
        # # Event Bindings
        # self.bind("<p>", self.on_pause_released)
        # self.bind("<c>", self.on_continue_released)

        # Frames
        self.layout_frame = ttk.Frame(self, padding=10)
        self.layout2_frame = ttk.Frame(self,  padding=10)
        self.layout3_frame = ttk.Frame(self, padding=10)

        # Grid Frames
        self.layout_frame.grid(row=0, column=0, sticky='n')
        self.layout2_frame.grid(row=0, column=1, sticky='n', padx=40)
        self.layout3_frame.grid(row=0, column=2, sticky='n')
        
        # ===============  Frame 1  ==================== #
        # Labels
        self.lbl_title = ttk.Label(self.layout_frame, text="Batch Processing", style='Title.TLabel')
        self.lbl_num_processes = ttk.Label(self.layout_frame, text="Number of Processes")
        self.lbl_pending_batches = ttk.Label(self.layout_frame, text="Pending Batches: 0")
        
        # Buttons
        self.btn_add_process = ttk.Button(self.layout_frame, text="Add", command=self.on_create_processes_button_clicked)
        
        # Entries
        self.quantity_entry = tk.Entry(self.layout_frame, width=30)

        # Treeview widget
        self.column_values = ("max_time", )
        self.treeview_1 = ttk.Treeview(self.layout_frame)
        self.treeview_1.configure(columns=self.column_values)
        # add column names 
        self.treeview_1.heading("#0", text="ID")
        self.treeview_1.heading("max_time", text="Max Time") 
        # use column method to modify the width
        self.treeview_1.column("#0", width=80)
        self.treeview_1.column("max_time", width=80)

        # grid Frame1 widgets
        self.lbl_title.pack()
        self.lbl_num_processes.pack(pady=(20, 0))
        self.quantity_entry.pack()
        self.btn_add_process.pack(pady=10)
        self.treeview_1.pack()
        self.lbl_pending_batches.pack(pady=(15, 0))

        # ===============  Frame 2  ==================== #
        self.lbl_current_process = ttk.Label(self.layout2_frame, text="Current Process", style='Title.TLabel') 
        self.lbl_operation = ttk.Label(self.layout2_frame, text=f"Operation : ...")
        self.lbl_max_time = ttk.Label(self.layout2_frame, text=f"Max Time : ")
        self.lbl_id = ttk.Label(self.layout2_frame, text=f"ID : ...")
        # progressbar 
        self.progressbar = ttk.Progressbar(self.layout2_frame, mode="determinate", length=180)
        self.lbl_timer = ttk.Label(self.layout2_frame,
                                   text="00:00:00",
                                   font=("Verdana", 20, "bold"),
                                   background="white",
                                   foreground="black")
        self.time_elapsed = tk.IntVar()

        # grid Frame 2 widgets
        self.lbl_current_process.pack(pady=(0, 50))
        self.lbl_operation.pack(anchor="w", pady=20)
        self.lbl_max_time.pack(anchor="w", pady=20)
        self.lbl_id.pack(anchor="w", pady=20)
        self.progressbar.pack(pady=20)
        self.lbl_timer.pack()
        
        # ===============  Frame 3  ==================== #
        self.lbl_completed_processes = ttk.Label(self.layout3_frame, text="Completed Processes", style='Title.TLabel')
        # create a treeview widget
        self.column_values_2 = ("operation", "result")
        self.treeview_2 = ttk.Treeview(self.layout3_frame, columns=self.column_values_2)
        # add column names
        self.treeview_2.heading("#0", text="Id")
        self.treeview_2.heading("operation", text="Operation")
        self.treeview_2.heading("result", text="Result")
        # config columns 
        self.treeview_2.column("#0", width=80)
        self.treeview_2.column("operation", width=80)
        self.treeview_2.column("result", width=80)
        
        # buttons
        self.btn_play = ttk.Button(self.layout3_frame, text="Play", command=self.on_play_button_clicked)

        # grid Frame 3 widgets
        self.lbl_completed_processes.pack()
        self.treeview_2.pack(pady=40)
        self.btn_play.pack()
    
    # def on_pause_released(self, event):
    #     self.pause_flag.clear()
        
    # def on_continue_released(self, event):
    #     self.pause_flag.set()

    def on_play_button_clicked(self): 
        # disable buttons
        self.btn_play.config(state=tk.DISABLED)
        self.btn_add_process.config(state=tk.DISABLED)
        
        # initialize main timer
        self.thread1.start()
        
        # while not self.process.is_empty():
        self.thread2.start()
        
    def execute_process(self):
        """Ejecutar un proceso a la vez"""
        # revisa que aun haya procesos
        if len(self.process.processes) > 0:
            # prints for debug purposes
            print("\nbatch list:", self.process.batch)
            print("process list:", self.process.processes)
            # verifica si batch esta no esta vacío
            if len(self.process.batch[0]) > 0:
                process = self.process.get_first_process()
                # actualiza labels
                self.update_process_labels(process)
                # start progressbar
                self.start_progressbar(process['max_time'])
                # update treeview rows
                self.update_treeview_rows()
                # delete last process
                self.process.delete_first_process()
            else:
                del self.process.batch[0]
            
            self.execute_process()
        else:
            self.lbl_pending_batches.config(text=f"Pending Batches: {self.process.get_batch_len()}")
            if len(self.treeview_1.get_children()) > 0:
                self.clear_treeview_items()
        
    def start_progressbar(self, time):
        for sec in range(100):
                # if self.pause_flag.is_set():
                sleep(time / 100)
                self.progressbar['value'] = sec
                self.update_idletasks()
            #     else:
            #         while not self.pause_flag.is_set():
            #             sleep(1)
            # self.progressbar['value'] = 0

    def update_treeview_rows(self):
        """insert in treeview_2 and delete from treeview_1"""
        self.insert_on_treeview_2()
        if len(self.treeview_1.get_children()) > 0:
            selected_item = self.treeview_1.get_children()[0]
            self.treeview_1.delete(selected_item)

    def insert_on_treeview_2(self):
        """insert a process in treeview_2"""
        # get information from the process to insert into treeview2
        item_to_insert = self.process.get_first_process()
        operation = f"{item_to_insert['num1']} {item_to_insert['operator']} " \
                    f"{item_to_insert['num2']}"
                    
        self.treeview_2.insert(
                               parent="",
                               index=tk.END,
                               text=item_to_insert["id"],
                               values=(operation, item_to_insert["result"])
                              )
                
    def update_process_labels(self, process):
        
        operation = f"{process['num1']} {process['operator']} {process['num2']} = {process['result']:.2f}"
        
        self.lbl_operation.config(text=f"Operation: {operation}")
        self.lbl_max_time.config(text=f"Max Time: {process['max_time']}") 
        self.lbl_id.config(text=f"ID: {process['id']}")
        self.lbl_pending_batches.config(text=f"Pending Batches: {self.process.get_batch_len()}")

    def init_main_timer(self):
            if not self.process.is_empty():
                seconds = self.time_elapsed.get()
                hours = seconds // 3600
                minutes = (seconds % 3600) // 60
                seconds = seconds % 60
                self.lbl_timer.config(text=f"{hours:02d}:{minutes:02d}:{seconds:02d}")
                self.after(1000, self.init_main_timer)
                self.time_elapsed.set(self.time_elapsed.get() + 1)
    
    def on_create_processes_button_clicked(self):
        """Create the number of processes given"""
        try:
            num_of_processes = int(self.quantity_entry.get())
        except ValueError:
            messagebox.showerror(title="Error", message="You must use integers numbers")
        else:
            if num_of_processes > 0:
                self.process.generate_process(num_of_processes)
                self.process.split_in_batches()
                
                for item in self.process.processes:
                    self.insert_on_treeview(item)
                
            
    def insert_on_treeview(self, item):
        """insert a new row in treeview every time a new process is added"""
        self.treeview_1.insert(parent="", index=tk.END, text=item["id"], values=(item["max_time"], ))
        #update batch Label
        self.lbl_pending_batches.config(text=f"Pending Batches: {self.process.get_batch_len()}")
            
    def clear_treeview_items(self):
        """clear all items from treeview"""
        self.treeview_1.delete(*self.treeview_1.get_children())
        



if __name__ == "__main__":
    window = ProcessInterface()
    window.mainloop()
