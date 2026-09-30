import pandas

file = pandas.read_csv("intermediate-python-projects/tools/NATO-alphabet/nato_phonetic_alphabet.csv")
nato_words = {letter : code for (letter, code) in file.values}

user_input = input("Enter a word: ").upper()

# Get the nato word from the keys provided in user input

final = [nato_words[letter] for letter in user_input]

print(final)