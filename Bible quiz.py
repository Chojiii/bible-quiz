print("welcome to the test!")
registered_name = input("what is your name?: ")
start = input("are you ready for the test?: ")
if start == "yes":
    print(f' okay! {registered_name} we wish you success.')
else:
    quit()

print("each question carries one mark. good luck!")


class Question:
    def __init__(self, prompt, answer):
        self.answer = answer
        self.prompt = prompt


question_prompts = [
    "1. where was jesus christ born\n(a) jerusalem\n(b) bethlehem\n(c) jerusalem\n(d) nigeria\n\n",
    "2. who gave birth to jesus\n(a) mary\n(b) esther\n(c) anna\n(d) hannah\n\n",
    "3. who was the first man God created\n(a) michael\n(b) noah\n(c) adam\n(d) abel\n\n",
    "4. who made the ark?\n(a) noah\n(b) Jesus\n(c) peter\n(d) judas\n\n",
    "5. which angel gave the message of Jesus chris being born?\n(a) angel michael\n(b) angel gabriel\n(c) angel "
    "uriel\n(d) raphael\n\n ",
    "6. what is the first book in the bible\n(a) genesis\n(b) revelations\n(c) luke\n(d)john\n\n",
    "7. what is the longest book in the bible\n(a) luke\n(b) timothy\n(c) psalm\n(d) proverbs\n\n",
    "8. what is the last book in the bible\n(a) psalm\n(b) revelations\n(c) luke\n(d) john\n\n",
    "9. who betrayed Jesus christ\n(a) peter\n(b) paul\n(c) saul\n(d) judas\n\n",
    "10. why did Jesus die for us?\n(a) to wash away our sins\n(b) because God asked him to\n(c) because he wanted "
    "to\n(d) because he loves us\n\n "

]

questions = [
    Question(question_prompts[0], "b"),
    Question(question_prompts[1], "a"),
    Question(question_prompts[2], "c"),
    Question(question_prompts[3], "a"),
    Question(question_prompts[4], "b"),
    Question(question_prompts[5], "a"),
    Question(question_prompts[6], "c"),
    Question(question_prompts[7], "b"),
    Question(question_prompts[8], "d"),
    Question(question_prompts[9], "a"),
]


def run_quiz(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("you got " + str(score) + "/" + str(len(questions)) + " totally")


run_quiz(questions)
