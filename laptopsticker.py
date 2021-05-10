def fit(wc, hc, ws, hs):
    if (wc - ws) > 1 and (hc - hs) > 1:
        return 1
    else:
        return 0


inp = list(map(int, input().rstrip().split()))
print(fit(inp[0], inp[1], inp[2], inp[3]))