for _ in range(int(input())):
    problem = input()
    if problem == "P=NP": print("skipped")
    else:
        a, b = map(int, problem.split("+"))
        print(a + b)