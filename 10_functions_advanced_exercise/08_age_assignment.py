def age_assignment(*args, **kwargs):
    persons = {}
    for name in args:
        persons[name] = 0
    for first_letter, age in kwargs.items():
        for person in persons:
            if person.startswith(first_letter):
                persons[person] = age
    return "\n".join(f'{x[0]} is {x[1]} years old.' for x in sorted(persons.items()))


print(age_assignment("Peter", "George", G=26, P=19))

print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))