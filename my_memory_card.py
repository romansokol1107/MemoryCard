#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QPushButton, QLabel, QButtonGroup)
from random import shuffle, randint

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
    
app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Memory card')
main_win.total = 0
main_win.score = 0
main_win.questions_asked = list()
but_answer = QPushButton('Ответить')
question = QLabel('Самый сложный вопрос в мире!')
RadioGroupBox = QGroupBox('Варианты ответов')
rbtn1 = QRadioButton('Вариант 1')
rbtn2 = QRadioButton('Вариант 2')
rbtn3 = QRadioButton('Вариант 3')
rbtn4 = QRadioButton('Вариант 4')
RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn1)
RadioGroup.addButton(rbtn2)
RadioGroup.addButton(rbtn3)
RadioGroup.addButton(rbtn4)

layout_main = QHBoxLayout()
layout_1 = QVBoxLayout()
layout_2 = QVBoxLayout()

layout_1.addWidget(rbtn1)
layout_1.addWidget(rbtn2)

layout_2.addWidget(rbtn3)
layout_2.addWidget(rbtn4)

layout_main.addLayout(layout_1)
layout_main.addLayout(layout_2)
RadioGroupBox.setLayout(layout_main)


AnsGroupBox = QGroupBox('Результат теста')
result = QLabel('Правильно/неправильно')
correct = QLabel('Правильный ответ будет здесь')
layout_res = QVBoxLayout()
layout_res.addWidget(result, alignment = (Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(correct, alignment = Qt.AlignHCenter)
AnsGroupBox.setLayout(layout_res)
layout_H1 = QHBoxLayout()
layout_H2 = QHBoxLayout()
layout_H3 = QHBoxLayout()

layout_H1.addWidget(question, alignment = (Qt.AlignHCenter | Qt.AlignVCenter))
layout_H2.addWidget(RadioGroupBox)
layout_H2.addWidget(AnsGroupBox)
AnsGroupBox.hide()
layout_H3.addStretch(1)
layout_H3.addWidget(but_answer, stretch = 2)
layout_H3.addStretch(1)

layout_card = QVBoxLayout()
layout_card.addLayout(layout_H1, stretch = 2)
layout_card.addLayout(layout_H2, stretch = 8)
layout_card.addStretch(1)
layout_card.addLayout(layout_H3, stretch = 1)
layout_card.addStretch(1)
layout_card.setSpacing(5)
main_win.setLayout(layout_card)

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    but_answer.setText('Следующий вопрос')

def show_question():
    AnsGroupBox.hide()
    RadioGroupBox.show()
    but_answer.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn1.setChecked(False)
    rbtn2.setChecked(False)
    rbtn3.setChecked(False)
    rbtn4.setChecked(False)
    RadioGroup.setExclusive(True)


answers = [rbtn1, rbtn2, rbtn3, rbtn4]

def ask(q: Question):
    shuffle(answers)
    correct.setText(q.right_answer)
    question.setText(q.question)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    show_question()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно')
        main_win.score += 1
    elif answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
        show_correct('Неверно')
    print('Статистика')
    print('-Всего вопросов:', main_win.total)
    print('-Правильных ответов:', main_win.score)
    print('Рейтинг:', str(main_win.score * 100//main_win.total) + '%')


def show_correct(res):
    result.setText(res)
    show_result()


quest = Question('В каком году основана Москва?', '1147', '1063', '1256', '1188')
quest2 = Question('Когда был совершен первый полет человека в космос?', '1961', '1932', '1898', '1990')
quest3 = Question('Когда был открыт материк Америка?', '1492', '1345', '1427', '1566')


questions = []
questions.append(quest)
questions.append(quest2)
questions.append(quest3)


def next_question():
    cur_question = randint(0, len(questions) -1)
    while cur_question in main_win.questions_asked:
        cur_question = randint(0, len(questions) -1)
    q = questions[cur_question]
    main_win.questions_asked.append(cur_question)
    main_win.total += 1
    if main_win.total%len(questions) == 0:
        main_win.questions_asked = list()
    ask(q)

def click_ok():
    if but_answer.text() == 'Ответить':
        check_answer()
    else:
        next_question()
next_question()

but_answer.clicked.connect(click_ok)
main_win.show()
app.exec_()
