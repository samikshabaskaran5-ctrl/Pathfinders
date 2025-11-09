string = "banana"
freq = {}
for ch in string:
    if ch in freq:
        freq[ch] = freq[ch] + 1
    else:
        freq[ch] = 1
for ch in freq:
    print(ch, "→", freq[ch])
