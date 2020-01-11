class Student():
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    def name(self):
        return self.firstName + " " + self.lastName


class WorkingStudent(Student):  # erbe alle eigenschaften aus der class: Student
    def __init__(self, firstName, lastName, company):
        super().__init__(firstName, lastName)  # überneme firstName..etc. aus class: Student
        self.company = company

    def name(self):
        return super().name() + " (" + self.company + ")"


students = [
    Student("Edo", "Cajlakovic"),
    WorkingStudent("Saban", "Saulic", "Egal GmbH"),
    Student("Enida", "Cajlakovic"),
    WorkingStudent("Adis", "Cajlakovic", "Wichtig GmbH")
]

for i in students:
    print(i.name())


# working_student = WorkingStudent("Saban", "Saulic", "Egal GmbH")
# print(working_student.name())
#
# student = Student("Edo", "Cajlakovic")
# print(student.name())
