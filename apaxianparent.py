def create_extended_name(y: str, p: str) -> str:
    """ Extend the input string """
    final_letter = y[-1]
    if final_letter == "e":
        extended_name = y + "x" + p
    elif final_letter in ["a", "i", "o", "u"]:
        extended_name = y[:-1] + "ex" + p
    elif final_letter == "x":
        if y[-2] == "e":
            extended_name = y + p
    else:
        extended_name = y + "ex" + p
    return extended_name

y, p = list(map(str, input().rstrip().split()))
extended_name = create_extended_name(y, p)
print(extended_name)