# QUIZ GAME DESIGNED BY TUSHAR MAHAJAN
# Define the Quiz questions and answers
quiz = [
    {
        "question": "What is the capital of India?",
        "options": ["A. New Delhi", "B. London", "C. Rome", "D. Berlin"],
        "answer": "A",
        "feedback": "The Capital Of India is New Delhi."
    },
    {
        "question": "What is 2 + 2?",
        "options": ["A. 3", "B. 4", "C. 5", "D. 6"],
        "answer": "B",
        "feedback": "2+2 equals 4."
    },
    
    {
        "question": "What is the chemical symbol for water?",
        "options": ["A. CO2", "B. H2O", "C. O2", "D. N2"],
        "answer": "B",
        "feedback": "The chemical symbol for water is H2O."
    },
    
    {"question" :"Who Wrote ramayana?",
     "options" :["A.Tulsidas", "B.Vyasa", "C.Valmiki", "D.Kalidasa"],
      "answer": "C",
       "feedback": "The Ramayana Was Written by Valmiki"
     },
    
]

# Function to conduct the quiz
def conduct_quiz(quiz):
    score = 0
    for i, item in enumerate(quiz):
        print(f"Question {i+1}: {item['question']}")
        for option in item["options"]:
            print(option)
        answer = input("Your answer (A/B/C/D): ").strip().upper()
        if answer == item["answer"]:
            print("correct!")
            score += 1
        else:
            print("Incorrect!")
        print(f"Feedback: {item['feedback']}\n")  # Provide feedback

    print(f"You got {score} out of {len(quiz)} questions correct!")
    print ("Thanks for Attempting the Questions")

# Start the quiz
conduct_quiz(quiz)