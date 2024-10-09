

def quiz_game_trivia():
    # Define the questions and answers
    questions = [
        "Who is the founder of Facebook?",
        "What is the capital of Canada?",
        "What is the largest country in the world?",
        "What is the currency of Japan?",
        "What is the highest mountain in the world?"
    ]
    answers = [
        "Mark Zuckerburg",
        "Ottawa",
        "Russia",
        "Japanese yen",
        "Mount Everest"
    ]
    
    score = 0
    
    # Loop through the questions and ask them
    for i in range(len(questions)):
        print(questions[i])
        answer = input("Enter your answer: ")
        if answer.lower() == answers[i].lower():
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")
    
    # Print the final score
    print(f"You got {score} out of {len(questions)} correct!")
    

if __name__ == '__main__':
    quiz_game_trivia()