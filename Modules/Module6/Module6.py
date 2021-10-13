class ObjectTesting:
 
    # default constructor
    def __init__(self):
        self.anobj = "ObjectTesting"
 
    # a method for printing data members
    def print_AnObj(self):
        print(self.anobj)
 
 
# creating object of the class
obj = ObjectTesting()
 
# calling the instance method using the object obj
obj.print_AnObj()