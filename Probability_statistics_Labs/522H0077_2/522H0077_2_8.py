import itertools

def calculate_probability():
    total = 23
    ball_select = 6

    total_ball = list(itertools.combinations(['W']*8 + ['B']*6 + ['R']*9, ball_select))

    favorable_count = 0

    for combination in total_ball:
        if (combination.count('W') == 2 and combination.count('B') == 2 and combination.count('R') == 2):
            favorable_count += 1

    probability = favorable_count / len(total_ball)
    return probability

res = calculate_probability()
print("Result: ", res)
