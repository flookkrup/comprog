from math import floor
# Portrait

w = 8
h = 12

portrait = w // 2 + h // 3

# Landscape

w = 12
h = 8

landscape = w // 2 + h // 3

if portrait > landscape:
    print("Portrait")
else:
    print("Landscape")
