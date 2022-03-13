class Student(object):
    def __init__(self,name,age,gender,grade):
        self.name = name
        self.age = age
        self.gender = gender
        self.grade = {}
    def setGrade(self,course,grade):
        self.grade[course]=grade
    def getGrade(self,course):
        return self.grade[course]
    def getGPA(self):
        return sum(self.grade.values())/len(self.grade)

Riya = Student("Riya",14,"female",{"maths":9})
print(Riya.name)
Riya.setGrade("maths",9)
print(Riya.getGPA())