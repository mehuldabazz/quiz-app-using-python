from tkinter import *
from tkinter.ttk import Progressbar

# define question dictionary
question = {
    "2+3": ['2', '3', '5', '9'],
    "2-1": ['2', '1', '5', '0'],
    "3+3": ['3', '6', '9', '7'],
    "5-2": ['2', '3', '5', '1'],
    "6/2": ['3', '2', '6', '4'],
    "4*2": ['6', '8', '2', '9'],
    "9-3": ['6', '3', '9', '7'],
    "7+1": ['7', '8', '9', '6'],
    "8-4": ['3', '4', '5', '6'],
    "10/2": ['2', '4', '5', '6']
}
# define answer list
ans = ['5', '1', '6', '3', '3', '8', '6', '8', '4', '5']

current_question = 0


def start_quiz():
    start_button.forget()
    next_button.pack()
    next_question()


def next_question():
    global current_question
    if current_question < len(question):
        # get key or question that need to be printed
        check_ans()
        user_ans.set('None')
        c_question = list(question.keys())[current_question]
        # clear frame to update its content
        clear_frame()
        # printing question
        Label(f1, text=f"Question : {c_question}", padx=15,
              font="calibre 16 normal").pack(anchor=NW)
        # printing options
        for option in question[c_question]:
            Radiobutton(f1, text=option, variable=user_ans,
                        value=option, padx=28, font="calibre 14").pack(anchor=NW)
        # update progress bar
        progress['value'] = ((current_question + 1) / len(question)) * 100
        current_question += 1
    else:
        next_button.forget()
        check_ans()
        clear_frame()
        output = f"Your Score is {user_score.get()} out of {len(question)}"
        Label(f1, text=output, font="calibre 25 bold").pack()
        Label(f1, text="Thanks for Participating",
              font="calibre 18 bold").pack()


def check_ans():
    temp_ans = user_ans.get()
    if temp_ans != 'None' and temp_ans == ans[current_question-1]:
        user_score.set(user_score.get()+1)


def clear_frame():
    for widget in f1.winfo_children():
        widget.destroy()


if __name__ == "__main__":
    root = Tk()
    # setup basic window
    root.title("GFG QUIZ APP")
    root.geometry("850x520")
    root.minsize(800, 400)

    user_ans = StringVar()
    user_ans.set('None')
    user_score = IntVar()
    user_score.set(0)

    Label(root, text="Quiz App",
          font="calibre 40 bold",
          relief=SUNKEN, background="cyan",
          padx=10, pady=9).pack()
    Label(root, text="", font="calibre 10 bold").pack()
    start_button = Button(root,
                          text="Start Quiz",
                          command=start_quiz,
                          font="calibre 17 bold")
    start_button.pack()

    f1 = Frame(root)
    f1.pack(side=TOP, fill=X)

    next_button = Button(root, text="Next Question",
                         command=next_question,
                         font="calibre 17 bold")

    # Add progress bar
    progress = Progressbar(root, orient=HORIZONTAL, length=100, mode='determinate')
    progress.pack(pady=20)

    root.mainloop()

