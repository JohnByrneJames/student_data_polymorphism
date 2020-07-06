# Polymorphism

#### A concept related to the object oriented approach of programming.

Polymorphism is one of the core concepts in OOP languages, it describes the concept that different classes
can be used with same interface. Each of these classes can provide its own implementation of the interface.
If a method sometimes referred to as an interface is overridden in another class
it is said to be polymorphic. This means it can be used to produce different results through the same
method.

[**devops_student**](devops_student.py) **[Parent/ Base Class]**
* **Attributes**
    * current_grade `private`
    * current_trainer `public`
* **Methods**
    * print_details `public`
    * change_current_grade `private` 

[**student_data**](student_data.py) **[Child/ Derived Class]**
* **Methods**
    * print_details `public`
    
Here the method `print_details` has been made polymorphic as it has been overridden and
using a for loop printed out for both classes. It comes out different showing that the
class is using polymorphism. 

Two classes that can be iterated and provide outputs for each method call through a
polymorphic variable such as instance are known as polymorphic methods.

```python
Ross = StudentData(90, "Hulk Hagen")
John = DevOpsStudent(70, "Billy bog-man")

for instance in (Ross, John):
    print(instance)
    print(instance.print_details())
```

The output for this would be different for each instance, but essentially this
for loop doesn't care what is in the `print_details()` it just knows they are in both classes. Therefore
they can both be accessed this way.
