class Soda:
    def __init__(self):
        e, f, c = self._read_input()
        count = self._calculate_empty_bottles(e=e, f=f, c=c)
        print(count)

    @staticmethod
    def _read_input() -> list:
        return list(map(int, input().rstrip().split()))

    def _calculate_empty_bottles(self, e: int,  f: int, c: int) -> int:
        count = 0
        e += f
        while e >= c:
            div, mod = divmod(e, c)
            count += div
            e = div + mod
        return count


if __name__ == "__main__":
    Soda()