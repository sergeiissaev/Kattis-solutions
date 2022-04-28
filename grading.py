def convert_to_letter_grade(cutoffs: list, grade: int, mapping: list) -> str:
    for cutoff in range(len(cutoffs)):
        if grade >= cutoffs[cutoff]:
            return mapping[cutoff]
    return "F"


cutoffs = list(map(int, input().rstrip().split()))
grade = int(input())
mapping = ["A", "B", "C", "D", "E"]

print(convert_to_letter_grade(cutoffs=cutoffs, grade=grade, mapping=mapping))

