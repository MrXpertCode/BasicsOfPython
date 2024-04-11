import random

randomNumber = random.randint(1 , 100)
print(randomNumber)
print("Welcome to guess the number game")
print("Guess the number between 1 to 100")
guesses = 0
userInput = None


while randomNumber != userInput:
    guesses += 1
    userInput = int(input("Can you guess the number-->"))
    # assert userInput in range(1,101)
    if randomNumber == userInput:
        print("You guessed it right")
    else:
        if randomNumber > userInput:
            print("Too low, guess high")
        elif randomNumber < userInput:
            print("Too high, guess low")
    
print(f'Congratulation you guess it right in {guesses}th turn')

finalscore = 'Highscore.txt' 

if str(guesses)< finalscore:
    with open('Highscore.txt', 'w') as files:
        files.write(str(guesses))
