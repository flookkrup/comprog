txt = input("Enter a string: ").upper()
cnt = {}

for char in txt:
    if not char in cnt:
        cnt[char] = 1
    else:
        cnt[char] += 1
        

for key in cnt:
    print(f"{key}: {cnt[key]}")