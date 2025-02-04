"""
Name: Connor Morrison
NSID: tvi340
Student Number: 11374770
Course Number: CMPT 145
Lecture Section: 04
Laboratory Section: L02
"""

import a3q4 as C


def close_enough(a, b, tolerance=0.0001):
    """
    Purpose:
        Check if 2 floating point values are close enough to be considered equal.
    Pre-Conditions:
        :param a: a floating point value
        :param b: a floating point value
        :param tolerance: a small positive floating point value
    Post-Conditions:
        none
    Return:
        :return: True if the difference between a and b is small
    """
    return abs(a - b) < tolerance


# Test create() method
def test_create_deck():
    """
    Purpose:
        Test create() method to ensure it generates 52 unique cards.
    Pre-Conditions:
        none
    Post-Conditions:
        Prints error message if the created deck does not contain exactly 52 unique cards.
    Return:
        none
    """
    test_item = 'create()'
    reason = "Creating a full deck of 52 unique cards"
    card_instance = C.Card()
    deck = card_instance.create()
    if len(deck) != 52 or len(set(deck)) != 52:
        print(f'Error in {test_item}: expected 52 unique cards but obtained {len(deck)} with {len(set(deck))} unique cards -- {reason}')


# Test deal method
def test_deal_cards():
    """
    Purpose:
        Test deal() method to ensure it deals specified number of cards to specified number of players.
    Pre-Conditions:
        none
    Post-Conditions:
        Prints error message if number of hands or the number of cards per hand does not match the expected values.
    Return:
        none
    """
    test_item = 'deal()'
    reason = "Dealing cards to players"
    card_instance = C.Card()
    num_cards = 5
    num_players = 3
    hands = card_instance.deal(num_cards, num_players, card_instance.deck)
    if not all(len(hand) == num_cards for hand in hands) or len(hands) != num_players:
        print(f'Error in {test_item}: expected {num_players} hands with {num_cards} cards each but obtained different results -- {reason}')


# Test value method
def test_card_values():
    """
    Purpose:
        Test value() method to ensure it returns the correct value for each card.
    Pre-Conditions:
        none
    Post-Conditions:
        Prints error message if the returned value does not match its expected value.
    Return:
        none
    """
    test_item = 'value()'
    reason = "Getting card values"
    card_instance = C.Card()
    test_cases = [('AS', 1), ('10D', 10), ('KH', 13)]
    for card, expected in test_cases:
        result = card_instance.value(card)
        if result != expected:
            print(f'Error in {test_item}: expected {expected} but obtained {result} -- {reason}')


# Test highest method
def test_highest_card():
    """
    Purpose:
        Test highest() method to ensure it identifies card with the highest value.
    Pre-Conditions:
        none
    Post-Conditions:
        Prints error message if the identified card is not the one with the expected highest value.
    Return:
        none
    """
    test_item = 'highest()'
    reason = "Identifying highest card"
    card_instance = C.Card()
    cards = ['2H', 'KD', '5S', '10C']
    expected = 'KD'
    result = card_instance.highest(cards)
    if result != expected:
        print(f'Error in {test_item}: expected {expected} but obtained {result} -- {reason}')


# Test lowest method
def test_lowest_card():
    """
    Purpose:
        Test lowest() method to ensure it identifies card with the lowest value.
    Pre-Conditions:
        none
    Post-Conditions:
        Prints error message if the identified card is not the one with the expected lowest value.
    Return:
        none
    """
    test_item = 'lowest()'
    reason = "Identifying lowest card"
    card_instance = C.Card()
    cards = ['2H', 'KD', '5S', '10C']
    expected = '2H'
    result = card_instance.lowest(cards)
    if result != expected:
        print(f'Error in {test_item}: expected {expected} but obtained {result} -- {reason}')


