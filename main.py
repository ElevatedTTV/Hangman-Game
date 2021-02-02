import random


# Opens a designated word list text file (given as an argument in the function) and then converts it to a list known
# as new_word_list.


def hang_man(filepath):
    '''
    This will return the variable new_word_list as a list of the words from your word list, allowing iteration.
    :param filepath:
    :return:
    '''
    with open(filepath) as wordlist:
        global new_word_list
        new_word_list = []
        for word in wordlist:
            new_word_list.append(word.strip())
        return new_word_list


hang_man("FILE GOES HERE)

secret_word = str(new_word_list[random.randint(0, len(new_word_list))]).lower()
hidden_word = str('*'*len(secret_word))
# Selects a random word from the word list and displays it on the screen.


def guessingGame():
    guess_count = 0
    user_guesses = set()  # turning user guesses into a set to avoid printing duplicates.
    incorrect_guesses = []
    print(f'The secret word is {hidden_word}')
    while guess_count != 3:
        userInput = input('Guess a Letter: ')
        for number in range(0, 10):
            if userInput == str(number):
                print('ENTER A DAMN LETTER')
        if str(userInput.lower()) in secret_word:
            print('Good Job! ')
            user_guesses.add(userInput)
            guess_count = 0
            print(f'Secret Word: {hidden_word}, Your correct guesses: ' + ' '.join(user_guesses).upper())
            # for letter in user_guesses:
            #     print(secret_word.index(letter))    <<<---- Prints the index location of the guessed letter.
        else:
            print('Nope Not Right')
            guess_count += 1  # only charges a guess count if guess was incorrect.
            print(f'Secret Word: {hidden_word}, Your correct guesses: ' + ' '.join(user_guesses).upper())
            incorrect_guesses.append(userInput)
    else:
        print(f'Sorry, you ran out of guesses, the secret word was \"{secret_word}\"!')


guessingGame()

# Issues to fix #
# Would like to print the ****** secret word but including the already guessed letters in the correct position.???
