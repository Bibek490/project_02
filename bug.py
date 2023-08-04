class Student:
    def __init__(self,name,age,grade):
        self.name=name
        self.age=age
        self.grade=grade


    def display_intro(self):
        print(f"{self.name}")
        print(f"{self.age}")
        print(f"{self.grade}")

if __name__=="__main__":
    student1=student("bibek",16,"A") #object create gareko with the help of class student.
    student2=student("nature",20,"A")

#student1 and student2 object ho. we made these wuth the help of class name student.



#function call garda always (object.fuction_name) gaeinxa
print("\n student 2:")
student2.display_intro()


#features of classes in object oriented programming language.

#abstracction: date hiding
#encapsulation    : classes allow you to bundle data together into single units.

# task to do tommorow do some research on what is oop in python and what are its featues.
#inheritance:parent class ko feature child calss ma acquire garne.
#polymorphism" ;; onw object have many feature

#attributes: classes allow to do (name, class ,grade) define attributes that stores realated data.
#method : class vitra ko function 