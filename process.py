


class Process:
    
    def __init__(self): 
        
        self.processes = []
        self.batch = []
        
        # self.programmer_nm = kw["name"]
        # self.id = kw["id"]
        # self.operator = kw["operator"]
        
        # self.max_time = kw["max_time"] * 1000  # this time will work as ms
        # self.num1 = kw["num1"]
        # self.num2 = kw["num2"]
        
        
    def add_process(self, **kw):
    
        print(kw)
        self.processes.append(kw)
        
    
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
    
    