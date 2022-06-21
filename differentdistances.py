class Distances:
    @staticmethod
    def print_p_distances():
        test_case = list(map(float, input().rstrip().split()))
        while test_case != [0]:
            x1, y1, x2, y2, p = test_case
            print(((abs(x1-x2)**p) + (abs(y1-y2)**p))**(1/p))
            test_case = list(map(float, input().rstrip().split()))


if __name__ == "__main__":
    distance = Distances()
    distance.print_p_distances()