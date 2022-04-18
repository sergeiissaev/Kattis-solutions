class Skocimis:
    def __init__(self):
        positions = list(map(int, input().rstrip().split()))
        self._calculate_maximum_playtime(positions=positions)

    @staticmethod
    def _calculate_maximum_playtime(positions: list) -> None:
        '''Find the maximum distance between the outer points and the inner point'''
        print(max(positions[2] - positions[1], positions[1] - positions[0]) - 1)


if __name__ == "__main__":
    Skocimis()