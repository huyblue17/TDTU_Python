import random
import itertools

# Create a set of cards
suits = ['Heart', 'Spade', 'Club', 'Diamond']
ranks = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
Cards = {rank + suit for suit in suits for rank in ranks}

# Randomly collect 3 cards
B = set(random.sample(Cards, 3))

# Define events A1 and A2
A1 = {s for s in itertools.combinations(B, 3) if s.count('K') >= 1}
A2 = {s for s in itertools.combinations(Cards, 3) if s.count('K') >= 1}

# Calculate probabilities
P_A1 = len(A1) / len(Cards)**3
P_A2 = len(A2) / len(Cards)**3

print("a.Cards:", Cards)
print("b.B:", B)
print("c.A1:", A1)
print("d.A2:", A2)
print("e1.Probability of event A1:", P_A1)
print("e2.Probability of event A2:", P_A2)