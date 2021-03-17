def ispossible(nums):
    one, two, three = nums
    if one + two == three:
        return 'Possible'
    elif one * two == three:
        return 'Possible'
    elif one - two == three:
        return 'Possible'
    elif two - one == three:
        return 'Possible'
    elif one / two == three:
        return 'Possible'
    elif two / one == three:
        return 'Possible'
    return 'Impossible'


for inp in range(int(input())):
    nums = list(map(int, input().rstrip().split()))
    print(ispossible(nums))