classmates=[]
def add_classmate(name):
    classmaates.append({'name':name,'attendance':0})

    print(f"{name} added to the class")


    def make_attendance(name):
        for classmate in classmates:
            classmate['name']==name:
            classmate['attendance']+=1
            print(f"{name} is present.total attendance:{classmate['attendance']}")
            return
        print("classmate not found.")
                
    if classmate['name']==name:
                    classmate['attendance']+=1
    print(f"{name} is present.total attendance":{classmate["attendance"]})
    return print("classmate not found.")  


def view_attendance():
    print("Attendance")
    for classmate in classmates:
        print(f"{classmate['name']}:{classmate['attendance']}")


def view_attendance():
    print('Attendance')
    for classmate in classmates:
        print(f"{classmate['name']}:{classmate['attendance']}")



def main():
 print("digital attendance system")

 while True:
     print("noptions")
     print("1.make attendance")
     print("2.make attendance")
     print("3.view attendance")
     print("4. Exit")


     choice=input("enter your choice:")

     if choice=="1":
         name=input("enter classmate name:")
         add_classmate(name)


     elif choice=='2':
         name=input("enter your classmate name:")
         make_attendance(name)

     elif choice=='3':



      choice=input("enter your choice")




if choice=='1':
    name=str(input("enter classmates name:")
             add_classmate(name)

