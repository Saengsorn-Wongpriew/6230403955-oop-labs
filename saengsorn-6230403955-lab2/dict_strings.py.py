dictionary = {
    "manee": "1234",
    "mana": "4567",
    "chujai": "6789"
}

t = list(dictionary.items())
print(t)

v = list(dictionary.values())
print(v)

k = list(dictionary.keys())
print(k)

word = "antidisestablishmentarianism"
word = sorted(word)
print(''.join(word))

sentence = "the quick brown fox jumped over the lazy dog"
w = sentence.split()
print(w)
