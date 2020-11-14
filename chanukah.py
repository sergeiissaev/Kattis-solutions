def candles(arr):
    case, days = arr[0], arr[1]
    candles = int(1/2 * ((3 * days) + (days ** 2)))
    return str(str(case) + " " +  str(candles))


for k in range(int(input())):
    print(candles(list(map(int, input().rstrip().split()))))