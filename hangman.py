import random
import os
print("\n                                              .........HANGMAN GAME........")
words_list = ["abruptly","absurd","abyss","affix","avenue","awkward","axiom"]
selected_word=random.choice(words_list)
word_length=len(selected_word)
print("Word: ",end="")
for i in range(word_length):
    print("_ ",end="")
display=[]
lives=6
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

for i in range(word_length):
    display += "_"
end=False
while not end:
    guess = input("\nGuess a letter: ")
    guess = guess.lower()
    os.system("cls")
    for i in range(word_length):
        letter=selected_word[i]
        if (guess==letter):
            display[i]=letter
    if guess not in selected_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("\nSorry,You lost the game.")
            print(f"The word is {selected_word}")
            break
    print(f"\nWord: {display}")
    if "_" not in display:
        end=True
        print("\nCongratulations!!!,You won the game.")
    else:
        print(stages[lives])
