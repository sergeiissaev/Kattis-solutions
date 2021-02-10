def simon(input):
    return ' '.join(x for x in inp[2:])


for comm in range(int(input())):
    inp = list(map(str, input().rstrip().split()))
    if inp[0] == 'Simon' and inp[1] == 'says':
        print(simon(inp))