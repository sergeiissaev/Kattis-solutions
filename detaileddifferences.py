def comparison(s1, s2):
    #Print original strings
    print(s1)
    print(s2)
    #Make comparison
    for i in range(len(s1)):
        if s1[i] == s2[i]:
            print(".", end = "")
        else:
            print("*", end = "")
    #Print blank line
    print("\n")

for i in range(int(input())):
    s1 = str(input())
    s2 = str(input())
    comparison(s1, s2)
