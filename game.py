#!/usr/bin/env python3
"""
Interactive Multiple-Choice Quiz Game
Test your knowledge on Python, movies, and fun facts!
"""

def display_welcome():
    """Display welcome message"""
    print("\n" + "="*60)
    print("   WELCOME TO THE ULTIMATE QUIZ CHALLENGE! 🏆")
    print("="*60)
    print("Test your knowledge on Python, movies, and more!")
    print("Choose the correct answer for each question.\n")

def get_questions():
    """Return a list of quiz questions with answers"""
    questions = [
        {
            "question": "What is the output of print(2 ** 3) in Python?",
            "options": ["6", "8", "9", "27"],
            "correct": 1  # Index 1 = "8"
        },
        {
            "question": "Which movie won the Academy Award for Best Picture in 2023?",
            "options": ["Top Gun: Maverick", "Everything Everywhere All at Once", "The Fabelmans", "Avatar: The Way of Water"],
            "correct": 1  # Index 1 = "Everything Everywhere All at Once"
        },
        {
            "question": "In Python, which keyword is used to create a function?",
            "options": ["function", "def", "define", "func"],
            "correct": 1  # Index 1 = "def"
        },
        {
            "question": "What does HTML stand for?",
            "options": ["Hyper Text Markup Language", "High Tech Modern Language", "Home Tool Markup Language", "Hyperlinks and Text Markup Language"],
            "correct": 0  # Index 0
        },
        {
            "question": "Which planet is known as the 'Red Planet'?",
            "options": ["Venus", "Jupiter", "Mars", "Saturn"],
            "correct": 2  # Index 2 = "Mars"
        },
        {
            "question": "In Python, what is a 'list' primarily used for?",
            "options": ["Storing a single value", "Storing an ordered collection of items", "Creating loops", "Defining functions"],
            "correct": 1  # Index 1
        },
        {
            "question": "Who directed 'The Shawshank Redemption'?",
            "options": ["Steven Spielberg", "Frank Darabont", "Christopher Nolan", "Martin Scorsese"],
            "correct": 1  # Index 1 = "Frank Darabont"
        },
        {
            "question": "What does 'AI' stand for?",
            "options": ["Artificial Intelligence", "Automated Integration", "Advanced Integration", "Artificial Integration"],
            "correct": 0  # Index 0
        },
        {
            "question": "In Python, which data type is immutable?",
            "options": ["list", "dict", "tuple", "set"],
            "correct": 2  # Index 2 = "tuple"
        },
        {
            "question": "How many Academy Awards did 'Titanic' win in 1998?",
            "options": ["11", "13", "15", "10"],
            "correct": 1  # Index 1 = "11"
        }
    ]
    return questions

def run_quiz():
    """Run the quiz game"""
    score = 0
    questions = get_questions()
    
    for i, q in enumerate(questions, 1):
        print(f"\n{'='*60}")
        print(f"Question {i} of {len(questions)}")
        print(f"{'='*60}")
        print(f"\n{q['question']}\n")
        
        for j, option in enumerate(q['options'], 1):
            print(f"  {j}. {option}")
        
        while True:
            try:
                user_answer = int(input("\nYour answer (1-4): "))
                if 1 <= user_answer <= 4:
                    break
                else:
                    print("Invalid input! Please enter a number between 1 and 4.")
            except ValueError:
                print("Invalid input! Please enter a number.")
        
        # Convert to 0-based index
        user_answer_idx = user_answer - 1
        
        if user_answer_idx == q['correct']:
            print("✓ Correct!")
            score += 1
        else:
            correct_answer = q['options'][q['correct']]
            print(f"✗ Incorrect! The correct answer is: {correct_answer}")
    
    display_score(score, len(questions))

def display_score(score, total):
    """Display final score and rating"""
    print("\n" + "="*60)
    print("   QUIZ COMPLETE! 🎉")
    print("="*60)
    print(f"\nYour Score: {score}/{total}")
    
    percentage = (score / total) * 100
    
    if percentage == 100:
        rating = "PERFECT! You're a quiz master! 🌟"
    elif percentage >= 80:
        rating = "Excellent! Outstanding performance! 🏅"
    elif percentage >= 60:
        rating = "Good! Not bad at all! 👍"
    elif percentage >= 40:
        rating = "Fair! Keep practicing! 📚"
    else:
        rating = "Keep trying! You'll do better next time! 💪"
    
    print(f"Percentage: {percentage:.1f}%")
    print(f"Rating: {rating}\n")

def play_again():
    """Ask if user wants to play again"""
    while True:
        response = input("Would you like to play again? (yes/no): ").strip().lower()
        if response in ['yes', 'y']:
            return True
        elif response in ['no', 'n']:
            return False
        else:
            print("Please enter 'yes' or 'no'.")

def main():
    """Main game loop"""
    display_welcome()
    
    while True:
        run_quiz()
        if not play_again():
            print("\n" + "="*60)
            print("Thanks for playing! Goodbye! 👋")
            print("="*60 + "\n")
            break

if __name__ == "__main__":
    main()
