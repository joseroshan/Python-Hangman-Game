import random, hangman_art as ha, hangman_words as hw
from replit import clear


chosen_word = random.choice(hw.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6


print(ha.logo)


display = []
for _ in range(word_length):
    display += "_"

print(f"\n{' '.join(display)}\n")

guessed_words = []
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    clear()
    
#If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in guessed_words:
      print(f"You've already guessed {guess}")
      continue
      
    else:
      guessed_words.append(guess)
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        
      # for debugging use this statement print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter


#If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(f"You lose. The word is {chosen_word}")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(ha.stages[lives])