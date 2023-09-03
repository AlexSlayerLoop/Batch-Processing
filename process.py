


class Process:
    
    def __init__(self): 
        "Constructor creates two empty lists"
        self.processes = []
        self.batch = []
        
        
    def add_process(self, **kw):
    
        self.processes.append(kw)
        print(self.processes)
        
    
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
        pass
    
    