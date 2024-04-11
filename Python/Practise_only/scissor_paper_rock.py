import random

my_list=['scissor' , 'paper' ,'rock']

computer_choice = random.choice(my_list)
player_choice = input("Scissor paper or rock: ").lower()


def game():
    if computer_choice == player_choice:
        return("It's a tie!")
    elif computer_choice =='rock' and player_choice == 'scissor':
        return('Computer won')
    elif computer_choice =='paper' and player_choice == 'rock':
        return('Computer won')
    elif computer_choice =='scissor' and player_choice == 'paper':
        return('Computer won')
    elif player_choice == 'rock' and computer_choice == 'scissor':
        return('PLayer wins')
    elif player_choice == 'rock' and computer_choice == 'scissor':
        return('PLayer wins')
    elif player_choice == 'paper' and computer_choice == 'rock':
        return('PLayer wins')
    elif player_choice == 'scissor' and computer_choice == 'paper':
        return('PLayer wins')


print(f"Computer choose -->{computer_choice}")
print(f"Player choose -->{player_choice}")

if player_choice in my_list:
    result = game()
    print(result)
else:
    print("Invalid choice choose between [Rock , Paper and Scissor]")