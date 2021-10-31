from os import write


f = open("even.txt", "w")

for i in range(2, 101, 2):
    f.write(str(i) + "\n")
f.close()

# %%
for i in range(2, 25, 3):

    print(i)

# %%
for i in range(2, 5):

    print(i)

# %%
for i in range(6, 2, -2):

    print(i)

# %%
for i in range(1.0, 3.0):

    print(i)

# %%
