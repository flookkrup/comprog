#%%
# Quiz 1
x = input("Enter : ")

if ('0' <= x <= '9'):
    print("digit")
else:
    if(x in ['A', 'E', 'I', 'O', 'U']):
        print("vowel")
    elif('A' <= x <= 'Z'):
        print("capital letter")

x = float(input("x: "))
y = float(input("y: "))

if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x is equal to y")
# %%
