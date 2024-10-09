import random


def rock_paper_scissors():
    choices = ['rock', 'paper', 'scissors']
    
    print('welcome to rock paper scissors game')
    while True:
        #get player choice
        player_choice = input('enter your choice: ').lower()
        
        if player_choice == 'quit':
            print('thank you for playing')
            break
        
        
        if player_choice not in choices:
            print('please enter a valid choice')
            continue
        
        #get computer choice
        
        compiter_choice = random.choice(choices)
        print(f'computer choice is {compiter_choice}')
        
        if player_choice == compiter_choice:
            print('its a tie')
        elif player_choice == 'rock' and compiter_choice == 'scissors':
            print('you win')
        elif player_choice == 'paper' and compiter_choice == 'rock':
            print('you win')
        elif player_choice == 'scissors' and compiter_choice == 'paper':
            print('you win')
        else:
            print('you lose')
            
        
        print('do you want to play again?')
        if input().lower() != 'yes':
            break
        
    

if __name__ == '__main__':
    rock_paper_scissors()
        
    