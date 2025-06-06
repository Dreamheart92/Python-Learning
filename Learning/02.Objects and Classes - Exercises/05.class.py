from functools import reduce


class Class:
    __students_count = 22

    def __init__(self, name: str):
        self.name = name
        self.students = []
        self.grades = []

    def add_student(self, name: str, grade: float):
        students_counts = len(self.students)
        if students_counts < Class.__students_count:
            self.students.append(name)
            self.grades.append(grade)

    def get_average_grade(self):
        sum_grades = reduce(lambda acc, x: acc + x, self.grades)
        total_grades = len(self.grades)
        return round(sum_grades / total_grades, 2)

    def __repr__(self):
        return f"The students in {self.name}: {', '.join(self.students)}. Average grade: {self.get_average_grade()}"


a_class = Class("11B")

a_class.add_student("Peter", 4.80)

a_class.add_student("George", 6.00)

a_class.add_student("Amy", 3.50)

print(a_class)
