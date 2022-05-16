class Award:
    def __init__(self):
        input()
        self._print_winners()

    def _print_winners(self):
        awarded = 0
        awarded_list = list()
        while awarded < 12:
            institution, team = list(map(str, input().rstrip().split()))
            if institution not in awarded_list:
                awarded_list.append(institution)
                awarded += 1
                print(f"{institution} {team}")


if __name__ == "__main__":
    Award()