# define question dictionary
question = {
    "2+3": ['2', '3', '5', '9'],
    "2-1": ['2', '1', '5'],
    "3+3": ['3', '6', '9', '7']
}
# define answer list
ans = ['5', '1', '6']

current_question = 0
user_score = 0

def start_quiz():
    global current_question, user_score
    user_score = 0
    current_question = 0
    next_question()

def next_question():
    global current_question
    if current_question < len(question):
        check_ans()
        c_question = list(question.keys())[current_question]
        print(f"Question: {c_question}")
        options = question[c_question]
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
        user_input = input("Select the correct option number: ")
        try:
            selected_option = options[int(user_input) - 1]
        except (IndexError, ValueError):
            selected_option = 'None'
        user_ans = selected_option
        current_question += 1
        next_question()
    else:
        check_ans()
        print(f"Your Score is {user_score} out of {len(question)}")
        print("Thanks for Participating")

def check_ans():
    global current_question, user_score
    if current_question > 0:
        previous_question = list(question.keys())[current_question - 1]
        temp_ans = input(f"Your answer for {previous_question} was: ")
        if temp_ans == ans[current_question - 1]:
            user_score += 1

if __name__ == "__main__":
    print("Welcome to the Quiz App!")
    start_quiz()
