class Eligibility:
    def __init__(self):
        self._determine_eligibility()

    def _determine_eligibility(self):
        for _ in range(int(input())):
            name, enrolment_date, birth_date, courses = list(map(str, input().rstrip().split()))
            eligibility = self._eligibility_check(enrolment_date=enrolment_date, birth_date=birth_date, courses=int(courses))
            print(f"{name} {eligibility}")

    def _eligibility_check(self, enrolment_date: str, birth_date: str, courses: int):
        if int(enrolment_date[:4]) >= 2010 or int(birth_date[:4]) >= 1991:
            return "eligible"
        elif courses > 40:
            return "ineligible"
        else:
            return "coach petitions"


if __name__ == "__main__":
    Eligibility()