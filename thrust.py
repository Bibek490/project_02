#class and object


class person:
    def __init__(self,name,age):
       self.name=name
       self.age=age



    def introduce(self):
        print(f"hi my name is {self.name}.i am {self.age} years old.")



p=person("bibek",16) 
q=person("narayan",90)


p.introduce()
q.introduce()