#
# Chapter 10 Practice
# Dylan Le Voguer
#

vowels = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}


def count_vowels(word):
    for char in word:
        if char in vowels:
            vowels[char] += 1


print(f"before = {vowels}")

userword = input("Enter a word to count it's vowels:")

count_vowels(userword)

print(f"after = {vowels}")
