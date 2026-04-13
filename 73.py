class Employee:
    def __init__(self):
        print("Employee created")
    def __del__(self):
        print("Destructor called")                      
def Create_obj():
     print("Making an object")
     obj=Employee() 
     print("functon end") 
     return obj
obj=Create_obj()           