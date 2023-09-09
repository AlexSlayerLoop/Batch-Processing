import tkinter as tk
from tkinter import ttk
from process import Process
from save_data_interface import SaveDataInterface, FONT, COLOR1
from threading import Thread
from time import sleep


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
        self.style.configure("TFrame", background=COLOR1)

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
        self.lbl_title = ttk.Label(self.layout_frame, text="Batch Processing")
        self.lbl_pending_batches = ttk.Label(self.layout_frame, text="Pending Batches: 0")
        
        # Buttons
        self.btn_add_process = ttk.Button(self.layout_frame, text="Add", command=self.on_raise_form_button_clicked)

        # Treeview widget
        self.column_values = ("max_time", )
        self.treeview_process = ttk.Treeview(self.layout_frame)
        self.treeview_process.configure(columns=self.column_values)
        # add column names 
        self.treeview_process.heading("#0", text="ID")
        self.treeview_process.heading("max_time", text="Max Time") 
        # use column method to modify the width
        self.treeview_process.column("#0", width=80)
        self.treeview_process.column("max_time", width=80)

        # grid Frame1 widgets
        self.lbl_title.pack()
        self.btn_add_process.pack(pady=20, fill='x')
        self.treeview_process.pack()
        self.lbl_pending_batches.pack(pady=(15, 0))

        # ===============  Frame 2  ==================== #
        self.lbl_current_process = ttk.Label(self.layout2_frame, text="Current Process") 
        self.lbl_name = ttk.Label(self.layout2_frame, text=f"Name : ...")
        self.lbl_operation = ttk.Label(self.layout2_frame, text=f"Operation : ...")
        self.lbl_max_time = ttk.Label(self.layout2_frame, text=f"Max Time : ")
        self.lbl_id = ttk.Label(self.layout2_frame, text=f"ID : ...")
        # progressbar 
        self.progressbar = ttk.Progressbar(self.layout2_frame, mode="determinate", length=180)
        self.lbl_timer = ttk.Label(self.layout2_frame,
                                   text="00:00:00",
                                   font=("Verdana", 20),
                                   background="white",
                                   foreground="black")
        self.time_elapsed = tk.IntVar()

        # grid Frame 2 widgets
        self.lbl_current_process.pack()
        self.lbl_name.pack(anchor="w", pady=(40, 20))
        self.lbl_operation.pack(anchor="w", pady=20)
        self.lbl_max_time.pack(anchor="w", pady=20)
        self.lbl_id.pack(anchor="w", pady=20)
        self.progressbar.pack(pady=20)
        self.lbl_timer.pack()
        
        # ===============  Frame 3  ==================== #
        self.lbl_completed_processes = ttk.Label(self.layout3_frame, text="Completed Processes")
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

    def on_play_button_clicked(self):
        # disable buttons
        self.btn_play.config(state=tk.DISABLED)
        self.btn_add_process.config(state=tk.DISABLED)
        # update item rows
        # self.update_treeview_rows()
        
        # if there are still elements in processes, flush them (appends'em into a new batch)
        self.process.flush_processes_list()
        
        # initialize main timer
        thread1 = Thread(target=self.init_main_timer, daemon=True)
        thread1.start()
        
        # while not self.process.is_empty():
        thread2 = Thread(target=self.execute_process, daemon=True)
        thread2.start()
        
    def execute_process(self):
        """Ejecutar un proceso a la vez"""
        # revisa que aun haya procesos
        if len(self.process.processes) > 0:
            # verifica si batch esta no esta vacío
            if len(self.process.batch[0]) > 0:
                # actualiza labels
                process = self.process.get_first_process()
                self.update_process_labels(process=process)
                # start progressbar
                self.start_progressbar(process['max_time'])
                # update treeview rows
                self.update_treeview_rows()
                # delete last process
                self.process.delete_first_process()
            else:
                del self.process.batch[0]
            print("\nbatch list:", self.process.batch)
            print("process list:", self.process.processes)
            self.execute_process()

    def start_progressbar(self, time):
        for sec in range(100):
            sleep(time / 100)
            self.progressbar['value'] = sec
            self.update_idletasks()
        self.progressbar['value'] = 0

    def update_treeview_rows(self):
        """insert in treeview_2 and delete from treeview_1"""
        self.insert_on_treeview_2()
        if len(self.treeview_process.get_children()) > 0:
            selected_item = self.treeview_process.get_children()[0]
            self.treeview_process.delete(selected_item)
        else:    
            # if not self.process.is_empty():
            items = self.process.batch[0]
            for item in items:
                self.insert_on_treeview(item)

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
        
        operation = f"{process['num1']} {process['operator']} {process['num2']} = {process['result']}"
        
        self.lbl_name.config(text=f"Name: {process['name']}") 
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

    def on_raise_form_button_clicked(self):
        # raise a Form with the fields to create a new process
        raise_form = SaveDataInterface(self, object_process=self.process)
        
        # insert the new brand process in the treeview widget
        self.insert_on_treeview(self.process.processes[-1])
        
        # if batch_size is not specified wil be 5
        self.process.separate_in_batches()
        
        # clear treeview every time batch increments
        self.clear_treeview_items()

    def insert_on_treeview(self, item):
        """insert a new row in treeview every time a new process is added"""
        try:
            p_id = item['id']
            max_time = item['max_time']
        except TypeError:
            print("processes lists empty")
        else:
            self.treeview_process.insert(parent="", index=tk.END, text=p_id, values=(max_time, ))
        finally:
            if len(self.treeview_process.get_children()) == 0:
                items = self.process.batch[-1]
                for item in items:
                    self.insert_on_treeview(item)
    
    def clear_treeview_items(self):
        """clear all items from treeview"""
        items_displayed = len(self.treeview_process.get_children())
        if items_displayed == 5:
            # Delete all items in the treeview
            self.treeview_process.delete(*self.treeview_process.get_children())
        self.lbl_pending_batches.config(text=f"Pending Batches: {self.process.get_batch_len()}")
