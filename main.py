import random
import json

def load_questions(file_path):
    with open(file_path, 'r') as file:
        questions = json.load(file)
    return questions

def geography_quiz():
    # Load questions from the JSON file
    file_path = "questions.json"
    questions = load_questions(file_path)

    # Shuffle the questions for randomness
    random.shuffle(questions)

    # Display welcome message
    print("Welcome to the Geography Quiz!")
    print("Answer the following 10 questions:")

    # Initialize the score
    score = 0

    # Loop through each question
    for i in range(1, 11):  # Ask 10 questions
        question = questions[i - 1]  # Get the current question

        # Ask the user for an answer
        user_answer = input(f"{i}. {question['question']}? ").strip().capitalize()

        # Check if the answer is correct
        if user_answer == question['answer']:
            print("Correct!\n")
            score += 1  # Increase the score by 1 for a correct answer
        else:
            print(f"Wrong! The correct answer is {question['answer']}.\n")

    # Display the final score
    print(f"Quiz completed! Your score is: {score}/10")

if __name__ == "__main__":
    geography_quiz()

