import random
print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")
#if the user has not guessed the correct answer, enter the loop
#ask the user for a guess
#is the guess the correct number?
#if the correct guess, tell the user it was the correct guess and exit the loop
#if the wrong guress , tell the user it was the wrong guess and continue the loop
number = random.randint(1,10)
isGuessRight = False
while isGuessRight != True:
    guess = input("Guess a number between 1 and 10: ")
    if int(guess) == number:
        print("You guessed {. That is correct! You win!".format(guess))
        isGuessRight = True
    else:
        print("You guessed {}. Sorry, that isn't it.Try again.".format(guess))