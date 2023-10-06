import itertools
import random

Ranks = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'}
Suits = {'Heart', 'Diamond', 'Club', 'Spade'}

# Create a list of all possible cards in the deck
Cards = list(itertools.product(Ranks, Suits))

def draw_cards(num_cards):
    # Randomly draw the specified number of cards from the deck
    hand = random.sample(Cards, num_cards)
    return hand

def calculate_probability(event, num_experiments):
    count_event = 0

    for _ in range(num_experiments):
        hand = draw_cards(4)

        # Check if the event occurs in the drawn hand
        if event(hand):
            count_event += 1

    probability = count_event / num_experiments
    return probability

# Define the events we want to calculate probabilities for

# Event: All 4 cards are from the same suit
def is_same_suit(hand):
    suits = set(card[1] for card in hand)
    return len(suits) == 1

# Event: All 4 cards are different suits
def is_different_suits(hand):
    suits = set(card[1] for card in hand)
    return len(suits) == 4

# Event: All 4 cards are same color
def is_same_color(hand):
    colors = set()
    for card in hand:
        if card[1] in ('Heart', 'Diamond'):
            colors.add('Red')
        else:
            colors.add('Black')
    return len(colors) == 1

# Event: All 4 cards are same value
def is_same_value(hand):
    values = set(card[0] for card in hand)
    return len(values) == 1

# Event: All 4 cards are numbers
def is_numbers(hand):
    values = set(card[0] for card in hand)
    return all(isinstance(value, int) for value in values)

# Event: All 4 cards are faces
def is_faces(hand):
    values = set(card[0] for card in hand)
    return values == {'J', 'Q', 'K'}

# Calculate the probabilities

num_experiments = 100

probability_same_suit = calculate_probability(is_same_suit, num_experiments)
probability_different_suits = calculate_probability(is_different_suits, num_experiments)
probability_same_color = calculate_probability(is_same_color, num_experiments)
probability_same_value = calculate_probability(is_same_value, num_experiments)
probability_numbers = calculate_probability(is_numbers, num_experiments)
probability_faces = calculate_probability(is_faces, num_experiments)

# Print the calculated probabilities
print("Practical Probabilities:")
print("All 4 cards are from the same suit:", probability_same_suit)
print("All 4 cards are different suits:", probability_different_suits)
print("All 4 cards are same color:", probability_same_color)
print("All 4 cards are same value:", probability_same_value)
print("All 4 cards are numbers:", probability_numbers)
print("All 4 cards are faces:", probability_faces)