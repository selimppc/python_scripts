"""
Code for Deep Equals
"""

class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __eq__(self, other) -> bool:
        if isinstance(other, Person):
            return self.age == other.age
        return False

# check 2 persons are equal
john = Person('John', 'Doe', 25)
mary = Person('Mary', 'Doe', 25)
third = Person('Third', 'Doe', 22)

equal_check = (john == mary == third)
print(equal_check)



