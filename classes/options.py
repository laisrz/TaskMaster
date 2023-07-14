class Option:
    def __init__(self, option):
        self.option = option
    
    def is_create_task(self):
        return self.option == "c"
    
    def is_view_tasks(self):
        return self.option == "v"
    
    def is_filter(self):
        return self.option == "f"
    
    def is_update(self):
        return self.option == "u"
    
    def is_modify(self):
        return self.option == "m"
    
    def is_delete(self):
        return self.option == "d"
    
    def is_confirm_delete(self):
        return self.option == "y"
    
    def is_exit(self):
        return self.option == "e"