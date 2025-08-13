# quiz_game.py
# Week 4 Mini Project - Quiz Game

def run_quiz(questions):
    score = 0
    for question, answer in questions.items():
        user_answer = input(f"{question} ").strip().lower()
        if user_answer == answer.lower():
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer is {answer}")
    print(f"\nYour final score is {score}/{len(questions)}")

questions = {
    "What is the capital of France? ": "Paris",
    "What is 5 + 7? ": "12",
    "What language is this program written in? ": "Python"
}

if __name__ == "__main__":
    run_quiz(questions)
