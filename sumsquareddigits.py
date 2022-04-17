class SumSquareDigits:
    def __init__(self):
        self._loop_over_inputs()

    def _loop_over_inputs(self):
        for _ in range(int(input())):
            dataset, b, n = list(map(int, input().rstrip().split()))
            self._calculate_ssd(dataset, b, n)

    @staticmethod
    def _calculate_ssd(dataset: int, b: int, n: int) -> None:
        list_of_a_squared = list()
        while n > 0:
            a = n % b
            list_of_a_squared.append(a ** 2)
            n //= b
        print(f"{dataset} {sum(list_of_a_squared)}")


if __name__ == "__main__":
    SumSquareDigits()