numbers = [5, 2, 9, 1, 7]
first = second = float('-inf')
for num in numbers:
    if num > first:
        second = first
        first = num
    elif num > second and num != first:
        second = num

print("Second largest element:", second)
