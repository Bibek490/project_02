#datavase ko mistake hudaina

#class and objects
# method vanixa



#today class will be much more intreasting

#class is a blueprint and object is its instances.
#euta class ko use gareko dhwerai wota objects bananuna sakxau?
# OOP= object oriented programming 
# pop=procedure oriented programming
#OOP==python,java,php,ruby


#abstraction=data hiding
# polymorphism== euta method ko dherai wota ststes.
#encapsulation== class ko members can be public private, protected
#attributes==variable in the class are attrubute

#inheritance== parent class ma vayeko features child class le acquire garxa
  

class GFG:
    def __init__(self,name,company):
        self.name=name
        self.company=company

    def show(self):
        print(f"my name is {self.name} and i am working at {self.company}")


q=GFG("nature","apple") 
p=GFG("bibek","google")
r=GFG("narayan","tesla")

q.show()
p.show()
r.show()


    