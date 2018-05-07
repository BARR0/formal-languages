# GRAMMAR = [ # Add a separate production if the same symbol can have multiple results
#     ('S', 'AB'),
#     ('S', 'SS'),
#     ('S', 'AC'),
#     ('S', 'BD'),
#     ('C', 'SB'),
#     ('D', 'SA'),
#     ('A', 'a'),
#     ('B', 'b')
# ]

# WORD = 'aabbab'

# GRAMMAR = [
#     ('S', 'AB'),
#     ('S', 'BA'),
#     ('A', 'AB'),
#     ('A', 'a'),
#     ('B', 'AA'),
#     ('B', 'b')
# ]

# WORD = 'bbab'

GRAMMAR = [
    ('S', 'SU'),
    ('S', 'SB'),
    ('S', 'CA'),
    ('S', 'c'),
    ('A', 'AU'),
    ('A', 'a'),
    ('B', 'b'),
    ('C', 'c'),
    ('U', 'a'),
]

WORD = 'cabaac'

def CYK(G, w, pinit = 'S'):
    V = [[set() for j in range(len(w))] for i in range(len(w))]

    for i in range(len(w)):
        V[i][i] = {x for (x, y) in G if y == w[i]}

    for gap in range(1, len(w)):
        for i in range(len(w) - gap):
            start = i
            end = i + gap
            prods = {(x + y) for j in range(gap) for x in V[start][start + j] for y in V[start + j + 1][end]}
            # print(start, end, gap, prods)
            V[start][end] = {x for (x, y) in G if y in prods}

    for i in V:
        print(i)
    print()

    return pinit in V[0][-1]

if __name__ == '__main__':
    if CYK(GRAMMAR, WORD):
        print(WORD, 'is in L(G).')
    else:
        print(WORD, 'is not in L(G).')

