class Process:
    
    def __init__(self): 
        """Constructor creates two empty lists"""
        self.processes = []
        self.batch = []
        
        # ========== Init with values ========== # 
        # self.batch = [
        #     [
        #         {'id': '1', 'name': 'Alejandro', 'operator': '+', 'max_time': 2, 'num1': 2, 'num2': 2, 'result': 4}, 
        #         {'id': '2', 'name': 'fabian', 'operator': '-', 'max_time': 2, 'num1': 2, 'num2': 3, 'result': -1}, 
        #         {'id': '3', 'name': 'giovanni', 'operator': '+', 'max_time': 2, 'num1': 23, 'num2': 12, 'result': 35}, 
        #         {'id': '4', 'name': 'kaka', 'operator': '+', 'max_time': 2, 'num1': 12, 'num2': 21, 'result': 33}, 
        #         {'id': '5', 'name': 'messi', 'operator': '+', 'max_time': 2, 'num1': 2, 'num2': 121, 'result': 123}
        #     ], 
        #     [
        #         {'id': '6', 'name': 'carlos', 'operator': '+', 'max_time': 2, 'num1': 99, 'num2': 1, 'result': 100}, 
        #         {'id': '7', 'name': 'pepe', 'operator': '*', 'max_time': 2, 'num1': 2, 'num2': 12, 'result': 24}, 
        #         {'id': '8', 'name': 'maradona', 'operator': '*', 'max_time': 2, 'num1': 3, 'num2': 3, 'result': 9}, 
        #         {'id': '9', 'name': 'Diego', 'operator': '%', 'max_time': 2, 'num1': 99, 'num2': 3, 'result': 0}, 
        #         {'id': '10', 'name': 'monse', 'operator': '+', 'max_time': 2, 'num1': 30, 'num2': 3, 'result': 33}
        #     ], 
        #     [
        #         {'id': '11', 'name': 'oscar', 'operator': '-', 'max_time': 2, 'num1': 0, 'num2': 4, 'result': -4},
        #         {'id': '12', 'name': 'jose', 'operator': '*', 'max_time': 2, 'num1': 12, 'num2': 12, 'result': 144}, 
        #         {'id': '13', 'name': 'batman', 'operator': '/', 'max_time': 2, 'num1': 45, 'num2': 5, 'result': 9.0}, 
        #         {'id': '14', 'name': 'maria', 'operator': '+', 'max_time': 2, 'num1': 2, 'num2': 123, 'result': 125}, 
        #         {'id': '15', 'name': 'nicole', 'operator': '*', 'max_time': 2, 'num1': 14, 'num2': 15, 'result': 210}, 
        #     ], 
        #     [
        #         {'id': '16', 'name': 'josefa', 'operator': '+', 'max_time': 2, 'num1': 160, 'num2': 40, 'result': 200},
        #         {'id': '17', 'name': 'lorena', 'operator': '*', 'max_time': 2, 'num1': 23, 'num2': 32, 'result': 736}, 
        #         {'id': '18', 'name': 'karina', 'operator': '*', 'max_time': 2, 'num1': 15, 'num2': 15, 'result': 225}, 
        #         {'id': '19', 'name': 'elon', 'operator': '-', 'max_time': 2, 'num1': 1, 'num2': 1, 'result': 0}, 
        #         {'id': '20', 'name': 'omar', 'operator': '+', 'max_time': 2, 'num1': 24, 'num2': 24, 'result': 48}
        #     ], 
        #     [
        #         {'id': '21', 'name': 'lola', 'operator': '+', 'max_time': 2, 'num1': 999, 'num2': 1, 'result': 1000},
        #         {'id': '22', 'name': 'hernesto', 'operator': '+', 'max_time': 2, 'num1': 3, 'num2': 2, 'result': 5},
        #         {'id': '23', 'name': 'violeta', 'operator': '+', 'max_time': 2, 'num1': 232, 'num2': 112, 'result': 344} 
        #     ]
        # ]
        # self.processes = [
        #     {'id': '1', 'name': 'Alejandro', 'operator': '+', 'max_time': 2, 'num1': 2, 'num2': 2, 'result': 4}, 
        #     {'id': '2', 'name': 'fabian', 'operator': '-', 'max_time': 2, 'num1': 2, 'num2': 3, 'result': -1}, 
        #     {'id': '3', 'name': 'giovanni', 'operator': '+', 'max_time': 2, 'num1': 23, 'num2': 12, 'result': 35}, 
        #     {'id': '4', 'name': 'kaka', 'operator': '+', 'max_time': 2, 'num1': 12, 'num2': 21, 'result': 33}, 
        #     {'id': '5', 'name': 'messi', 'operator': '+', 'max_time': 2, 'num1': 2, 'num2': 121, 'result': 123}, 
        #     {'id': '6', 'name': 'carlos', 'operator': '+', 'max_time': 2, 'num1': 99, 'num2': 1, 'result': 100}, 
        #     {'id': '7', 'name': 'pepe', 'operator': '*', 'max_time': 2, 'num1': 2, 'num2': 12, 'result': 24}, 
        #     {'id': '8', 'name': 'maradona', 'operator': '*', 'max_time': 2, 'num1': 3, 'num2': 3, 'result': 9}, 
        #     {'id': '9', 'name': 'Diego', 'operator': '%', 'max_time': 2, 'num1': 99, 'num2': 3, 'result': 0}, 
        #     {'id': '10', 'name': 'monse', 'operator': '+', 'max_time': 2, 'num1': 30, 'num2': 3, 'result': 33},
        #     {'id': '11', 'name': 'oscar', 'operator': '-', 'max_time': 2, 'num1': 0, 'num2': 4, 'result': -4}, 
        #     {'id': '12', 'name': 'jose', 'operator': '*', 'max_time': 2, 'num1': 12, 'num2': 12, 'result': 144}, 
        #     {'id': '13', 'name': 'batman', 'operator': '/', 'max_time': 2, 'num1': 45, 'num2': 5, 'result': 9.0}, 
        #     {'id': '14', 'name': 'maria', 'operator': '+', 'max_time': 2, 'num1': 2, 'num2': 123, 'result': 125}, 
        #     {'id': '15', 'name': 'nicole', 'operator': '*', 'max_time': 2, 'num1': 14, 'num2': 15, 'result': 210}, 
        #     {'id': '16', 'name': 'josefa', 'operator': '+', 'max_time': 2, 'num1': 160, 'num2': 40, 'result': 200}, 
        #     {'id': '17', 'name': 'lorena', 'operator': '*', 'max_time': 2, 'num1': 23, 'num2': 32, 'result': 736}, 
        #     {'id': '18', 'name': 'karina', 'operator': '*', 'max_time': 2, 'num1': 15, 'num2': 15, 'result': 225}, 
        #     {'id': '19', 'name': 'elon', 'operator': '-', 'max_time': 2, 'num1': 1, 'num2': 1, 'result': 0}, 
        #     {'id': '20', 'name': 'omar', 'operator': '+', 'max_time': 2, 'num1': 24, 'num2': 24, 'result': 48}, 
        #     {'id': '21', 'name': 'lola', 'operator': '+', 'max_time': 2, 'num1': 999, 'num2': 1, 'result': 1000},
        #     {'id': '22', 'name': 'hernesto', 'operator': '+', 'max_time': 2, 'num1': 3, 'num2': 2, 'result': 5},
        #     {'id': '23', 'name': 'violeta', 'operator': '+', 'max_time': 2, 'num1': 232, 'num2': 112, 'result': 344} 
        # ]

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

    def is_unique(self, new_id):
        """Verify if and id already exists"""
        id_list = [id['id'] for id in self.processes]
        return new_id in id_list

    def separate_in_batches(self, batch_size: int = 5):
        """Separate in batches every tims it is posbible"""
        aux_list = list()
        # Si el numero de procesos es divisible entre batch_size y ademas lista procesos es mayor que 0
        if (len(self.processes) > 0) and ((len(self.processes) % batch_size) == 0):
            aux_list = self.processes[:batch_size]  # agrega los primeros 5 procesos a una lista
            self.batch.append(aux_list)

    def flush_processes_list(self):
        """if there are still elements in processes list appends them on batch"""
        num_procesos_restantes = len(self.processes) % 5  # 5 es por el tamanho de cada Lote
        if num_procesos_restantes > 0:
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