# Test average method
def test_average_value():
    """
    Purpose:
        Test average() method to ensure it calculates correct average value of the given cards.
    Pre-Conditions:
        none
    Post-Conditions:
        Prints error message if calculated average does not match the expected average value.
    Return:
        none
    """
    test_item = 'average()'
    reason = "Calculating average value of cards"
    card_instance = C.Card()
    cards = ['2H', '3D', '4S', '5C']
    expected = 3.5  # Average value of 2, 3, 4, 5
    result = card_instance.average(cards)
    if not close_enough(result, expected):
        print(f'Error in {test_item}: expected {expected} but obtained {result} -- {reason}')


##### Additional test cases for invalid input types #####

# Test deal() with more than 52 cards
def test_deal_more_cards_than_available():
    """
    Purpose:
        Test deal() method to ensure it handles more cards than available in the deck.
    Pre-Conditions:
        none
    Post-Conditions:
        Raises a ValueError if asked to deal more cards than available.
    Return:
        none
    """
    test_item = 'deal()'
    reason = "Dealing more cards than available"
    card_instance = C.Card()
    num_cards = 60
    num_players = 1
    try:
        card_instance.deal(num_cards, num_players, card_instance.deck)
        print(f'Error in {test_item}: expected a ValueError for {reason} but did not get one.')
    except ValueError as error:
        print(f'Correctly caught ValueError for {reason}: {error}')


# Test deal() with zero cards
def test_deal_zero_cards():
    """
    Purpose:
        Test deal() method to ensure it handles attempting to deal zero cards.
    Pre-Conditions:
        none
    Post-Conditions:
        Raises a ValueError if asked to deal zero cards.
    Return:
        none
    """
    test_item = 'deal()'
    reason = "Dealing zero cards"
    card_instance = C.Card()
    num_cards = 0
    num_players = 1
    try:
        card_instance.deal(num_cards, num_players, card_instance.deck)
        print(f'Error in {test_item}: expected a ValueError for {reason} but did not get one.')
    except ValueError as error:
        print(f'Correctly caught ValueError for {reason}: {error}')


# Test deal() with zero players
def test_deal_zero_players():
    """
    Purpose:
        Test deal() method to ensure it handles attempting to deal cards to zero players.
    Pre-Conditions:
        none
    Post-Conditions:
        Raises a ValueError if asked to deal cards to zero players.
    Return:
        none
    """
    test_item = 'deal()'
    reason = "Dealing to zero players"
    card_instance = C.Card()
    num_cards = 52
    num_players = 0
    try:
        card_instance.deal(num_cards, num_players, card_instance.deck)
        print(f'Error in {test_item}: expected a ValueError for {reason} but did not get one.')
    except ValueError as error:
        print(f'Correctly caught ValueError for {reason}: {error}')


# Test deal() with negative input values
def test_deal_negative_input():
    """
    Purpose:
        Test deal() method to ensure it handles negative input.
    Pre-Conditions:
        none
    Post-Conditions:
        Raises a ValueError if asked to handle negative inputs.
    Return:
        none
    """
    test_item = 'deal()'
    reason = "Dealing with negative input"
    card_instance = C.Card()
    num_cards = -5
    num_players = -3
    try:
        card_instance.deal(num_cards, num_players, card_instance.deck)
        print(f'Error in {test_item}: expected a ValueError for {reason} but did not get one.')
    except ValueError as error:
        print(f'Correctly caught ValueError for {reason}: {error}')


# Test driver
if __name__ == "__main__":
    """
    Purpose:
        Execute a series of tests for Card class.
    Pre-Conditions:
        The Card class and methods are defined and available for testing.
    Post-Conditions:
        Outputs results of each test case, including error messages for tests designed to validate error handling.
    Return:
        none
    """
    # Standard script testing
    test_create_deck()
    test_deal_cards()
    test_card_values()
    test_highest_card()
    test_lowest_card()
    test_average_value()

    # Test cases for invalid input values
    test_deal_more_cards_than_available()
    test_deal_zero_cards()
    test_deal_zero_players()
    test_deal_negative_input()

    print('*** Test script completed ***')
