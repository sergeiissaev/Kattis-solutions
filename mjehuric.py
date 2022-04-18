class Mjehuric:
    def __init__(self):
        self.layout = list(map(int, input().rstrip().split()))
        self._print_swaps()

    def _print_swaps(self) -> None:
        '''Swap elements one at a time'''
        while self.layout != [1,2,3,4,5]:
            for idx in range(4):
                index_plus1 = self.layout[idx + 1]
                if self.layout[idx] > index_plus1:
                    self.layout[idx + 1] = self.layout[idx]
                    self.layout[idx] = index_plus1
                    print(" ".join(str(num) for num in self.layout))


if __name__ == "__main__":
    Mjehuric()