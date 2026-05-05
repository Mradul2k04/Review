#mradul->Task 3 – Employee Performance Rating System
#Scenario
#Build an employee performance rating system where different job types have different evaluation logic.
#OOP‑Covered
#Abstraction, inheritance, polymorphism, method overriding, error handling
#Instructions
#Create abstract class Employee with id, name, and abstract method getPerformanceRating().
#Create subclasses SoftwareEngineer, SalesAssociate, OfficeAdmin which override getPerformanceRating() differently (e.g., productivity, revenue, feedback).
#Demonstrate:
#List of Employee objects.
#Polymorphic calls to getPerformanceRating().
#Input validation and custom exceptions (e.g., InvalidRatingException if rating < 1 or > 5).


from abc import ABC, abstractmethod

class InvalidRatingException(Exception):
    pass

class Employee(ABC):
    def __init__(self, emp_id, emp_name):
        self.emp_id = emp_id
        self.emp_name = emp_name

    @abstractmethod
    def getPerformanceRating(self):
        pass

    def performance_rating(self, rating):
        if 1 <= rating <= 5:
            return rating
        else:
            raise InvalidRatingException(f"Rating {rating} for {self.emp_name} is invalid.")

class SoftwareEngineer(Employee):
    def __init__(self, emp_id, emp_name, productivity):
        super().__init__(emp_id, emp_name)
        self.productivity = productivity

    def getPerformanceRating(self):
        return self.performance_rating(self.productivity)

class SalesAssociate(Employee):
    def __init__(self, emp_id, emp_name, revenue):
        super().__init__(emp_id, emp_name)
        self.revenue = revenue

    def getPerformanceRating(self):
        return self.performance_rating(self.revenue)

class OfficeAdmin(Employee):
    def __init__(self, emp_id, emp_name, feedback):
        super().__init__(emp_id, emp_name)
        self.feedback = feedback

    def getPerformanceRating(self):
        return self.performance_rating(self.feedback)

print("---------- Employee Performance Rating System ------------")

employees = [
    SoftwareEngineer(1, "Mradul", 2),
    SalesAssociate(2, "Anuj", 3),
    OfficeAdmin(3, "Karan", 2),
    SoftwareEngineer(4, "Error Test", 6)
]

for i in employees:
    try:
        rating_val = i.getPerformanceRating()
        print(f"ID: {i.emp_id} | Name: {i.emp_name} | Rating: {rating_val}")
    except InvalidRatingException as e:
        print(f"Error for ID {i.emp_id}: {e}")