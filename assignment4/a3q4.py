"""
Name: Connor Morrison
NSID: tvi340
Student Number: 11374770
Course Number: CMPT 145
Lecture Section: 04
Laboratory Section: L02
"""

import random


class Card:
    def __init__(self):
        """
        Purpose:
            Initialize a Card instance.
        Pre-Conditions:
            none
        Post-Conditions:
            Deck of 52 cards is created and stored in the instance variable 'deck'.
        Return:
            none
        """
        self.deck = self.create()

    def create(self):
        """
        Purpose:
            Generate a deck of 52 playing cards.
        Pre-Conditions:
            none
        Post-Conditions:
            Creates a list representing a deck of cards with each card a string combining its value and suit.
        Return:
            A list of strings, each string representing a card (e.g., 'AS', '10D').
        """
        suits = ['H', 'D', 'S', 'C']
        values = ['A']

        for v in range(2, 11):
            values.append(str(v))

        # Append face cards
        values += ['J', 'Q', 'K']
        deck = []
        for suit in suits:
            for value in values:
                card = value + suit
                deck.append(card)

        return deck

    def deal(self, num_cards, num_players, deck):
        """
        Purpose:
            Deal a specified number of cards to a specified number of players from the deck.
        Pre-Conditions:
            :param num_cards: An integer, the number of cards to deal to each player.
            :param num_players: An integer, the number of players to deal cards to.
            :param deck: A list of strings, each representing a card.
        Post-Conditions:
            Cards are removed from the deck as they are dealt to each player.
        Return:
            Nested list, where each inner list represents a player's cards.
        """
        # Handle invalid inputs
        if num_cards < 0 or num_players < 0:
            raise ValueError("Number of cards and number of players cannot be negative.")
        if num_players == 0 or num_cards == 0:
            raise ValueError("Number of cards and number of players cannot be zero.")
        if len(deck) < num_cards * num_players:
            raise ValueError("Not enough cards to deal to all players.")

        self.deck = deck
        hands = []
        for player_index in range(num_players):
            hands.append([])

        for card_number in range(num_cards):
            for hand in hands:
                if not self.deck:  # Check deck not empty
                    break  # Stop dealing if are no cards left
                card_index = random.randint(0, len(self.deck) - 1)  # Select random card index
                hand.append(self.deck.pop(card_index))  # Remove card from the deck and add it to player's hand

        return hands

    def value(self, card):
        """
        Purpose:
            Determine the numerical value of a given card.
        Pre-Conditions:
            :param card: A string representing a card (e.g., 'AS', '10D').
        Post-Conditions:
            none
        Return:
            An integer representing the numerical value of the card.
        """
        value_dict = {'A': 1,
                      '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
                      'J': 11, 'Q': 12, 'K': 13}
        value, suit = card[:-1], card[-1]

        return value_dict[value]  # Use value_dict for all card values

    def highest(self, list_of_cards):
        """
        Purpose:
            Find the highest valued card in a list of cards.
        Pre-Conditions:
            :param list_of_cards: A list of strings, each representing a card (e.g., 'AS', '10D').
        Post-Conditions:
            none
        Return:
            A string representing the highest valued card in the given list.
        """
        return max(list_of_cards, key=self.value)

    def lowest(self, list_of_cards):
        """
        Purpose:
            Find the lowest valued card in a list of cards.
        Pre-Conditions:
            :param list_of_cards: A list of strings, each representing a card (e.g., 'AS', '10D').
        Post-Conditions:
            none
        Return:
            A string representing the lowest valued card in the given list.
        """
        return min(list_of_cards, key=self.value)

    def average(self, list_of_cards):
        """
        Purpose:
            Calculate the average value of a given list of cards.
        Pre-Conditions:
            :param list_of_cards: A list of strings, each representing a card (e.g., 'AS', '10D').
        Post-Conditions:
            none
        Return:
            A float representing the average numerical value of the given list of cards. Returns 0 if the list is empty.
        """
        values = []

        for card in list_of_cards:
            card_value = self.value(card)
            values.append(card_value)

        if values:
            return sum(values) / len(values)
        else:
            return 0


# Example usage
if __name__ == "__main__":
    """
    Purpose:
        Demonstrate the usage of the Card class.
    Pre-Conditions:
        Card class defined with methods create(), deal(), value(), highest(), lowest(), and average().
    Post-Conditions:
        Prints the initial deck, the hands dealt to players, and the highest, lowest, and average card values from a sample hand. 
        This demonstrates the functionality of the Card class.
    Return:
        none
    """
    card_instance = Card()
    print(card_instance.deck)

    cards_dealt = card_instance.deal(5, 3, card_instance.deck)
    print(cards_dealt)

    highest_card = card_instance.highest(["5D", "10H", "QS", "8C", "JH"])  # Assignment example
    print(highest_card)  # outputs: "QS"

    lowest_card = card_instance.lowest(["5D", "10H", "QS", "8C", "JH"])  # Assignment example
    print(lowest_card)  # outputs: "5D"

    average_value = card_instance.average(["5D", "10H", "QS", "8C", "JH"])  # Assignment example
    print(average_value)  # outputs: 9.2