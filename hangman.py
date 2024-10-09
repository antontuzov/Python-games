import random


def hangman():
    word_list = ["python", "java", "kotlin", "javascript", "swift", "rust", "c++", "c#"]
    word = random.choice(word_list)
    word_desplayed = "-" * len(word)
    guessed_letters = []
    attempts = 6
    
    
    print("welcome to hangman")
    print("you have 6 attempts to guess the word")
    
    
    while attempts > 0 and "-" in word_desplayed:
        print(f"word: {word_desplayed}")
        print(f"attempts: {attempts}")
        print(f"guessed letters: {''.join(guessed_letters)}") # print(f"guessed letters: {guessed_letters}")
        
        guess = input("guess a letter: ").lower()
        
        if guess in guessed_letters:
            print("you already guessed that letter")
            continue
        guessed_letters.append(guess)
        
        if guess in word:
            print("good guess")
            for i in range(len(word)):
                if word[i] == guess:
                    word_desplayed = word_desplayed[:i] + guess + word_desplayed[i+1:]
        else:
            print("bad guess")
            attempts -= 1
            if attempts == 0:
                print("game over")
                print(f"the word was {word}")
        print()
        print("the word is", word_desplayed)
        print()
        
        
        

if __name__ == '__main__':
    hangman()
        
      
  

   