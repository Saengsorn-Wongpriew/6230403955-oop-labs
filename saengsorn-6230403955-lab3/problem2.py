game = True
guesses = 3
secret_word = "kku"

while game:
    if guesses > 0:
        word = input("Enter a word: ")
        if word == secret_word:
            print("Congrats that you can guess the secret word correctly")
            game = False
        else:
            guesses -= 1
            if guesses == 1:
                guess = "guess"
            else:
                guess = "guesses"
            print(f"Incorrect you have {guesses} {guess} left")
    else:
        print ("Thanks for trying, \
but the secret word is actually", secret_word)
        game = False
