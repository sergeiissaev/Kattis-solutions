import math

class Solution:
    def __init__(self):
        self.pickup_time = 1
        self.running_speed = 15
        self.circle = "ABCDEFGHIJKLMNOPQRSTUVWXYZ '"
        self.distance_between_letters = 2 * math.pi * 30 / 28
        self.n = int(input())
        self.aphorisms = list()
        for i in range(self.n):
            self.aphorisms.append(str(input().rstrip()))
        self.calculate_time_aphorisms()

    def find_length_to_next_letter(self, current_letter: str, next_letter: str) -> int:
        """ Given two letters find the smallest distance between them """
        current_pos = self.circle.find(current_letter)
        next_pos = self.circle.find(next_letter)
        distance = min(abs(current_pos - next_pos), 28 - abs(current_pos - next_pos))
        return distance

    def calculate_time(self, aphorism: str):
        """ Given an aphorism calculate the time to pick up all the letters """
        total_distance = 0
        for letter_idx in range(len(aphorism) - 1):
            distance = self.find_length_to_next_letter(current_letter=aphorism[letter_idx], next_letter=aphorism[letter_idx + 1])
            total_distance += distance
        total_distance = total_distance * self.distance_between_letters
        time_running = total_distance / self.running_speed
        time_stops = len(aphorism)
        total_time = time_stops + time_running
        print(f"{total_time}")
        return total_time


    def calculate_time_aphorisms(self):
        for i in self.aphorisms:
            _ = self.calculate_time(i)


mySolution = Solution()

