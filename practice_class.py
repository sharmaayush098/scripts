

class MyClass(object):
    """
    Your Comments
    """
    def __init__(self, name):
        self.a = "ayush"
        self.b = "sharma"
        self.name= name

    def method_one(self):
        print("this is method one")
        print(self.name)

    def method_two(self):
        print("this is method two")
        print(self.a+" "+self.b)

    def my_object(self):
        print(self.__dict__)


