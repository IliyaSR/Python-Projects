#---------------------

def new_game():
    num_of_question = 0

    answers = []
    correct_answers = []

    for key, value in questions.items():
        print('---------------------')
        print(key)

        correct_answers.append(value)

        for option in options[num_of_question]:
            print(option)
        num_of_question += 1

        answer = input('A, B, C or D? : ')
        answers.append(answer)

    check_answer(correct_answers, answers)
def check_answer(correct_answers, answers):
    num_question = 0

    correct_questions = 0

    for correct_answer in correct_answers:
        if correct_answer == answers[num_question]:
            correct_questions += 1
        num_question += 1

    print('RESULTS')
    print('---------------------')
    print(f"Answers: {' '.join(correct_answers)}")
    print(f"Guesses: {' '.join(answers)}")

    display_score(correct_questions)

def display_score(num_of_correct_questions):

    result = 0

    if num_of_correct_questions == 1:
        result = '25%'
    elif num_of_correct_questions == 2:
        result = '50%'
    elif num_of_correct_questions == 3:
        result = '75%'
    elif num_of_correct_questions == 4:
        result = '100%'

    print(f"Your score is: {result}")


def play_again():
    play_one_more_time = input('Do you want play again? (yes or no)')

    if play_one_more_time == 'yes':
        return True
    elif play_one_more_time == 'no':
        return False





questions = {
    "Who created Python?": "A",
    'What year is created Python?': 'B',
    'Python is tributed in which comedy?': 'C',
    'Is the earth round?': 'A'
}

options = [
    ['A. Guido', 'B. Elon Musk', 'C. Bill Gates', 'D. Mark'],
    ['A. 1989', 'B. 1991', 'C. 2000', 'D. 2016'],
    ['A. Lonely Island', 'B. Smosh', 'C. Monty Python', 'D. SNL '],
    ['A. True', 'B. False', 'C. sometimes', 'D. What is earth?'],
]

new_game()

while play_again():
    new_game()

print('Byeeeee')