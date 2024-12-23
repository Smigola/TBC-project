import random


def user_input():  # bachana
    pass
    # davanamatot card change funqcionali


class Player:
    def __init__(self, name, deck):
        self.name = name
        self.deck = deck
        self.cards = []
    
    def remove_player(self):
        pass
    
    def player_cards(self):  # checkinggggg
        for _ in range(5):
            card = random.choice(self.deck)
            self.cards.append(card)
        return self.cards
    
    def show_cards(self, cards):  # mariami
        print("Current cards: ", end="")
        for card in cards:
            print(card, end=" ")
        print()
    
    def card_change(self):  # mariami
        self.show_cards(self.cards)
        change = input("Would you like to change a card? Enter 'yes' or 'no': ").lower().strip()
        
        if change == "yes":
            card_index = int(input("Enter position of the card you'd like to change: ")) - 1
            if 0 <= card_index < len(self.cards):
                changed_card = random.choice(self.deck)
                self.cards[card_index] = changed_card
                self.show_cards(self.cards)
            else:
                print("Invalid position. Choose position between 1 and 5")
                print()
                Player.card_change(self)
        elif change == "no":
            print("No change")
        else:
            print("Invalid input")
            print()
            Player.card_change(self)
        
        return self.cards


class Card:
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
    
    def grade_calculation(self):  # daviti
        pass
        # if tie:
        # extra_comparison()
    
    def extra_comparison(self):  # daviti
        pass


def main():
    a = Card()
    deck = a.deck_generate()
    
    p = Player(name="aa", deck=deck)
    p.player_cards()
    p.card_change()
    
    # .show_cards(p.cards)
    print(p.cards)


if __name__ == "__main__":
    main()