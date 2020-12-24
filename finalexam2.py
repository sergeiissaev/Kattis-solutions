answers = list()
def grade(answers):
   score = 0
   for i in range(1, len(answers)):
      if answers[i] == answers [i - 1]:
         score += 1
   return score

cases = int(input())

for _ in range(cases):
   answers.append(str(input()))

print(grade(answers))
