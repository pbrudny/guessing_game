import random
import json
import tkinter as tk
from tkinter import messagebox

class GeographyQuizApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Geography Quiz Game")

        self.questions = self.load_questions("questions.json")
        self.score = 0
        self.current_question_index = 0

        self.label_question = tk.Label(self.master, text="")
        self.label_question.pack(pady=10)

        self.entry_answer = tk.Entry(self.master)
        self.entry_answer.pack(pady=10)

        self.button_submit = tk.Button(self.master, text="Submit Answer", command=self.check_answer)
        self.button_submit.pack(pady=10)

        self.display_question()

    def load_questions(self, file_path):
        with open(file_path, 'r') as file:
            questions = json.load(file)
        return questions

    def display_question(self):
        if self.current_question_index < len(self.questions):
            question_text = f"{self.current_question_index + 1}. {self.questions[self.current_question_index]['question']}"
            self.label_question.config(text=question_text)
        else:
            self.show_final_score()

    def check_answer(self):
        user_answer = self.entry_answer.get().strip().capitalize()
        correct_answer = self.questions[self.current_question_index]['answer']

        if user_answer == correct_answer:
            self.score += 1

        self.current_question_index += 1
        self.entry_answer.delete(0, tk.END)
        self.display_question()

    def show_final_score(self):
        messagebox.showinfo("Quiz Completed", f"Quiz completed!\nYour final score is: {self.score}/10")
        self.master.destroy()

def main():
    root = tk.Tk()
    app = GeographyQuizApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
