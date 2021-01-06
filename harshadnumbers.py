def closest(inp):
    while inp:
        sum = 0
        for i in str(inp):
            sum += int(i)
        if inp % sum == 0:
            return inp
        inp += 1


inp = int(input())
print(closest(inp))
