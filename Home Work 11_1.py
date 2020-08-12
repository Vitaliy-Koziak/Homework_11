"""В класі Person визначте метод compare_age(), який повертатиме результат порівняння віку людини з
Вашим віком. При заданих об’єктах p1, p2 і p3, які будуть ініціалізовані name та age, буде повертатися
повідомлення наступного формату:

{other_person} is {older than / younger than / the same age as} me."""
class Person(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def compare_age(self):
        if self.age > 18:
            print(self.name,"is older than me! ")
        elif self.age < 18:
            print(self.name,"is younger than me! ")
        else:
            print(self.name,"is the same age as me! ")
def main():
    person_1 = Person("Arsen",20)
    person_1.compare_age()
    person_2 = Person("Petro",13)
    person_2.compare_age()
    person_3 = Person("Ann",18)
    person_3.compare_age()

if __name__ == "__main__":
    main()
