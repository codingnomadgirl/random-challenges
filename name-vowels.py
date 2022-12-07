# Version 1
name = input("What's your name? ")
i = 0
for letter in name:
    if letter == "a":
        i += 1
    elif letter == "e":
        i += 1
    elif letter == "i":
        i += 1
    elif letter == "o":
        i += 1
    elif letter == "u":
        i += 1
    number_of_vowels = i
print(f"Your name has {number_of_vowels} vowels.")


# Version 2

name = input("What's your name? ")
vowels_list = ["a", "e", "i", "o", "u"]

x = 0
for letter in name:
    if letter in vowels_list:
        x += 1
        number_of_vowls = x
print(f"Your name has {number_of_vowls} vowels.")

