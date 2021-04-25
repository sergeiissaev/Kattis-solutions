def timer(times):
    if len(times) % 2 == 1:
        return 'still running'
    else:
        time = 0
        temp = 0
        for i in range(len(times)):
            if i % 2 == 0:
                temp = times[i]
            else:
                time += (times[i] - temp)
        return time


times = list()
for i in range(int(input())):
    times.append(int(input()))

print(timer(times))


