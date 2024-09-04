from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOUR = "#004cb5"

class QuizInterface:
    def __init__(self,quiz_brain: QuizBrain) -> None:
        self.quiz_brain = quiz_brain

        self.window = Tk()
        self.window.title("quizz")
        self.window.config(padx=20 ,pady=20, background=THEME_COLOUR)
        self.window.resizable(False, False)

        self.score_label= Label(text="score : 0", fg="white", bg=THEME_COLOUR, font=("Ariel", 15, "bold"))
        self.score_label.grid(row=0, column=0, columnspan=2)

        self.canvas = Canvas(width=500, height=250, bg="white")
        self.question = self.canvas.create_text(250, 125, text="hello", width=480, font=("Ariel", 25, "italic")) 
        self.canvas.grid(row=1, column=0, columnspan=2, padx=10, pady=20)

        correct_img = PhotoImage(file="images/true.png")
        self.button_correct = Button(image=correct_img, highlightthickness=0, relief=FLAT, command=self.given_true)
        self.button_correct.grid(row=2, column=0)

        wrong_img = PhotoImage(file="images/false.png")
        self.button_wrong = Button(image=wrong_img, highlightthickness=0, relief=FLAT, command=self.given_false)
        self.button_wrong.grid(row=2, column=1)

        self.get_next_qns()

        self.window.mainloop()

    def get_next_qns(self):
        if self.quiz_brain.still_has_questions():
            q_text = self.quiz_brain.next_question()
            self.canvas.itemconfig(self.question, text=q_text)
            self.score_label.config(text=f"Score : {self.quiz_brain.score}")
        else:
            self.window.after(1000, self.canvas.itemconfig(self.question, text=f"You have completed this quiz \n your score is: {self.quiz_brain.score}/{self.quiz_brain.question_number}"))
            self.button_wrong.config(state="disabled")
            self.button_correct.config(state="disabled")


    def given_true(self):
        user_answer = "True"
        self.show_result(user_answer)
        

    def given_false(self):
        user_answer = "False"
        self.show_result(user_answer)
        
           
    def show_result(self, user_answer):
        return_text = self.quiz_brain.check_answer(user_answer)
        self.canvas.itemconfig(self.question, text=return_text)
        self.window.after(1000, self.get_next_qns)

           
        

