import random

# Questions to be asked

trivia_data = [
    {
        "question": "What is a variable in Python?",
        "options": ["A. A data type", "B. A location in memory to store data", "C. A reserved word", "D. A function"],
        "answer": "B",
        "explanation": "Variables are used to store data that can be referenced and manipulated during program execution."
    },
    {
        "question": "Which of these is not a core data type?",
        "options": ["A. Class", "B. Lists", "C. Tuples", "D. Dictionary"],
        "answer": "A",
        "explanation": "Class is a user defined data type."
    },
    {
        "question": "What is the purpose of the if statement in Python?",
        "options": ["A. To define a function", "B. To execute a block of code conditionally", "C.  To create a loop", "D. To declare a variable"],
        "answer": "B",
        "explanation": "The if statement is used to execute a block of code only if a specified condition is true."
    },
    {
        "question": "In Python, what is a class?",
        "options": ["A. A code block", "B. A function", "C. A module", "D. A blueprint for creating objects"],
        "answer": "D",
        "explanation": "A class in Python serves as a blueprint for creating objects with shared attributes and behaviors."
    },
    {
        "question": "Which of the following is false about dictionary?",
        "options": ["A. The values of a dictionary can be accessed using keys", "B. Dictionaries may or may not be ordered", "C. The keys of a dictionary can be accessed using values", "D. None of the above"],
        "answer": "C",
        "explanation": "The values of a dictionary can be accessed using keys but the keys of a dictionary can’t be accessed using values."
    },
    {
        "question": "What is the basic syntax of a while loop in Python?",
        "options": ["A. while (condition):", "B. for condition:", "C. loop while condition:", "D. while loop condition do:"],
        "answer": "A",
        "explanation": "The basic syntax of a while loop in Python is while (condition):"
    },
    {
        "question": "In Python, what is the purpose of a metaclass?",
        "options": ["A. To define the behavior of classes", "B. Metaclasses are not supported in Python", "C. To define class-level attributes", "D. To create class instances"],
        "answer": "A",
        "explanation": "A metaclass in Python defines the behavior of classes, allowing customization of class creation."
    },
    {
        "question": "How can you ensure a loop executes at least once?",
        "options": ["A. Use a for loop.", "B. Use a while loop with a break statement.", "C. Use a continue statement.", "D. Set the loop condition to True."],
        "answer": "D",
        "explanation": "Setting the loop condition to True ensures that the loop executes at least once."
    },
    {
        "question": "What is the output of the following code: print(9//2)",
        "options": ["A. 4.5", "B. 4", "C. 4.0", "D. Error"],
        "answer": "B",
        "explanation": "The ‘//’ operator in Python returns the integer part of the floating number."
        
    },
    {
        "question": "Which statement is used to exit a loop prematurely in Python?",
        "options": ["A. return", "B. exit", "C. break", "D. continue"],
        "answer": "C",
        "explanation": "The break statement is used to exit a loop prematurely."
    },
]

# Displaying content
def ask_question(question_data):
    print(question_data["question"])
    for option in question_data["options"]:
        print(option)
    user_answer = input("Enter your answer (A, B, C, D): ").upper()
    guesses.append(user_answer) 
    return user_answer == question_data["answer"]
    
# Main body
if __name__=="__main__":
    guesses = []
    score=0
    random.shuffle(trivia_data)
    selected_questions = trivia_data[:5]
    
    for i, question in enumerate(selected_questions, start = 1):
        print(f'Question {i} of 5')
        if ask_question(question):
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect! The correct answer is {question['answer']}.\n")
            print(f"Explanation: {question['explanation']}\n")
            
            
# Results            
print("----------------------")
print("       RESULTS        ")
print("----------------------")

print("\nanswers: ", end="")
for question in selected_questions: 
    print(question["answer"], end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print() 

percentage = int(score / len(selected_questions) * 100)
print(f"\nYour score is: {percentage}%")
    
