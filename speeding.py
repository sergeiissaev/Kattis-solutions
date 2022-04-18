class Speeding:
    def __init__(self):
        self.max_speed = 0
        self.prev_t = 0
        self.prev_d = 0
        self._loop_over_datapoints()

    def _loop_over_datapoints(self):
        '''Loop over inputs'''
        for _ in range(int(input())):
            t, d = list(map(int, input().rstrip().split()))
            self._calculate_max_speed(t=t, d=d)
        print(self.max_speed)

    def _calculate_max_speed(self, t: int, d: int):
        '''Replace max speed with new speed if new speed is greater'''
        if t != 0:
            speed = int((d - self.prev_d) / (t - self.prev_t))
            if speed > self.max_speed:
                self.max_speed = speed
            self.prev_d = d
            self.prev_t = t


if __name__ == "__main__":
    Speeding()