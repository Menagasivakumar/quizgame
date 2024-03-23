import tkinter as tk
from tkinter import messagebox
from random import shuffle

class QuizGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")

        self.question = [
            {
                "question": "Which is the largest planet in our solar system?",
                "options": ["jupiter", "saturn", "neptune", "earth"],
                "answer": "jupiter"
            },
            {
                "question": "what is the capital of India?",
                "options": ["delhi", "tamilnadu", "kolkata", "mumbai"],
                "answer": "delhi"
            },
            {
                "question": "What is the smallest unit of data in a computer?",
                "options": ["byte", "megabyte", "bit", "gigabyte"],
                "answer": "bit"
            },
            {
                "question": "which number is either prime nor composite number?",
                "options": ["0", "1", "2", "4"],
                "answer": "1"
            },
            {
                "question": "which planet is called a'red planet'?",
                "options": ["mars", "earth", "venus", "jupiter"],
                "answer": "mars"
            },
            {
                "question": "What is the largest ocean on Earth?",
                "options": ["indian ocean", "pacific ocean", "artic ocean", "antartic ocean"],
                "answer": "pacific ocean"
            },
            {
                "question": "What is the tallest mountain in the world?",
                "options": ["Mount Everest", "Kangchenjunga", "Manaslu", "Makalu"],
                "answer": "Mount Everest"
            },
            {
                "question": "What is the chemical symbol for water?",
                "options": ["o2", "Naoh", "H2o", "Nacl"],
                "answer": "H2o"
            },
            {
                "question": "What is the capital of TamilNadu?",
                "options": ["Salem", "coimbatore", "pondicherry", "chennai"],
                "answer": "chennai"
            },
            {
                "question": "How many consonants are there in the English alphabet?",
                "options": ["26", "27", "21", "6"],
                "answer": "21"
            },
            {
                "question": "Name the national flower of India?",
                "options": ["jasmin", "Rose", "Lotus", "sunflower"],
                "answer": "Lotus"
            }
        ]
        self.score = 0
        self.current_question = 0

        self.question_label = tk.Label(self.root, text="", font=("Arial", 14), wraplength=400)
        self.question_label.pack(pady=20)

        self.option_button = []
        for i in range(4):
            button = tk.Button(self.root, text="", font=("Arial", 14), width=30, command=lambda idx=i: self.check_answer(idx))
            button.pack(pady=5)
            self.option_button.append(button)

        self.score_label = tk.Label(self.root, text="score:0", font=("Arial", 12))
        self.score_label.pack(pady=20)

        self.next_question()

    def next_question(self):
        if self.current_question < len(self.question):
            question = self.question[self.current_question]
            self.question_label.config(text=question["question"])
            option = question["options"]
            shuffle(option)
            for i in range(4):
                self.option_button[i].config(text=option[i])
            self.score_label.config(text="score:{}".format(self.score))
        else:
            self.end_game()

    def check_answer(self, selected_option):
        question = self.question[self.current_question]
        selected_answer = question["options"][selected_option]
        correct_answer = question["answer"]
        if selected_answer == correct_answer:
            self.score += 1
        self.current_question += 1
        self.next_question()

    def end_game(self):
        messagebox.showinfo("Game over", "Quiz has ended\n Your score: {}".format(self.score))
        self.root.destroy()

root = tk.Tk()
quiz_game = QuizGame(root)
root.mainloop()
