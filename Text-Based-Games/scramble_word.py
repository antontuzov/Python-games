import random


def scramble_word():
    word = list(word)
    random.shuffle(word)
    word = ''.join(word)
    return word



def word_scramble():
    words = ['python', 'java', 'kotlin', 'javascript', 'swift', 'rust', 'c++', 'c#']
    word_to_scramble = random.choice(words)
    scrambled_word = scramble_word(word_to_scramble)
    print("welcome to word scramble game")
    print(f"scrambled word: {scrambled_word}")
    
    guess = input("guess the word: ")
    
    if guess == word_to_scramble:
        print("you guessed the word correctly")
    else:
        print("you guessed the word incorrectly")
        print(f"the word was: {word_to_scramble}")
        

if __name__ == "__main__":
    word_scramble()
    
    
    
   




