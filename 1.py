class Human():
    
    def __init__(self, name, age):
        self.name = name
        self.__age = age
    
    def get_age(self):
        print('The age is {0}'.format(self.__age))

Teacher = Human('Andrew', 33)

Teacher.get_age()
