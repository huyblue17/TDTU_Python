import itertools

#EX5
def calculate_theoretical_probability():
    total_straights = 0
    total_combinations = 0

    # Generate all possible combinations of 5 cards from a deck of 52 cards
    combinations = itertools.combinations(range(1, 53), 5)

    for hand in combinations:
        # Check if the hand forms a straight
        if is_straight(hand):
            total_straights += 1

        total_combinations += 1

    probability = total_straights / total_combinations
    return probability

def is_straight(hand):
    # Sort the hand in ascending order
    hand = sorted(hand)

    # Check if the hand forms a straight
    for i in range(1, len(hand)):
        if hand[i] != hand[i-1] + 1:
            return False

    return True

# Calculate the theoretical probability
theoretical_probability = calculate_theoretical_probability()

# Print the result
print("Theoretical Probability:", theoretical_probability)