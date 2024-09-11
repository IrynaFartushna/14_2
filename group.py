from student import Student

class GroupLimitExceededError(Exception):
    """Виключення для ситуації, коли у групі більше 10 студентів."""
    def __init__(self, message="Cannot add more than 10 students to the group"):
        self.message = message
        super().__init__(self.message)

class Group:
    def __init__(self, number):
        self.number = number
        self.group = set()
        self.max_students = 10  # Ограничение на количество студентов в группе

    def add_student(self, student):
        if len(self.group) >= self.max_students:
            raise GroupLimitExceededError()
        self.group.add(student)

    def delete_student(self, last_name):
        student_to_remove = self.find_student(last_name)
        if student_to_remove:
            self.group.remove(student_to_remove)
        else:
            print(f"Student with last name {last_name} not found.")

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = "\n".join(str(student) for student in self.group)
        return f'Number: {self.number}\n{all_students}'
