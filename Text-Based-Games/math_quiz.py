import random
import operator



def math_quiz():
    
    operators = {'+': operator.add,
                 '-': operator.sub,
                 '*': operator.mul,
                 '/': operator.floordiv}
    
    print('welcome to math quiz')
    
    num_questions = 5 #number of questions
    score = 0
    
    
    for i in range(num_questions):
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        operation = random.choice(list(operators.keys()))
        
        # if the operator is divided, make sure num2 is not zero
        
        if operation == '/':
            while num2 == 0:
                num2 = random.randint(1, 100)
        correct_answer = operators[operation](num1, num2)
        
        print(f'what is {num1} {operation} {num2}?')
        answer = int(input('enter your answer: '))
        
        if answer == correct_answer:
            score += 1
            print('correct')
        else:
            print(f'the correct answer is {correct_answer}')
            
    print(f'you got {score} correct out of {num_questions}')
    
    

if __name__ == '__main__':
    math_quiz()
        
        
        
    
    
    