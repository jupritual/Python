quiz = {
    "What is the capital of India?": "delhi",
    "Who developed Python?": "guido van rossum",
    "What is 5 + 7?": "12"
}
score = 0 
for question, answer in quiz.items():
    print(question)
    user_input = input("Enter answer: ").lower()
    if quiz[question] == user_input:
        print("correct answer")
        score += 1
    else:
        print(f"Wrong answer, correct answer was {answer} ")
print(f"Your score is, {score}/{len(quiz)}")