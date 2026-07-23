import random

# Game setup
list_word = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'grape', 'honeydew']
word = random.choice(list_word)
life = len(word) - 2

# Player setup
word_to_guess = ['_'] * len(word)
current_guess = ''

#  Start Game
print("Welcome to Hangman Game!")
print(f"The word to guess has {len(word)} letters: {''.join(word_to_guess)}")
print(f"You have {life} lives. Good luck!")
print("================================")

while not (life == 0 or ''.join(word_to_guess) == word):
    current_guess = input("Guess a letter: ").lower()
    if current_guess in word_to_guess:
        print(f"You've already guessed '{current_guess}'. Try a different letter.")    
    elif current_guess in word:
        for index, letter in enumerate(word):
            if letter == current_guess:
                word_to_guess[index] = current_guess
        print(f"Good guess! {''.join(word_to_guess)}")
    else:
        life -= 1
        print(f"Wrong guess! You have {life} lives left.")
    print("================================")

if ''.join(word_to_guess) == word:
    print("Congratulations! You've guessed the word:", word)
else:
    print('You lose!')
