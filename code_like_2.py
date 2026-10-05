luddy_departments = {"INFO": "Informatics", "CSCI": "Computer Science", "ILS": "Information and Library Science", "ENGI": "Intelligent Systems Engineering"}

luddy_students = {"Skye": "INFO", "Kelsey": "INFO", "Aang": "INFO", "Harris": "INFO", "Cleo": "CSCI", "Priya": "CSCI", "Zuko": "CSCI", "Casey": "CSCI", "Aoife": "ILS", "Lena": "ILS", "Carter": "ILS", "Eliza": "ENGI", "Alex": "ENGI", "Ray": "ENGI"}

# print(luddy_departments)

# print(luddy_students)

print(list(luddy_departments))

student_name = input("Please enter a student name to add: ")

department_code = input("What department are they in?: ")

luddy_students[student_name] = department_code 

print(f"There are currently {len(luddy_students)} students in our system.")

print(f"The student name that occurs first in the alphabet is {min(luddy_students)}.")

print(f"The student name that occurs last in the alphabet is {max(luddy_students)}.")

student_name_2 = input("Please enter a student name: ")

print(f"{student_name_2} is in the {luddy_departments[luddy_students[student_name_2]]} department.")


