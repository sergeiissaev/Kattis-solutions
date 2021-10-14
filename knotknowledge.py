def find_diff(need, have):
    return list(set(need) - set(have))[0]

input()
need = list(map(int, input().rstrip().split()))
have = list(map(int, input().rstrip().split()))
missing = find_diff(need, have)
print(missing)
