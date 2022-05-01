import math


class EstimateArea:
    def __init__(self):
        self._read_inputs()

    def _read_inputs(self):
        while True:
            self.testcase = list(map(float, input().rstrip().split()))
            if self.testcase == [0.0, 0.0, 0.0]:
                break
            else:
                self._return_radii()

    def _return_radii(self):
        r, m, c = self.testcase
        pi_estimate = 4 * c / m
        true_radius = math.pi * r * r
        estimated_radius = pi_estimate * r * r
        print(f"{true_radius} {estimated_radius}")


if __name__ == "__main__":
    EstimateArea()
