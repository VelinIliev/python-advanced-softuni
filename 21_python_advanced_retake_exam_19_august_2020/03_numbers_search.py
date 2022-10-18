def numbers_searching(*args):
    check_for_missing = set(sorted(args))
    first = min(check_for_missing)
    last = max(check_for_missing)
    full_list = [x for x in range(first, last + 1)]
    missing = list(set(full_list) - check_for_missing)
    # print(missing)

    duplicates = []
    find_duplicates = set(args)
    for x in find_duplicates:
        if args.count(x) > 1:
            duplicates.append(x)

    return [*missing, sorted(duplicates)]

print(numbers_searching(1, 2, 4, 2, 5, 4))
print()
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print()
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))