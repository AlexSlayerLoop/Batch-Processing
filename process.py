class Process:
    
    def __init__(self): 
        """Constructor creates two empty lists"""
        self.processes = []
        self.batch = []

    def add_process(self, **kw):
        """add a new process to the list"""
        self.processes.append(kw)

    def is_empty(self) -> bool:
        return len(self.processes) == 0

    def get_last_process_added(self):
        if not self.is_empty():
            return self.processes[-1]

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
        # Si el numero de procesos es divisible entre batch_size y ademas list procesos es mayor que 0
        if (len(self.processes) > 0) and (len(self.processes) % batch_size) == 0: 
            aux_list = self.processes[-batch_size:]  # agrega los ultimos 5 procesos a una lista
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
    
    def delete_last_process(self):
        """Delete last process from batch list and processes list"""
        del self.batch[-1][-1]
        del self.processes[-1]
