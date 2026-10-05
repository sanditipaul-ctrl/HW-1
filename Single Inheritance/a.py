class Employee:
    def __init__(self):
        self.name = input("Enter name: ")
        self.id = input("Enter employee id: ")
    def display_info(self):
        print(f'Name: {self.name}')
        print(f'Employee id: {self.id}')

class Manager(Employee):
    def __init__(self):
        super().__init__()
        self.department = input("Enter department: ")

    def display_info(self):
        super().display_info()
        print(f'Department: {self.department}')

managers = []

for i in range(5):
    print(f"\nEnter information for Manager {i+1}")
    manager = Manager()
    managers.append(manager)

print("Thanks!")