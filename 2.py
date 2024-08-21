class Person: 

    origin_country = "USA" 
 
    def __init__(self, name, age, gender): 
        self.name = name 
        self.age = age 
        self.gender = gender 

    def speak(self, words): 
        print(f"{self.name} speaks: {words}") 
 
    @classmethod 
    def change_origin_country(cls, new_country): 
        cls.origin_country = new_country 
        print(cls.origin_country) 

