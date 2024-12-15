import random


def user_input():
    pass

class Player:
    def __init__(self,name):
        self.name = name

    def remove_player(self):
        pass 
    
    def player_cards(self,cards):
        pass

    def card_change():
        pass



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

    def grade_calculation():
        pass

    def extra_comparison():
        pass
    
    def show_cards():
        pass


def main():
    a = Card()
    print(a.deck_generate())
    


if __name__ == "__main__":
    main()