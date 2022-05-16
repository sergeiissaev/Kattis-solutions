class DiceGame:
    def __init__(self):
        gunnar_score = self._calculate_average_roll()
        emma_score = self._calculate_average_roll()
        if gunnar_score == emma_score: print("Tie")
        elif gunnar_score > emma_score: print("Gunnar")
        else: print("Emma")

    def _calculate_average_roll(self) -> int:
        a1, b1, a2, b2 = list(map(int, input().rstrip().split()))
        return (((b1-a1) / 2) + a1) + (((b2-a2) / 2) + a2)


if __name__ == "__main__":
    DiceGame()