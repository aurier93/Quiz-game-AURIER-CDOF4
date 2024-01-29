# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 14:11:21 2024

@author: Michel
"""

import os
import platform

# Clear the screen based on the user's operating system
def clear_screen():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

# Function to run the quiz
def run_quiz(questions):
    score = 0
    for question in questions:
        clear_screen()
        print(question["question"])
        for idx, option in enumerate(question["options"], 1):
            print(f"{idx}. {option}")
        
        # Input validation loop
        while True:
            try:
                user_answer = int(input("\nEnter the number of your answer: "))
                if 1 <= user_answer <= len(question["options"]):
                    break
                else:
                    print("Please enter a valid option number.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        # Check if the answer is correct
        if question["options"][user_answer - 1] == question["answer"]:
            score += 1
            print("\nCorrect!")
        else:
            print("\nWrong!")
        input("\nPress Enter to continue to the next question...")

    clear_screen()
    print(f"Your final score is {score}/{len(questions)}")
    # Final message based on the score
    if score == len(questions):
        print("Amazing! You got all questions right!")
    elif score > len(questions) // 2:
        print("Good job! You scored more than half.")
    else:
        print("You can do better next time.")
    input("\nPress Enter to exit the quiz.")

# List of questions
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Paris", "London", "Rome", "Berlin"],
        "answer": "Paris"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Jupiter", "Venus"],
        "answer": "Mars"
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
        "answer": "Pacific Ocean"
    },
    {
        "question": "In which year did the Titanic sink?",
        "options": ["1912", "1921", "1918", "1905"],
        "answer": "1912"
    },
    # You can add more questions here
]

# Start the quiz
if __name__ == "__main__":
    run_quiz(questions)
