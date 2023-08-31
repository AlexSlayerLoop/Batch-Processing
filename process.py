


class Process:
    
    def __init__(self, **process_data) -> None: 
        
        self.programmer_nm = process_data["name"]
        self.id = process_data["id"]
        self.operator = process_data["operator"]
        
        self.max_time = process_data["max_time"] * 1000  # this time will work as ms
        self.num1 = process_data["num1"]
        self.num2 = process_data["num2"]
        
        self.process_num = 0
        self.dict_data = process_data
        
        self.batch = []
        self.list_of_batches = []
        
    
    def get_dict(self):
        return self.batch

    
    def add_process(self):
        pass

 

# class Batch:
    
#     def __init__(self) -> None:
