quiz = [
    ("What is the capital of India?",
     ("A. Mumbai", "B. Delhi", "C. Kolkata", "D. Chennai"), "B"),

    ("Which language is primarily used for web development?",
     ("A. Python", "B. C++", "C. JavaScript", "D. Java"), "C"),

    ("What is the output of: print(2 ** 3)?",
     ("A. 6", "B. 8", "C. 9", "D. 5"), "B"),

    ("Which one is an immutable data type?",
     ("A. List", "B. Dictionary", "C. Tuple", "D. Set"), "C"),

    ("Who is the founder of Microsoft?",
     ("A. Steve Jobs", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerberg"), "C")
]

score = 0
for i in quiz:
    q, o, a, = i
    print(q)
    for opt in o:
        print(opt)
    answer=input("Enter Correct option A/B/C/D: ").strip().upper()
    if answer == a:
        print("correct answer...")
        score += 1
    else:
        print("wrong answer")

else:
    print(f"Your score is {score}")