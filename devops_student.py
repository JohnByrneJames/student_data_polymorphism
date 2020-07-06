from student_data import StudentData

class DevOpsStudent(StudentData):  # subclass to StudentData
    def __init__(self, current_grade, current_trainer):
        # super().__init__ is taking all the members of the parent class
        super().__init__(current_grade, current_trainer)
        self.current_grade = current_grade
        self.current_trainer = current_trainer

    def print_details(self):
        return "You have overridden the print_details() method from student_data..."


Ross = StudentData(90, "Hulk Hagen")  # Creation of instance of the StudentData class
John = DevOpsStudent(70, "Billy bog-man")  # Creation of an instance of the DevOpsStudent class

# Two classes that can be iterated and provide outputs for each method call through a
# polymorphic variable such as instance are known as polymorphic methods
for instance in (Ross, John):  # Creates a union of classes StudentData and DevOpsStudent
    print(instance)  # print out the current classes object data (demonstrate different classes)
    # instance is an alias for both classes but can access them both as they have the same method name
    print(instance.print_details())
    print("")
