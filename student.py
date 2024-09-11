class Student:
    def __init__(self, gender, age, first_name, last_name, record_book):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name
        self.record_book = record_book

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.age} years old, {self.gender}, Record Book: {self.record_book}"

    def __eq__(self, other):
        if isinstance(other, Student):
            return (self.first_name == other.first_name and
                    self.last_name == other.last_name and
                    self.record_book == other.record_book)
        return False

    def __hash__(self):
        return hash((self.first_name, self.last_name, self.record_book))
