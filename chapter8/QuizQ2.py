from math import sqrt

# init position
x, y = 0, 0

moves = input("Enter a sequence of move: ").split()

for i in range(0, len(moves), 2):
    if moves[i] == "U":
        y += int(moves[i + 1])
    elif moves[i] == "D":
        y -= int(moves[i + 1])
    elif moves[i] == "R":
        x += int(moves[i + 1])
    elif moves[i] == "L":
        x -= int(moves[i + 1])

print(sqrt(x ** 2 + y ** 2))

"""
    Test Case : U 5 D 3 L 3 R 2
"""