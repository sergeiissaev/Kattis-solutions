class Karte:
    def __init__(self):
        self.cards = input()

    def print_missing(self):
        history = list()
        suits = dict(P=0, H=0, K=0, T=0)
        for i in range(0, len(self.cards), 3):
            card = self.cards[i:i+3]
            if card in history:
                return "GRESKA"
            history.append(card)
            suits[card[0]] += 1
        return " ".join(str(a) for a in [13-suits[x] for x in ["P", "K", "H", "T"]])


if __name__ == '__main__':
    karte = Karte()
    print(karte.print_missing())