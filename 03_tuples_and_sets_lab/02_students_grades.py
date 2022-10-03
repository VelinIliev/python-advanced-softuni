number_of_students = int(input())

students = {}

for student in range(number_of_students):
    data = input().split()
    name = data[0]
    grade = float(data[1])
    if name not in students:
        students[name] = []
    students[name].append(grade)

for student, grades in students.items():
    average = sum(grades) / len(grades)
    print(f'{student} ->', end=" ")
    for grade in grades:
        print(f'{grade:.2f}', end=" ")
    print(f'(avg: {average:.2f})')
