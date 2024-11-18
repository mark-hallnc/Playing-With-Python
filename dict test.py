import pickle


def main():

    employeeDictionary = {}
    
    #open to write
    filename = 'file.dat'
    file = open(filename, 'wb')

    name = "bob"
    id_number = 1
    department = "accounting"
    title = "accountant"
    newEmp = Employee(name, id_number, department, title)

    
   # newEmp.setName(name)
   # newEmp.set_id_number(id_number)
   # newEmp.set_department(department)
   # newEmp.set_title(title)
    employeeDictionary[newEmp] = newEmp

    print(dict)
    pickle.dump(dict, file)
    file.close()
    


    
  #  dict = {'bob': 1, 'e': 2, 'f': 3}
  #  name = 'bob'
  #  del dict[name]
  #  print(dict)

    #open to read
    file = open(filename, 'rb')
    unwrapped = pickle.load(file)
    print(unwrapped)

    
class Employee: 
    def __init__(self, name, id_number, department, title):
        self.__name = name
        self.__id_number = id_number
        self.__department = department
        self.__title = title
    # Setters for name, id, department and title.
    def set_name(self, name):
        self.__name = name
    def set_id_number(self, id_number):
        self.__id_number = id_number
    def set_department(self, department):
        self.__department = department
    def set_title(self, title):
        self.__title = title
    # Getters for name, id, department and title.
    def get_name(self):
        return self.__name
    def get_id_number(self):
        return self.__id_number
    def get_department(self):
        return self.__department
    def get_title(self):
        return self.__title
    # Method to display current state of object.
    def __str__(self):
        result = 'Name: ' + self.get_name() + \
                 '\nID number: ' + self.get_id_number() + \
                 '\nDepartment: ' + self.get_department() + \
                 '\nTitle: ' + self.get_title()
        return result


    










main()
