def expenses(numbers):
    return -sum([entry for entry in numbers if entry < 0])


input()
numbers = list(map(int, input().rstrip().split()))
print(expenses(numbers))
