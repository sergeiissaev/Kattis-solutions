def limit(turtles):
    lower = 0
    for i in range(1, len(turtles) - 1):
        lower += max((turtles[i] - (turtles[i - 1]) * 2), 0)
    return lower


for i in range(int(input())):
    print(limit(list(map(int, input().rstrip().split()))))
