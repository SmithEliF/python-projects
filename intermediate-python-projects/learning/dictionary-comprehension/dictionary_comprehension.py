# Dictionary comprehension

import random

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

grades = {student : random.randint(0,100) for student in names}

passed_students = {student : grade for (student, grade) in grades.items() if grade >= 60}

print(grades)

print(passed_students)