class Person: 

    origin_country = "USA" 
 
    def __init__(self, name, age, gender): 
        self.name = name 
        self.age = age 
        self.gender = gender 

    def speak(self, words): 
        print(f"{self.name} speaks: {words}") 
 
    @classmethod 
    def change_origin_country(cls, new_country): # cls is among parameters 
        cls.origin_country = new_country 
        print(cls.origin_country) 

    @staticmethod 
    def is_adult(age):
        return age > 18

Person.change_origin_country('Ukr') #can be called before instantiation
Andrew = Person('Andrew', 33, 'male')
Bob = Person('Bob', 30, 'male')

print(Andrew.origin_country+'\n'+ Bob.origin_country)

Person.change_origin_country('UK')
print(Andrew.origin_country+'\n'+ Bob.origin_country) #change the attributes in both instances

print(Person.is_adult(30)) #does not require instantiation actually
print(Andrew.is_adult(33))