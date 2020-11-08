def outlet(arr):
    return (sum(arr[1:]) - len(arr[1:]) + 1)

for k in range(int(input())):
    print(outlet(list(map(int, input().rstrip().split()))))
