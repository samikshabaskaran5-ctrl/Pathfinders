arr = [1, 2, 2, 3, 4, 4, 5]
unique = []  
for num in arr:
    found = False
    for u in unique:
        if u == num:
            found = True
            break
    if not found:
        unique.append(num)
print("Array without duplicates =", unique)
