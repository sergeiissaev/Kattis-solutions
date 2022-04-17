class SumKindOfProblem:
    def __init__(self):
        self._loop_over_datasets()

    def _loop_over_datasets(self):
        for _ in range(int(input())):
            k, n = list(map(int, input().rstrip().split()))
            self._calculate_sums(k=k, n=n)

    @staticmethod
    def _calculate_sums(k: int, n: int):
        sum_positive = int((n*(n+1)) / 2)
        sum_odd = n * n
        sum_even = n * (n+1)
        print(f"{k} {sum_positive} {sum_odd} {sum_even}")


if __name__ == "__main__":
    SumKindOfProblem()