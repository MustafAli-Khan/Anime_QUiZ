from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self,  quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(self.window, text="Score", bg=THEME_COLOR,fg="white")
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(bg="white", width=300, height=250)
        self.question_text = self.canvas.create_text(150,
                                                     125,
                                                     width=250,
                                                     text="Question",
                                                     fill=THEME_COLOR,
                                                     font=("Arial", 20, "italic")
                                                     )

        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        true_img = PhotoImage(file="images/true.png")
        self.true_btn = Button(image=true_img, highlightthickness=0, command=self.true_pressed)
        self.true_btn.grid(column=0, row=2)

        false_img = PhotoImage(file="images/false.png")
        self.false_btn = Button(image=false_img, highlightthickness=0, command=self.false_pressed)
        self.false_btn.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score : {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)

        else:
            self.canvas.itemconfig(self.question_text, text="GAME OVER")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")


    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='#06D001')
        else:
            self.canvas.config(bg='#FE0000')
        self.window.after(1000, self.get_next_question)


