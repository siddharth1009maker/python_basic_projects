quiz = {
    "question1": {
        "question": "What is the capital of France?",
        "answer": "Paris"
    },
    "question2": {
        "question": "What is the capital of Germany?",
        "answer": "Berlin"
    },
    "question3": {
        "question": "What is the capital of Italy?",
        "answer": "Rome"
    },
    "question4": {
        "question": "What is the capital of Spain?",
        "answer": "Madrid"
    }, "question5": {
        "question": "What is the capital of Portugal?",
        "answer": "Lisbon"
    }, "question6": {
        "question": "What is the capital of Switzerland?",
        "answer": "Bern"
    }, "question7": {
        "question": "What is the capital of Austria?",
        "answer": "Vienna"
    },
}

score = 0

for values in quiz.values():
    print(values['question'])
    answer = input("Answer is: ")

    if (answer.lower() == values["answer"].lower()):
        print("Correct")
        score += 1
        print(f"Your score is {score}")
        print("")
        print("")
    else:
        print("Wrong!")
        print("The answer is : " + values['answer'])
        print(f"Your score is {score}")
        print("")
        print("")
print("You got " + str(score) + " out of 7 questions correctly")

percentage = score/7 * 100
print(f"Your percentage is {round(percentage,2)}%")
