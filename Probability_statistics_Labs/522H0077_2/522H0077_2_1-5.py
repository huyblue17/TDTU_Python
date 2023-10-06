import random

n = 100

#EX1
print("EX1")

def simulator_dice1(n):
    count = 0
    
    for i in range(n):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        if (dice1 % 2 == 0) and (dice2 % 2 == 0):
            count += 1
    probability = count / n
    return probability

prob_bothevent = simulator_dice1(n)
print("1.Result: ", prob_bothevent)

#EX2
print("EX2")

def simulator_dice2(n):
    count = 0
    
    for i in range(n):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        if (dice1 % 2 == 0 and dice2 % 2 != 0) or (dice1 % 2 != 0 and dice2 % 2 == 0):
            count += 1
    probability = count / n
    return probability

prob_eveodd = simulator_dice2(n)
print("2.Result: ", prob_eveodd)

#EX3
print("EX3")

def simulator_dice3(n):
    count = 0
    
    for i in range(n):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        if (dice1 == dice2):
            count += 1
    probability = count / n
    return probability

prob_same = simulator_dice3(n)
print("3.Result: ", prob_same)

#EX4
print("EX4")

def simulator_dice4(n):
    count = 0
    
    for i in range(n):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        if (dice1 == 1 and dice2 == 6) or (dice1 == 6 and dice2 == 1):
            count += 1
    probability = count / n
    return probability

prob_1or6 = simulator_dice4(n)
print("4.Result: ", prob_1or6)

#EX5
print("EX5")

def simulator_dice5(n):
    count = 0
    
    for i in range(n):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        if (dice1 + dice2) > 6:
            count += 1
    probability = count / n
    return probability

prob_sum = simulator_dice5(n)
print("5.Result: ", prob_sum)

