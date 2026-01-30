import time

def print_slow(text, delay=0.05):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

def kbc():
    print("="*50)
    print("🎤  WELCOME TO KAUN BANEGA CROREPATI (CLI EDITION) 🎤")
    print("="*50)
    time.sleep(1)

    name = input("\n🎯 Enter your name: ")
    print_slow(f"\nWelcome, {name}! Let’s begin your journey...\n")

    questions = [
        {
            "question": "What is the capital of India?",
            "options": ["A) Mumbai", "B) Delhi", "C) Kolkata", "D) Chennai"],
            "answer": "B"
        },
        {
            "question": "Which language is used for web development?",
            "options": ["A) Python", "B) C", "C) JavaScript", "D) Assembly"],
            "answer": "C"
        },
        {
            "question": "Who is known as the Father of Computers?",
            "options": ["A) Charles Babbage", "B) Alan Turing", "C) Tim Berners-Lee", "D) Bill Gates"],
            "answer": "A"
        }
    ]

    prize = 0
    prize_money = [1000, 5000, 10000]

    for i, q in enumerate(questions):
        print("\n" + "-"*50)
        print_slow(f"🔥 Question {i+1} for ₹{prize_money[i]}:")
        print_slow(q["question"])

        for option in q["options"]:
            print(option)

        answer = input("\n👉 Your answer (A/B/C/D): ").upper()

        if answer == q["answer"]:
            prize = prize_money[i]
            print_slow("\n✅ Correct Answer! Moving ahead...")
        else:
            print_slow("\n❌ Wrong Answer!")
            print_slow(f"💰 You take home ₹{prize}")
            print("\nGame Over!")
            return

    print("\n" + "="*50)
    print_slow(f"🎉 CONGRATULATIONS, {name}! You won ₹{prize}! 🎉")
    print("="*50)

if __name__ == "__main__":
    kbc()
