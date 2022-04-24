class Skener:
    def __init__(self):
        self._set_params()
        for row in range(self.r):
            self._print_scanned_line()

    def _print_scanned_line(self):
        line = input()
        ret = ""
        for char in line:
            ret += char * self.zc
        for multiple in range(self.zr):
            print(ret)

    def _set_params(self):
        self.r, self.c, self.zr, self.zc = list(map(int, input().rstrip().split()))
        return self


if __name__ == "__main__":
    Skener()