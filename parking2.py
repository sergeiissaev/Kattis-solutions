def parking(stores):
    distance = 2 * (max(stores) - min(stores))
    return int(distance)


for k in range(int(input())):
    _ = input()
    print(parking(list(map(int, input().rstrip().split()))))
