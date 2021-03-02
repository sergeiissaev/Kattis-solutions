def options(features):
    return features[0] * features[1] * features[2]


features = list(map(int, input().rstrip().split()))
print(options(features))