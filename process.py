import random

class Process:
    
    def __init__(self): 
        """Constructor creates two empty lists"""
        self.batch = None
        self.processes = []
        self.id = 0
    
    def generate_process(self, quantity):
        """Generate quantity-processes with random"""
        for _ in range(quantity):
            self.id += 1
            operator = ('+', '-', '*', '/', '%')
            op = random.choice(operator)
            max_time = random.randint(6, 18)
            num1 = random.randint(1, 100)
            num2 = random.randint(1, 100)
            result = self.operation_result(operator=op, num1=num1, num2=num2)
            
            self.add_process ( 
                id = self.id,
                operator = op,
                max_time = max_time,
                num1 = num1,
                num2 = num2,
                result = result
            )              
    
    def split_in_batches(self, batch_size: int = 5):
        split_lists = []
        for i in range(0, len(self.processes), batch_size):
            chunk = self.processes[i:i + batch_size]
            split_lists.append(chunk)

        self.batch = split_lists
    
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
        
