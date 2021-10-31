#%%
def f(a, b):
    a = 10
    b = 0
    x = 0
    y = 1
    print(x, y)
    return a-b

x = 5
y = 7
z = f(x,y)
print(x, y, z)

""" 
Results:
0 1
5 7 10
"""
#%%
def f(a, b):
    global x, y
    a = 10
    b = 0
    x = 0
    y = 1
    print(x, y)
    return a-b

x = 5
y = 7
z = f(x, y)
print(x, y, z)

"""
Results (with global): 
0 1
0 1 10
"""
# %%
