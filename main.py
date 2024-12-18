import random


def user_input():
    players = []
    try:
        for i in range(1, 4):
            while True:
                player = input(f"Enter player {i} name: ").strip()
                if not player:
                    print("empty name, please try again.")
                elif not player.isalpha():
                    print("Player name can only contain letters. Please try again.")
                elif player in players:
                    print("Duplicate name detected. Please use different names")
                else:
                    players.append(player)
                    break
    except Exception as e:
        print(f"An error occurred: {e}")

    return players


class Player:
    def __init__(self, name, deck):
        self.name = name
        self.deck = deck
        self.cards = []

    def player_cards(self):
        self.cards = []
        for _ in range(5):
            card = random.choice(self.deck)
            self.deck.remove(card)
            self.cards.append(card)
        return self.cards

    def show_initial_cards(self):
        print(f"{self.name}'s cards: ", end="")
        for card in self.cards:
            print(card, end=" ")
        print()

    def card_change(self):
        print()
        self.show_initial_cards()
        change = input(f"{self.name} - would you like to change a card? Enter 'yes' or 'no': ").lower().strip()
        if change == "yes":
            card_index = int(input("Enter position of the card you'd like to change: ")) - 1
            if 0 <= card_index < len(self.cards):
                changed_card = random.choice(self.deck)
                self.cards[card_index] = changed_card
                print("Updated cards:")
                self.show_initial_cards()
            else:
                print("Invalid position. Choose position between 1 and 5")
                self.card_change()
        elif change == "no":
            print("No change")
        else:
            print("Invalid input")
            self.card_change()
        return self.cards


class Card:
    def __init__(self):
        self.deck = []

    def deck_generate(self):
        card_list_value = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        card_list_colour = ["\u2660", "\u2665", "\u2666", "\u2663"]
        self.deck = []

        for colour in card_list_colour:
            for value in card_list_value:
                self.deck.append(value + colour)
        self.deck = 4 * self.deck

        return self.deck

    def grade_by_value(self, hand):
        value_map = {
            '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
            'J': 11, 'Q': 12, 'K': 13, 'A': 20
        }
        return sum(value_map[card[:-1]] for card in hand)

    def grade_by_color(self, hand):
        colors_count = {}
        for card in hand:
            c = card[-1]
            if c not in colors_count:
                colors_count[c] = 0
            colors_count[c] = colors_count[c] + 1
        return max(colors_count.values())

    def grade_by_card(self, hand):
        same_count = {}
        for card in hand:
            c = card[0]
            if c not in same_count:
                same_count[c] = 0
            same_count[c] = same_count[c] + 1
        return max(same_count.values())

    def get_result(self, players):
        scores = {}
        for player in players:
            scores[player] = [
                self.grade_by_value(player.cards),
                self.grade_by_color(player.cards),
                self.grade_by_card(player.cards)
            ]

        for i in range(2):
            max_score = max(value[0] for value in scores.values())
            scores = {key: value for key, value in scores.items() if value[0] == max_score}

        loser = [player for player in players if player not in scores.keys()]

        return list(scores.keys()),loser
    
    def show_changed_cards(self, cards):
        for card in cards:
            print(card, end=" ")


def play_game(players, card_deck):
    for player in players:
        player.player_cards()
        player.show_initial_cards()

    for player in players:
        player.card_change()

    print("\nFinal cards:")
    for player in players:
        print(f"{player.name}: ", end="")
        card_deck.show_changed_cards(player.cards)
        print()

    winners,losers = card_deck.get_result(players)
    
    print("Eliminated:")
    for loser in losers:
        print(loser.name, end = " ")
    print()

    return winners


def main():
    card_deck = Card()
    deck = card_deck.deck_generate()

    player_names = user_input()
    players = [Player(name, deck) for name in player_names]
    winners = play_game(players, card_deck)
    while len(winners) > 1:
        print("Tie! start new round!")
        deck = card_deck.deck_generate()
        for player in players:
            player.deck = deck

        players = winners
        winners = play_game(players, card_deck)


    print(f"Winner: {winners[0].name}")



if __name__ == "__main__":
    main()