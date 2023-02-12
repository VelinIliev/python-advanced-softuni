def students_credits(*args):
    courses = {}
    total_credits = 0
    CREDITS_FOR_DIPLOMA = 240

    for data in args:
        course_name, course_credits, max_points, diyan_points = [int(x) if x.isnumeric() else x for x in data.split("-")]
        diyan_credits = (diyan_points / max_points) * course_credits
        courses[course_name] = diyan_credits
        total_credits += diyan_credits

    return_list = []
    if total_credits >= CREDITS_FOR_DIPLOMA:
        return_list.append(f'Diyan gets a diploma with {total_credits:.1f} credits.')
    else:
        credits_needed = CREDITS_FOR_DIPLOMA - total_credits
        return_list.append(f'Diyan needs {credits_needed:.1f} credits more for a diploma.')
    sorted_courses = sorted(courses.items(), key=lambda x: -x[1])
    for course, credit in sorted_courses:
        return_list.append(f'{course} - {credit:.1f}')
    return '\n'.join(return_list)


print(
    students_credits(
        "Computer Science-12-300-250",
        "Basic Algebra-15-400-200",
        "Algorithms-25-500-490"
    )
)

print(
    students_credits(
        "Discrete Maths-40-500-450",
        "AI Development-20-400-400",
        "Algorithms Advanced-50-700-630",
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Game Engine Development-70-100-70",
        "Mobile Development-25-250-225",
        "QA-20-300-300",
    )
)

print(
    students_credits(
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Java Development-10-300-150"
    )
)

