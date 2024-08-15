class Human():
    
    def __init__(self, name, age):
        self.name = name
        self.__age = age
    
    def get_age(self):
        print(f"The age is {self.__age}")

    def speak(self, phrase):
        print(phrase)

class Mother(Human):
    
    def speak(self, phrase):
        print(f"Mother said: {phrase}")

class Father(Human):
    
    def speak(self, phrase):
        print(f"Father said: {phrase}")

class Child(Mother, Father):

    pass

Andrew = Child('Andrew', 33)

Andrew.speak("good morning!")
