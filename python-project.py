import random
import time
import tkinter as tk
from tkinter import messagebox

questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A) Paris", "B) London", "C) Rome", "D) Berlin"],
        "answer": "A"
    },
    {
        "question": "Who wrote 'To Kill a Mockingbird'?",
        "options": ["A) Harper Lee", "B) J.K. Rowling", "C) Ernest Hemingway", "D) Mark Twain"],
        "answer": "A"
    },
    # Ajoute d'autres questions ici
]

random.shuffle(questions)

score = 0
current_question = 0

def start_console_quiz():
    global score
    time_limit = 10 
    for i, q in enumerate(questions, 1):
        print(f"\nQuestion {i}: {q['question']}")
        for option in q["options"]:
            print(option)
        
        start_time = time.time()
        answer = input("Votre réponse (A, B, C, D): ").strip().upper()
        
        elapsed_time = time.time() - start_time
        if elapsed_time > time_limit:
            print("Temps écoulé!")
            continue
        elif answer == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. La bonne réponse est: {q['answer']}")
    
    print(f"\nVotre score final est de {score}/{len(questions)}.")
    save_high_score(score)
    display_high_scores()

def save_high_score(score):
    with open("high_scores.txt", "a") as f:
        f.write(f"{score}\n")

def display_high_scores():
    try:
        with open("high_scores.txt", "r") as f:
            scores = [int(line.strip()) for line in f]
            scores.sort(reverse=True)
            print("\n--- Meilleurs Scores ---")
            for i, score in enumerate(scores[:5], 1): 
                print(f"{i}. {score}")
    except FileNotFoundError:
        print("Aucun score enregistré.")

def start_gui_quiz():
    global window, question_label, option_buttons
    window = tk.Tk()
    window.title("Quiz Game")

    question_label = tk.Label(window, text="", font=("Arial", 16))
    question_label.pack(pady=20)

    option_buttons = []
    for i in range(4):
        btn = tk.Button(window, text="", font=("Arial", 14), width=20)
        btn.pack(pady=5)
        option_buttons.append(btn)

    display_question()
    window.mainloop()

def check_answer(selected_option):
    global score, current_question
    if selected_option == questions[current_question]["answer"]:
        score += 1
        messagebox.showinfo("Résultat", "Correct!")
    else:
        messagebox.showinfo("Résultat", f"Incorrect! La bonne réponse est {questions[current_question]['answer']}")
    
    current_question += 1
    if current_question < len(questions):
        display_question()
    else:
        messagebox.showinfo("Fin du Quiz", f"Votre score final est {score}/{len(questions)}")
        save_high_score(score)
        display_high_scores()
        window.quit()

def display_question():
    question_label.config(text=questions[current_question]["question"])
    for i, option in enumerate(questions[current_question]["options"]):
        option_buttons[i].config(text=option.split(") ")[1], command=lambda opt=option.split(") ")[0]: check_answer(opt))


mode = input("Choisissez le mode (console/gui): ").strip().lower()
if mode == "console":
    start_console_quiz()
elif mode == "gui":
    start_gui_quiz()
else:
    print("Mode invalide.")
