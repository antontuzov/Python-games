import random

def number_guessing_with_levels():
    print('welcome to guess the number game with levels')
    
    #set the level
    while True:
        level = input('enter level (easy, medium, hard): ').lower()
        if level == 'easy':
            max_attempts = 10
            break
        elif level == 'medium':
            max_attempts = 5
            break
        elif level == 'hard':
            max_attempts = 3
            break
        else:
            print('please enter a valid level')
            continue
        
    if level == 'easy':
        print('you have 10 attempts to guess the number')
    elif level == 'medium':
        print('you have 5 attempts to guess the number')
    elif level == 'hard':
        print('you have 3 attempts to guess the number')
    
    number = random.randint(1, 100)
    attempts = 0
    
    while attempts < max_attempts:
        #guess the number
        try :
            guess = int(input('enter your guess: '))
        except ValueError:
            print('please enter a valid number')
            continue
        attempts += 1
        if guess < number:
            print('your guess is too low')
        elif guess > number:
            print('your guess is too high')
        else:
            print(f'you guessed the number in {attempts} attempts')
            break
        
    if attempts == max_attempts:
        print(f'the number was {number}')
        
        
        

if __name__ == '__main__':
    number_guessing_with_levels()
        
    
    