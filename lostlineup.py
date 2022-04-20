class LostLineUp:
    def __init__(self):
        self._read_input()

    def _read_input(self) -> list:
        '''Read inputs'''
        self.line_length = int(input())
        self.after_position = list(map(int, input().rstrip().split()))
        self._recreate_original_order()
        return self

    def _recreate_original_order(self) -> list:
        '''Recreate original positions in line'''
        self.before_positions = [1]
        for idx in range(self.line_length - 1):
            self.before_positions.append(self.after_position.index(idx) + 2)
        self.before_positions = " ".join(str(num) for num in self.before_positions)
        return self


if __name__ == "__main__":
    lineup = LostLineUp()
    print(lineup.before_positions)