import math


def arrangements(states):
    limit = math.ceil(states // 2)
    #print(f"limit is {limit}")
    ret = str(states) + ":\n"
    for i in range(2, limit + 2):
        #print(f"i = {i}")
        #print(f"checking {states} % {(i + i - 1)} = {(states % (i + i - 1))}...")
        if states % (i + i - 1) == (i):
            #print('case 1')
            sos = str(i) + "," + str(i - 1) + "\n"
            #print(sos)
            ret += sos
        if states % (i + i - 1) == 0:
            #print('case 2')
            tos = str(i) + "," + str(i - 1) + "\n"
            ret += tos
            #print(tos)
        if states % i == 0:
            val = (str(i) + "," + str(i) + "\n")
            ret += val
            #print(val)
    return ret


print(arrangements(int(input())))