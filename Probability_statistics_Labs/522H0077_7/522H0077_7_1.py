#EX1
import random

n = 50

def simulator_dice_a(n):
    count = 0
    
    for i in range(n):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        if dice1 == dice2:
            count += 1
    probability = count / n
    return probability

prob_a = simulator_dice_a(n)
print("a.Result: ", prob_a)



def simulator_dice_b(n):
    count = 0
    
    for i in range(n):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        if dice1 != dice2:
            count += 1
    probability = count / n
    return probability

prob_b = simulator_dice_b(n)
print("b.Result: ", prob_b)



def simulator_dice_c(n):
    count = 0
    
    for i in range(n):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        if (dice1 % 2 == 0) and (dice2 % 2 == 0):
            count += 1
    probability = count / n
    return probability

prob_c = simulator_dice_c(n)
print("c.Result: ", prob_c)



def simulator_dice_d(n):
    count = 0
    
    for i in range(n):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        if (dice1 % 2 != 0) and (dice2 % 2 != 0):
            count += 1
    probability = count / n
    return probability

prob_d = simulator_dice_d(n)
print("d.Result: ", prob_d)



def simulator_dice_e(n):
    count = 0
    
    for i in range(n):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        if ((dice1 % 2 != 0) and (dice2 % 2 == 0)) or ((dice1 % 2 == 0) and (dice2 % 2 != 0)):
            count += 1
    probability = count / n
    return probability

prob_e = simulator_dice_e(n)
print("e.Result: ", prob_e)



def simulator_dice_f(n):
    count = 0
    
    for i in range(n):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        if dice1 == 6 and dice2 == 6:
            count += 1
    probability = count / n
    return probability

prob_f = simulator_dice_f(n)
print("f.Result: ", prob_f)




def simulator_dice_g(n):
    count = 0
    
    for i in range(n):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        if dice1 + dice2 > 10:
            count += 1
    probability = count / n
    return probability

prob_g = simulator_dice_g(n)
print("g.Result: ", prob_g)



