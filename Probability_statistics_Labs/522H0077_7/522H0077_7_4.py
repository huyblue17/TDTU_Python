import itertools

#EX4
# Create a set to save all the balls
URN = {'W1', 'W2', 'B1', 'B2', 'B3', 'R1', 'R2', 'R3', 'R4'}

# Find the subset of 3 balls from set URN (regardless of the order)
U3 = list(itertools.combinations(URN, 3))

# List all the cases that have 1 white ball, 1 blue ball, and 1 red ball
white1blue1red1 = [subset for subset in U3 if ('W' in subset and 'B' in subset and 'R' in subset)]

# Find the probability of randomly choosing 3 balls with 1 white ball, 1 blue ball, and 1 red ball
P = len(white1blue1red1) / len(U3)

# Print the results
print("Subset of 3 balls from URN (U3):")
print(U3)
print("\nCases with 1 white ball, 1 blue ball, and 1 red ball (white1blue1red1):")
print(white1blue1red1)
print("\nProbability of choosing 3 balls with 1 white ball, 1 blue ball, and 1 red ball (P):")
print(P)