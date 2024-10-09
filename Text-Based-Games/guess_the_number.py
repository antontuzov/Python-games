
import random


def guess_the_number():
    
    number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10
    
    print('welcome to guess the number game')
    print(f'you have {max_attempts} attempts to guess the number')
    
    while attempts < max_attempts:
        # guess the number
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
    guess_the_number()
    
    
    
        
        
    
    
   
    
    
    
   
        