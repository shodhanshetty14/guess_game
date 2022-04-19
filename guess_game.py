#Guess the Number game
import random

secretNumber = random.randint(1, 30)
print("I'm thinging of a number between 1-30 right now, try guessing it: ")

#Asking the player to guess the number and give him a total of 3 chances
for guessTaken in range(1 ,4):
    print('Take a Guess: ')
    guess = int(input())

    if guess < secretNumber:
        print("Your guess is too Low. ")
    elif guess > secretNumber:
        print("Your guess is too high. ")
    else:
        break       #The guessed number is correct so break out of the loop

if guess == secretNumber:
    print("Congrulations!!, You have guessed the number Correctly. ")
    print(f"You have taken a total of {str(guessTaken )} guesses." )

else:
    print('Sorry your Guess is Wrong!!')
    print(f"The Number which i had guessed was {secretNumber} ")
