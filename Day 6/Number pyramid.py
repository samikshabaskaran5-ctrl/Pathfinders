n = int(input("Enter a number: "))

for i in range(1, n + 1):
    print(" " * (n - i), end="")

    for j in range(1, 2 * i):
        if j <= i:
            print(j, end="")
        else:
            print(2 * i - j, end="")

    print()
