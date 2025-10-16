def run_quiz(questions):
    score = 0
    for q in questions:
        print(q["question"])
        for i, option in enumerate(q["options"], 1):
            print(f"{i}. {option}")
        answer = input("Your answer (enter the number): ")
        if answer.strip() == str(q["answer"]):
            print(f"Current score: {score}\n")
            print("Correct!\n")
            score += 1
            print(f"The correct answer was {q['answer']}.\n")
        else:
            print(f"Wrong! The correct answer was {q['answer']}.\n")
    print(f"Quiz finished! Your score: {score}/{len(questions)}")

# English general knowledge questions by difficulty
easy_questions = [
    {
        "question": "What is the plural form of 'mouse'?",
        "options": ["Mouses", "Mice", "Mousies", "Mouse"],
        "answer": 2
    },
    {
        "question": "Which of these is a punctuation mark?",
        "options": ["Comma", "Commae", "Commar", "Coma"],
        "answer": 1
    },
    {
        "question": "What is the opposite of 'hot'?",
        "options": ["Warm", "Cold", "Cool", "Heat"],
        "answer": 2
    },
    {
        "question": "Which word is a noun?",
        "options": ["Run", "Blue", "Happiness", "Quickly"],
        "answer": 3
    },
    {
        "question": "Which sentence is correct?",
        "options": [
            "She go to school every day.",
            "She goes to school every day.",
            "She going to school every day.",
            "She gone to school every day."
        ],
        "answer": 2
    }
]

medium_questions = [
    {
        "question": "Which word is an adjective?",
        "options": ["Quickly", "Run", "Beautiful", "Happiness"],
        "answer": 3
    },
    {
        "question": "What is the past tense of 'run'?",
        "options": ["Runned", "Ran", "Running", "Runs"],
        "answer": 2
    },
    {
        "question": "Which sentence uses a simile?",
        "options": [
            "The sun was a golden coin.",
            "She is as fast as a cheetah.",
            "He runs quickly.",
            "It is raining outside."
        ],
        "answer": 2
    },
    {
        "question": "Which word is a synonym for 'big'?",
        "options": ["Tiny", "Large", "Small", "Short"],
        "answer": 2
    },
    {
        "question": "Which sentence is a question?",
        "options": [
            "She likes apples.",
            "Do you like apples?",
            "He eats apples.",
            "They have apples."
        ],
        "answer": 2
    }
]

hard_questions = [
    {
        "question": "Which sentence contains a subordinate clause?",
        "options": [
            "She went to the store.",
            "Because it was raining, we stayed inside.",
            "He likes pizza.",
            "They are playing outside."
        ],
        "answer": 2
    },
    {
        "question": "What is the antonym of 'generous'?",
        "options": ["Kind", "Selfish", "Friendly", "Helpful"],
        "answer": 2
    },
    {
        "question": "Which word is an abstract noun?",
        "options": ["Table", "Happiness", "Dog", "Car"],
        "answer": 2
    },
    {
        "question": "Which sentence is written in passive voice?",
        "options": [
            "The dog chased the cat.",
            "The cat was chased by the dog.",
            "The dog is chasing the cat.",
            "The cat chases the dog."
        ],
        "answer": 2
    },
    {
        "question": "What is the correct form: 'Neither of the boys ___ going.'?",
        "options": ["are", "is", "were", "be"],
        "answer": 2
    }
]

if __name__ == "__main__":
    print("Choose a difficulty: easy, medium, hard")
    difficulty = input("Enter difficulty: ").strip().lower()
    if difficulty == "easy":
        run_quiz(easy_questions)
    elif difficulty == "medium":
        run_quiz(medium_questions)
    elif difficulty == "hard":
        run_quiz(hard_questions)
    else:

        print("Invalid difficulty. Please restart and choose easy, medium, or hard.")
        #hi
