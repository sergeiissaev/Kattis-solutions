import math


class Prsteni:
    def __init__(self):
        input()
        self.rings = list(map(int, input().rstrip().split()))

    def print_fractions(self):
        ref = self.rings[0]
        for radius in self.rings[1:]:
            gcd = math.gcd(radius, ref)
            print(f"{int(ref/gcd)}/{int(radius/gcd)}")


if __name__ == "__main__":
    prsteni = Prsteni()
    prsteni.print_fractions()

