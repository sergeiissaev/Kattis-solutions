from collections import Counter

class Hangman:
    def __init__(self):
        self._read_in_lines()

    def _read_in_lines(self):
        self.word = input()
        self.permutation = input()
        return self

    def create_hangman(self):
        self.word = Counter(self.word)
        wrong = 0
        for letter in self.permutation:
            if letter in self.word:
                del self.word[letter]
                if len(self.word) == 0:
                    return "WIN"
            elif letter not in self.word:
                wrong += 1
                if wrong == 10:
                    return "LOSE"


if __name__ == "__main__":
    hangman = Hangman()
    print(hangman.create_hangman())