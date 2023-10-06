import itertools

#EX3
print("EX3")

math_books = ['M1', 'M2', 'M3', 'M4']
physics_books = ['P1', 'P2', 'P3']
chemistry_books = ['C1', 'C2']
language_books = ['L']

arrangements = itertools.permutations([math_books, physics_books, chemistry_books, language_books])

print(f'Total number of arrangements: {len(list(arrangements))}')

arrangements = itertools.permutations([math_books, physics_books, chemistry_books, language_books])

for arrangement in arrangements:
    for group in arrangement:
        for book in group:
            print(book, end=' ')
    print()