def add_days_to_set(event: list, food_days: set) -> set:
    ''' Add range of days to the set of existing food days '''
    for day in range(event[0], event[1] + 1):
        food_days.add(day)
    return food_days


food_days = set()
number_of_events = int(input())
for _ in range(number_of_events):
    event = list(map(int, input().rstrip().split()))
    food_days = add_days_to_set(event, food_days)
print(len(food_days))
