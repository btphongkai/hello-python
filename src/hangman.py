import random

list_word = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew']
word = random.choice(list_word)
word_to_guess = ['_'] * len(word)
print("Welcome to Hangman Game!");
print("The word to guess has", len(word), "letters.")
print(" ".join(word_to_guess))
