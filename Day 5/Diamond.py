n = int(input("Enter the value of n: "))
if n % 2 == 0:
    n -= 1
    print("Note: Even number entered, using", n, "to form the diamond.")
half = (n // 2) + 1
for i in range(half):
    stars = 2 * i + 1
    print(('*' * stars).center(n))
for i in range(half - 2, -1, -1):
    stars = 2 * i + 1
    print(('*' * stars).center(n))
