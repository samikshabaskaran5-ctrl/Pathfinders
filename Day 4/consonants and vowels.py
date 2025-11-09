string = "Education"
vowels = 0
consonants = 0
for ch in string:
    if ch.isalpha(): 
        if ch.lower() in ['a', 'e', 'i', 'o', 'u']:
            vowels = vowels + 1
        else:
            consonants = consonants + 1
print("Vowels =", vowels)
print("Consonants =", consonants)
