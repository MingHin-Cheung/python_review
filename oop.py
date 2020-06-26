class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


employee1 = Employee("ming", "Cheung", 15)
employee2 = Employee("hin", "Cheung", 17)

print(Employee.fullname(employee1))
print(employee1.fullname())
print(employee2.fullname())

