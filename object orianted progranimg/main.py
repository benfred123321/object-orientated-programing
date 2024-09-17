#object oriented porgraming
#step 1-creating a class - a class is a blueprint of the object we want to create,it includs properties and functions.
#step 2-creating object useing the class created in step 1

class Student:
    
    #creating functions 
    #creating constructor function
    def __init__(self):
        print("this function is responsable for creating student objet")
        #creating properties
        self.name = ""
        self.age = 12
        self.grade = 7
        self.home_room_teacher = "mrs jones"

    
    #creating function for displaying properties
    def show_details(self):
        print("the details of the stiudent are: ")
        print(self.name)
        print(self.age)
        print(self.grade)
        print(self.home_room_teacher)

    #creating funtions to update
    def update_details(self):
        self.name = input("what is the name of the stuent?")
        self.age  = int(input("what is the age of the student?"))

#creating objects using Student blueprint 
student1 = Student()
#calling show details from the class
student1.show_details()
student1.update_details()
student1.show_details()

#to create four diffrent objects create their details and show their details
#and continue on the fly game
