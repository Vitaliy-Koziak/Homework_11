"""В класі Name визначте:

атрибути для first name та last name (fname та lname відповідно);

атрибут fullname що повертає first і last names;

атрибут initials який повертає ініціали (перші літери first та last name, розділених ‘.’ ."""
class Name(object):
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
        self.fulname = fname + " " + lname
        self.initials = fname[0] + '.' + lname[0] + '.'

    def __repr__(self):
        return {'First name': self.fname, 'Last name': self.lname}
def main():
     name_1= Name("Vitaliy","Koziak")
     print(name_1.__repr__())
     print(name_1.fulname)
     print(name_1.initials)


if __name__ == "__main__":
    main()