class TaiFormula:
    def __init__(self):
        self._read_inputs()
        self._calculate_area()


    def _read_inputs(self):
        """Obtain inputs"""
        self.data = list()
        for _ in range(int(input())):
            self.data.append(list(map(float, input().rstrip().split())))
        return self

    def _calculate_area(self):
        "Loop over all trapezoids"
        area = 0
        for idx in range(1, len(self.data)):
            glucose_change = (self.data[idx][1] + self.data[idx - 1][1])/2
            time_change = (self.data[idx][0] - self.data[idx - 1][0]) / 1000
            trapezoid_area = glucose_change * time_change
            area += trapezoid_area
        print(area)


if __name__ == "__main__":
    TaiFormula()