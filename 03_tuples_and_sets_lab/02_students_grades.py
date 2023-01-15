number_of_students = int(input())

students = {}

for student in range(number_of_students):
    name, grade = input().split()
    if name not in students:
        students[name] = []
    students[name].append(float(grade))

for student, grades in students.items():
    average = sum(grades) / len(grades)
    print(f'{student} -> {" ".join(map(lambda x: f"{x:.2f}", grades))} (avg: {average:.2f})')
