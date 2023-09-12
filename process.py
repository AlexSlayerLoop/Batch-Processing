class Process:
    
    def __init__(self): 
        """Constructor creates two empty lists"""
        # self.batch = []
        # self.processes = []
        
        # ========== Init with values ========== # 
        self.batch = [
            [
                {'id': '1', 'name': 'alex', 'operator': '+', 'max_time': 1, 'num1': 1, 'num2': 1, 'result': 2}, 
                {'id': '2', 'name': 'pepe', 'operator': '+', 'max_time': 1, 'num1': 3, 'num2': 3, 'result': 6}, 
                {'id': '3', 'name': '123', 'operator': '+', 'max_time': 1, 'num1': 3, 'num2': 112, 'result': 115}, 
                {'id': '4', 'name': '321', 'operator': '+', 'max_time': 1, 'num1': 1, 'num2': 2, 'result': 3}, 
                {'id': '5', 'name': '12', 'operator': '+', 'max_time': 1, 'num1': 2, 'num2': 123, 'result': 125}
            ], 
            [
                {'id': '6', 'name': '123as', 'operator': '+', 'max_time': 2, 'num1': 2, 'num2': 32, 'result': 34}, 
                {'id': '7', 'name': 'asd2', 'operator': '+', 'max_time': 2, 'num1': 2, 'num2': 123, 'result': 125}, 
                {'id': '8', 'name': 'asda', 'operator': '+', 'max_time': 1, 'num1': 321, 'num2': 543, 'result': 864}, 
                {'id': '9', 'name': '2123s', 'operator': '+', 'max_time': 1, 'num1': 33, 'num2': 33, 'result': 66}, 
                {'id': '10', 'name': '123ffd', 'operator': '+', 'max_time': 2, 'num1': 321, 'num2': 222, 'result': 543}
            ], 
            [
                {'id': '11', 'name': '12dd', 'operator': '+', 'max_time': 1, 'num1': 32, 'num2': 213, 'result': 245}, 
                {'id': '12', 'name': 'akaka', 'operator': '*', 'max_time': 3, 'num1': 1, 'num2': 321, 'result': 321}, 
                {'id': '13', 'name': 'asdf', 'operator': '+', 'max_time': 2, 'num1': 321, 'num2': 123, 'result': 444}, 
                {'id': '14', 'name': 'gio', 'operator': '+', 'max_time': 3, 'num1': 21, 'num2': 12, 'result': 33}, 
                {'id': '15', 'name': 'pio', 'operator': '+', 'max_time': 3, 'num1': 23, 'num2': 2, 'result': 25}
            ], 
            [
                {'id': '16', 'name': 'alejasdmro', 'operator': '+', 'max_time': 3, 'num1': 23, 'num2': 43, 'result': 66}
            ]
        ]
        self.processes =  [
            {'id': '1', 'name': 'alex', 'operator': '+', 'max_time': 1, 'num1': 1, 'num2': 1, 'result': 2}, 
            {'id': '2', 'name': 'pepe', 'operator': '+', 'max_time': 1, 'num1': 3, 'num2': 3, 'result': 6}, 
            {'id': '3', 'name': '123', 'operator': '+', 'max_time': 1, 'num1': 3, 'num2': 112, 'result': 115}, 
            {'id': '4', 'name': '321', 'operator': '+', 'max_time': 1, 'num1': 1, 'num2': 2, 'result': 3}, 
            {'id': '5', 'name': '12', 'operator': '+', 'max_time': 1, 'num1': 2, 'num2': 123, 'result': 125}, 
            {'id': '6', 'name': '123as', 'operator': '+', 'max_time': 2, 'num1': 2, 'num2': 32, 'result': 34}, 
            {'id': '7', 'name': 'asd2', 'operator': '+', 'max_time': 2, 'num1': 2, 'num2': 123, 'result': 125}, 
            {'id': '8', 'name': 'asda', 'operator': '+', 'max_time': 1, 'num1': 321, 'num2': 543, 'result': 864}, 
            {'id': '9', 'name': '2123s', 'operator': '+', 'max_time': 1, 'num1': 33, 'num2': 33, 'result': 66}, 
            {'id': '10', 'name': '123ffd', 'operator': '+', 'max_time': 2, 'num1': 321, 'num2': 222, 'result': 543}, 
            {'id': '11', 'name': '12dd', 'operator': '+', 'max_time': 1, 'num1': 32, 'num2': 213, 'result': 245}, 
            {'id': '12', 'name': 'akaka', 'operator': '*', 'max_time': 3, 'num1': 1, 'num2': 321, 'result': 321}, 
            {'id': '13', 'name': 'asdf', 'operator': '+', 'max_time': 2, 'num1': 321, 'num2': 123, 'result': 444}, 
            {'id': '14', 'name': 'gio', 'operator': '+', 'max_time': 3, 'num1': 21, 'num2': 12, 'result': 33}, 
            {'id': '15', 'name': 'pio', 'operator': '+', 'max_time': 3, 'num1': 23, 'num2': 2, 'result': 25}, 
            {'id': '16', 'name': 'alejasdmro', 'operator': '+', 'max_time': 3, 'num1': 23, 'num2': 43, 'result': 66}
        ]
        
    
    def add_process(self, **kw):
        """add a new process to the list"""
        self.processes.append(kw)

    def is_empty(self) -> bool:
        return len(self.processes) == 0

    def get_first_process(self):
        if not self.is_empty():
            return self.processes[0]

    def operation_result(self, operator: str, num1: int, num2: int):
        """returns a results depending on the operator and numbers"""
        return (
            num1 + num2 if operator == '+' else
            num1 - num2 if operator == '-' else
            num1 * num2 if operator == '*' else
            num1 / num2 if operator == '/' else
            num1 % num2 if operator == '%' else None
        )

    def is_unique(self, new_id: str) -> bool:
        """Verify if and id already exists"""
        if len(self.processes) == 0: 
            return True
        else: 
            id_list = [p['id'] for p in self.processes] 
            return not new_id in id_list 

    def separate_in_batches(self, batch_size: int = 5):
        """Separate in batches every tims it is posbible"""
        aux_list = list()
        # Si el numero de procesos es divisible entre batch_size y ademas lista procesos es mayor que 0
        if (len(self.processes) > 0) and ((len(self.processes) % batch_size) == 0):
            aux_list = self.processes[ - batch_size:]  # agrega los ultimos 5 procesos a una lista
            self.batch.append(aux_list) # agrega lista antetior como un nuevo batch

    def flush_processes_list(self):
        """if there are still elements in processes list appends them on batch"""
        num_procesos_restantes = len(self.processes) % 5  # 5 es por el tamanho de cada Lote
        if num_procesos_restantes > 0 and num_procesos_restantes < 5:
            procesos_restantes = self.processes[ - num_procesos_restantes:]
            self.batch.append(procesos_restantes)
        
    def get_batch_len(self) -> int:
        """return batch list length"""
        return len(self.batch)
    
    def delete_first_process(self):
        """Delete last process from batch list and processes list"""
        del self.batch[0][0]
        del self.processes[0]
        
        if len(self.batch[0]) == 0:
            del self.batch[0] 
