"""Визначте атрибути fullname та email в класі Employee. При заданих first та last names:

- В конструкторі сформуйте fullname звичайним з’єднанням через пробіл first та last name.

В конструкторі сформуйте email з’єднанням first та last name через ‘.’ між ними та приєднуючи
‘@company.com’ наприкінці."""
class Employee(object):
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
        self.fulname = fname + " " + lname
        self.email = fname.lower() + '.' + lname.lower() + '@company.com'
def main():
     employee_1= Employee("Vitaliy","Koziak")
     print(employee_1.fulname)
     print(employee_1.email)


if __name__ == "__main__":
    main()