class Student:

    school = "MGP"

    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return(self.m1+self.m2+self.m3)/3

    @classmethod
    def info(cls):
        return cls.school

s1=Student(55,93,78)
s2=Student(73,87,95)

print("average marks of student 1 are :",s1.avg())
print(Student.info())