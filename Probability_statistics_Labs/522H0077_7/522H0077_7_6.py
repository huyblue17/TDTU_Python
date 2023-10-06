import itertools
import random

#EX6

E = {0, 1, 2, 3, 4, 5}
#a
three_digits_numbers = [hundreds_digit * 100 + tens_digit * 10 + units_digit
                        for hundreds_digit, tens_digit, units_digit in itertools.product(E, repeat=3)]

print("a. Result:", three_digits_numbers)

#b
four_digits_numbers = [thousands_digit * 1000 + hundreds_digit * 100 + tens_digit * 10 + units_digit
                       for thousands_digit, hundreds_digit, tens_digit, units_digit in random.sample(list(itertools.permutations(E, 4)), k=len(E)*len(E)*len(E))]

print("b. Result:", four_digits_numbers)
