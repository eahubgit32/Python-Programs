def find_duplicates(arr):

    seen = set()
    duplicate = set()

    for numbers in arr:
        if numbers in seen:
            duplicate.add(numbers)
        else:
            seen.add(numbers)

    return sorted(list(duplicate))


print(find_duplicates([2, 34, 0, 1, -6, 23, 5, 3, 2, 5, 67, -6, 23, 2, 43, 2, 12, 0, 2, 4, 4]))


