from student_data import StudentData

class DevOpsStudent(StudentData):  # subclass to StudentData
    def __init__(self, current_grade, current_trainer):
        # super().__init__ is taking all the members of the parent class
        super().__init__(current_grade, current_trainer)
        self.current_grade = current_grade
        self.current_trainer = current_trainer


John = DevOpsStudent(70, "Billy bog-man")  # Creation of an instance of the DevOpsStudent class

# Although the print_details() method is not in the DevOpsStudent class it can still be used as it has been inherited
# from the StudentData class, this allows it to access the attributes and methods of the parent.
print(John.print_details())
