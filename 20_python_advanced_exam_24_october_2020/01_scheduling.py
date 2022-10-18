jobs = [int(x) for x in input().split(", ")]
index = int(input())

number_to_compare = jobs[index]
processes = [x for x in jobs[:index] if x <= number_to_compare]
processes2 = [x for x in jobs[index:] if x < number_to_compare]
all_jobs = processes + processes2 + [number_to_compare]
print(sum(all_jobs))

