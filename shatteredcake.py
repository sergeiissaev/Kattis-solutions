width = int(input())
total = 0
for i in range(int(input())):
    piece = list(map(int, input().rstrip().split()))
    total += piece[0] * piece[1]

print(int(total / width))