from collections import deque
import common.util as u
round_count=0
class Deck:

    def __init__(self, cards):
        self.cards = deque(cards)
        #self.deck_history = [ self.getHash(self.cards.copy()) ]
        self.deck_history = []

    def add_to_bottom(self, cards, sort=True):
        if sort:
            sorted_cards = reversed(sorted(cards))
        else:
            sorted_cards = cards
        for card in sorted_cards:
            self.cards.appendleft(card)
        card_history = self.getHash(list(self.cards))
        self.deck_history.append(card_history)
    
    def get_card(self):
        return self.cards.pop()

    def getHash(self, lst):
        tple = tuple(lst.copy())
        return hash(tple)

    def checkHistory(self):
        lst=list(self.cards)
        hsh=self.getHash(lst)
        res = hsh in self.deck_history[:-1]
        return res
        #return (self.getHash(list(self.cards))) in self.deck_history[:-1]

def load_data(fpath):
    with open(fpath, 'r') as f:
        data = f.read()
    decks = data.split("\n\n")
    deck1_cards = decks[0].split("\n")[1:]
    deck2_cards = decks[1].split("\n")[1:]
    deck1_cards = [ int(card) for card in deck1_cards ]
    deck2_cards = [ int(card) for card in deck2_cards ]
    deck1 = Deck(reversed(deck1_cards))
    deck2 = Deck(reversed(deck2_cards))
    return deck1, deck2


def play_game(deck1, deck2, gn):
    global round_count
    while True:
        round_count+=1
        
        if len(deck1.cards) == 0:
            return 2, deck1, deck2
        if len(deck2.cards) == 0:
            return 1, deck1, deck2
        card1 = deck1.get_card()
        card2 = deck2.get_card()
        if deck1.checkHistory():
            return 1, deck1, deck2
        if deck2.checkHistory():
            return 1, deck1, deck2

        print(f"{round_count}:{list(deck1.cards)[::-1]}{list(deck2.cards)[::-1]}")

 

        if card1 > len(deck1.cards) or card2 > len(deck2.cards):
            if card1 > card2:
                deck1.add_to_bottom([card1, card2])
            else:
                deck2.add_to_bottom([card1, card2])
        else:
            subdeck1 = Deck(list(deck1.cards)[-card1:].copy())
            subdeck2 = Deck(list(deck2.cards)[-card2:].copy())
            result, subdeck1, subdeck2 = play_game(subdeck1, subdeck2, gn+1)
            print("")
            if result == 1:
                deck1.add_to_bottom([card1, card2], False)
            else:
                deck2.add_to_bottom([card2, card1], False)
        if round_count > 10000 and gn == 0:
            print("Round_count threshold")
            exit(0)
        

def main():
    deck1, deck2 = load_data(u.AOC_2020 + "\\22\\input.txt")
    result, deck1, deck2 = play_game(deck1, deck2, 0)
    if result == 1:
        points = 0
        for i, item in enumerate(list(deck1.cards)):
            print(f"{i+1}*{item} {points}")
            points += (i+1)*item
    else:
        points = 0
        for i, item in enumerate(list(deck2.cards)):
            print(f"{i+1}*{item} {points}")
            points += (i+1)*item
    print(points)
    print(round_count)


if __name__ == "__main__":
    main()


# players = [
# [12,48,26,22,44,16,31,19,30,10,40,47,21,27,2,46,9,15,23,6,50,28,5,42,34],
# [14,45,4,24,1,7,36,29,38,33,3,13,11,17,39,43,8,41,32,37,35,49,20,18,25]
# ]