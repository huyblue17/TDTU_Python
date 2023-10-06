import itertools

#EX2
def calculate_probability(event):
    total = 10
    ball_select = 3

    balls = ['W']*5 + ['B']*2 + ['R']*3

    total_ball = list(itertools.combinations(balls, ball_select))
    event_count = sum(1 for balls in total_ball if event(balls))
    probability = event_count / len(total_ball)

    return probability

# Define the events we want to calculate probabilities for

# Event: All 3 balls are the same color
def all_same_color(balls):
    return len(set(balls)) == 1

# Event: All 3 balls are different colors
def all_different_colors(balls):
    return len(set(balls)) == 3

# Event: Only 2 balls are the same color
def two_same_color(balls):
    return len(set(balls)) == 2

# Event: There are 2 red balls and 1 white ball
def two_red_one_white(balls):
    return balls.count('R') == 2 and balls.count('W') == 1

# Event: All 3 balls are white
def all_white(balls):
    return set(balls) == {'W'}

# Calculate the probabilities

probability_same_color = calculate_probability(all_same_color)
probability_different_colors = calculate_probability(all_different_colors)
probability_two_same_color = calculate_probability(two_same_color)
probability_two_red_one_white = calculate_probability(two_red_one_white)
probability_all_white = calculate_probability(all_white)

# Print the calculated probabilities
print("Practical Probabilities:")
print("All 3 balls are the same color:", probability_same_color)
print("All 3 balls are different colors:", probability_different_colors)
print("Only 2 balls are the same color:", probability_two_same_color)
print("There are 2 red balls and 1 white ball:", probability_two_red_one_white)
print("All 3 balls are white:", probability_all_white)