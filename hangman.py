import sys
import random
import re

hangman_words = ['abyss', 'cobweb', 'blizzard', 'crypt', 'buzzwords']


while True:
    random_word = hangman_words[random.randint(0, len(hangman_words) - 1)]
    random_word = random_word.lower()
    random_word = list(random_word)
    hidden_word = ['*' for letter in random_word]
    hidden_word_string = ''.join(hidden_word)

    print(f'\nGuess the word: {hidden_word_string}')
    #print(random_word)

    if len(random_word) * 2 < 26:
        guesses_left = len(random_word) * 2
    else:
        guesses_left = 26

    previous_guesses = []

    while True:

        current_guess = input('Guess a letter: ')
    
        if current_guess.title() == 'Quit':
            sys.exit()

        current_guess = current_guess.lower()
        
        if len(current_guess) > 1:
            print('\nYou many only guess one letter at a time!')

        elif not re.match("^[a-z]*$", current_guess):
            print("\nYou may only guess letters A-Z!")

        elif current_guess not in previous_guesses:
            if current_guess not in random_word:
                previous_guesses.append(current_guess)
                guesses_left -= 1

                if guesses_left == 0:
                    print('You have 0 guesses left. You lose!') 
                    sys.exit()

                hidden_word_string = ''.join(hidden_word)
                print(f'\nGuess the word: {hidden_word_string}')
                print(f'Attempts left: {guesses_left}')

                previous_guesses_string = ', '.join(previous_guesses)
                print(f'Previous attempts: {previous_guesses_string}')
                print(f'{current_guess} is not in the word!')
                
            if current_guess in random_word:
                previous_guesses.append(current_guess)
                guesses_left -=1

                indices = [i for i in range(len(random_word)) if random_word[i] == current_guess]
                #print(indices)
                
                for index in indices:
                    hidden_word[index] = current_guess

                hidden_word_string = ''.join(hidden_word)
                print(f'\nGuess the word: {hidden_word_string}')

                if '*' not in hidden_word:
                    print('Congratulations! You win!')
                    sys.exit()
                
                print(f'Attempts left: {guesses_left}')

                previous_guesses_string = ', '.join(previous_guesses)
                print(f'Previous attempts: {previous_guesses_string}')
                print(f'{current_guess} is in the word!')

                if guesses_left == 0:
                    print('You have 0 guesses left. You lose!') 
                    sys.exit()
        
        else:
            print(f'You have already guessed the letter {current_guess}\n')