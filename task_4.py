class EmployeeSalary:
    hourly_payment = 400
    def __init__(self, name, hours, rest_days, email):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email

    @classmethod
    def get_hours(cls, name, rest_days, email):
        return cls(name, (7 - rest_days) * 8, rest_days, email)

    @classmethod
    def get_email(cls, name, hours, rest_days):
        return cls(name, hours, rest_days, f"{name}@email.com")

    @classmethod
    def set_hourly_payment(cls, new_payment):
        cls.hourly_payment = new_payment
    
    def salary(self):
        salary = self.hours * self.hourly_payment
        return f"{self.name}, {self.hours}, {self.rest_days}, {self.email}, {salary}"

barbos = EmployeeSalary("Barbos", 40, 2, "Barbos@test.com")
igor = EmployeeSalary.get_email("igor", 40, 2)
liza = EmployeeSalary.get_hours("Liza", 2, "liza@email.com")
print(barbos.salary())
print(igor.salary())
print(liza.salary())
EmployeeSalary.set_hourly_payment(200)
print(barbos.salary())
print(igor.salary())
print(liza.salary())