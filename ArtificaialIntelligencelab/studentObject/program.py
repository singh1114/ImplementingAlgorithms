class Student(object):
    # The magic function that works as a constructor
    def __init__(self):
        self.Name = "Ranvir"
        self.Age = 21
        self.Class = "D3"
        self.rollNumber = 917

    def getStudent(self):
        self.Name = raw_input("\nName: ")
        self.Age = raw_input("\nAge: ")
        self.Class = raw_input("\nClass: ")
        self.rollNumber = raw_input("\nRoll Number: ")

    def showStudent(self):
        print(self.Name + "\n")
        print(self.Age + "\n")
        print(self.Class + "\n")
        print(self.rollNumber + "\n")

sachin = Student()
sachin.getStudent()
sachin.showStudent()
