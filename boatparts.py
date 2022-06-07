class BoatPart:
    def __init__(self):
        print(self._determine_day())

    def _determine_day(self):
        P, N = list(map(int, input().rstrip().split()))
        parts_list = set()
        for day in range(N):
            part = input()
            parts_list.add(part)
            if len(parts_list) == P:
                return day + 1
        return "paradox avoided"


if __name__ == '__main__':
    BoatPart()
