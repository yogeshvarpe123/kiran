class Student:
    School = "yogesh"

    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1 + self.m2 + self.m3)

s1 = Student(1,2,3)
s2 = Student(3,4,12)

print(s1.avg())
print(s2.avg())

