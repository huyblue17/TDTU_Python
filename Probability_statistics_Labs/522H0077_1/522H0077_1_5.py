import itertools

#EX5
print("EX5")

suits = ['Spade', 'Club', 'Diamond', 'Heart']
ranks = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

cards = []

for suit in suits:
    for rank in ranks:
        cards.append((rank, suit))

poker_5 = list(itertools.combinations(cards, 5))

#a
len_poker_5 = len(poker_5)
#a.
print("a.: ", len_poker_5)

#b
three_of_a_kind = []

for hand in poker_5:
    ranks = [card[0] for card in hand]
    unique_ranks = set(ranks)
    
    if len(unique_ranks) == 3:
        for rank in unique_ranks:
            if ranks.count(rank) == 3:
                three_of_a_kind.append(hand)
                break

len_three_of_a_kind = len(three_of_a_kind)
#b.
print("b.: ", len_three_of_a_kind)
