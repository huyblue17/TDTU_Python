import itertools

#EX4
print("EX4")

men = {'M1', 'M2', 'M3', 'M4', 'M5', 'M6'}
women = {'W1', 'W2', 'W3', 'W4', 'W5', 'W6', 'W7', 'W8', 'W9'}

select_men = list(itertools.combinations(men, 3))
select_women = list(itertools.combinations(women, 2))

total = len(select_men) * len(select_women)

print("Total:", total)

print("Selections:")
for combination_men in combinations_men:
    for combination_women in combinations_women:
        print(combination_men + combination_women)
