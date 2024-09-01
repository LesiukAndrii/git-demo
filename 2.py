class Person: 

    origin_country = "USA" 
 
    def __init__(self, name, age, gender): 
        self.name = name 
        self.age = age 
        self.gender = gender
        #self.email = f"{self.name}@email.com" 

    def speak(self, words): 
        print(f"{self.name} speaks: {words}") 
 
    @property # now email is an attribute and is changed after name update
    def email(self): 
        return f"{self.name}@email.com"

    @classmethod 
    def change_origin_country(self, new_country): # self or cls is among parameters 
        self.origin_country = new_country 
        print(self.origin_country) 

    @staticmethod 
    def is_adult(age):
        return age > 18
'''
Andrew = Person('Andrew', 33, 'male')
print(Andrew.email)
Andrew.name = 'andriilesiuk'
print(Andrew.email)

'''
Person.change_origin_country('Ukr') #can be called before instantiation
Andrew = Person('Andrew', 33, 'male')
Bob = Person('Bob', 30, 'male')

print(Andrew.origin_country+'\n'+ Bob.origin_country)

Person.change_origin_country('UK')
print(Andrew.origin_country+'\n'+ Bob.origin_country) #change the attributes in both instances

print(Person.is_adult(30)) #does not require instantiation actually
print(Andrew.is_adult(33))

