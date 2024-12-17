import random


def user_input():
    players = []
    for i in range(1,4):
        player = input(f"Enter player {i} name: ")
        players.append(player)
    
    return players

class Player:
    def __init__(self, name, deck):
        self.name = name
        self.deck = deck
        self.cards = []

    def remove_player(self):
        pass

    def player_cards(self):
        for _ in range(5):
            card = random.choice(self.deck)
            self.deck.remove(card)
            self.cards.append(card)
        return self.cards

    def card_change(self):
        change = input(f"{self.name} - would you like to change a card? Enter 'yes' or 'no': ").lower().strip()
        if change == "yes":
                #print(f"Your cards: {self.cards}")  # ამის სხვაგან დაპრინტვა ხო არ ჯობა?not sure
                card_index = int(input("Enter position of the card you'd like to change: ")) - 1
                if 0 <= card_index < len(self.cards):
                    changed_card = random.choice(self.deck)
                    self.cards[card_index] = changed_card
                else:
                    print("Invalid position. Choose position between 1 and 5")
                    self.card_change(self)
        elif change == "no":
            print("No change")
        else:
            print("Invalid input")
            self.card_change(self)

        return self.cards


class Card():
    def __init__(self):
        self.deck = []

    def deck_generate(self):
        card_list_value = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        card_list_colour = ["♠", "♥", "♦", "♣"]

        for colour in card_list_colour:
            for value in card_list_value:
                self.deck.append(value + colour)
        self.deck = 4 * self.deck

        return self.deck

    def grade_calculation():  # daviti
        pass
        # if tie:
        # extra_comparison()

    def extra_comparison():  # daviti
        pass

    def show_cards(self, cards):
        for card in cards:
            print(card, end=" ")


def main():

    a = Card()
    deck = a.deck_generate()

    player_names = user_input()
    players = [Player(name, deck) for name in player_names]

    for player in players:
        print(f"{player.name}'s cards:", player.player_cards())
    
    for player in players:
        player.card_change()

    print("\nFinal cards:")
    for player in players:
        print(f"{player.name}: ", end="")
        a.show_cards(player.cards)
        print()

if __name__ == "__main__":
    main()
