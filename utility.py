def goThroughQuestions(question_list,genre):
    count = 0
    for x in range(question_list[genre]['number_of_questions']):
        printQuestion(question_list[genre][f'test_question{x}'])
        if checkAnswer(getAnswer(), question_list[genre][f'test_question{x}'],"Correct", question_list[genre][f'test_question{x}']['wrong_answer_output'] ):
            count = count + 1
    print()
    return count

def printQuestion(question):
    print(question['question'])

    for x in range(question['number_question_options']):
        print(f'{x}) ' + question['question_options'][f'{x}'])

def getAnswer():
    answer = input('> ')
    return answer

def checkAnswer(answer, question, correct_output='', wrong_output=''):
    if answer in question['correct_answer'] or answer == question['correct_answer']:
        print(correct_output)
        return True
    elif answer == 'hint':
        print(question['hint'])
        checkAnswer(getAnswer(), question, correct_output, wrong_output)
    else:
        print(wrong_output)
        return False

def printGenres(question_list):
    print("Choose a topic: ")
    for x in question_list['genres']:
        print(f'- {x}')
