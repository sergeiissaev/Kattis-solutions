def list_to_int(num1: list) -> int:
    int1 = ""
    for val in num1:
        int1 += val
    return int(int1)



for testcase in range(int(input())):
    num1 = list_to_int(input().rstrip().split())
    num2 = list_to_int(input().rstrip().split())
    ret = num1 + num2
    spaced = ""
    for i in str(ret):
        spaced += f"{i} "
    print(spaced)