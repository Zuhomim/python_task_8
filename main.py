import json


def load_data():
    """Создает список экземпляров класса Question на основе полученных данных файла questions"""
    with open("questions.json", mode='r', encoding='utf-8') as file:
        return json.load(file)


def create_question_list(data_, questions_):
    pass
    for item in data_:
        question_item = Question(item["q"], int(item["d"]), item["a"])
        questions_.append(question_item)
    return questions_


def count_results(question_list_):
    """Вычисляет итоги: кол-во набранных баллов и кол-во правильных ответов"""
    user_points = 0
    right_answers = 0
    for item in question_list_:
        if item.is_correct(item.answer):
            user_points += item.points
            right_answers += 1
    return f'''Вот и всё!\nОтвечено {right_answers} вопросов из {len(question_list_)}\nНабрано баллов: {user_points}'''


class Question:
    """Класс со св-вами: текст вопроса, сложность, правильный ответ, задан ли вопрос, ответ пользователя"""

    def __init__(self, question_text, difficulty, right_answer, is_question_asked=False, answer=None):
        self.question_text = question_text
        self.difficulty = difficulty
        self.right_answer = right_answer
        self.points = self.get_points()
        self.is_question_asked = is_question_asked
        self.answer = answer

    def __repr__(self):
        return f'Question({self.question_text}, {self.difficulty}, {self.right_answer})'

    def get_points(self):
        """Возвращает int, количество баллов.
        Баллы зависят от сложности: за 1 дается 10 баллов, за 5 дается 50 баллов.
        """
        self.points = self.difficulty * 10
        return self.points

    def is_correct(self, answer):
        """Возвращает True, если ответ пользователя совпадает 
        с верным ответов иначе False.
        """
        if answer.lower() == self.right_answer.lower():
            return True
        return False

    def build_question(self):
        """Возвращает вопрос в понятном пользователю виде, например:
        Вопрос: What do people often call American flag?
        Сложность: 4/5
        """
        return f'''Вопрос: {self.question_text}\nСложность: {self.difficulty}/{max_difficulty}'''

    def build_feedback(self, answer):
        """Возвращает :
        Ответ верный, получено __ баллов...либо...Ответ неверный, верный ответ __
        """
        if answer.lower() == self.right_answer.lower():
            return f'Ответ верный, получено {self.points} баллов!'
        if answer.lower() != self.right_answer.lower():
            return f'Ответ неверный, верный ответ: {self.right_answer}'


# Максимальная сложность для вывода корректной записи сложности в вопросе
max_difficulty = 5
# Перечень вопросов, загруженный из файла questions
question_list = load_data()
# Список вопросов (экземпляров класса Question) для запуска программы
questions = create_question_list(question_list, [])


# Основной код программы
def main():
    print("Игра начинается!")
    input("Нажмите Enter для запуска")
    # Цикл викторины
    for question in questions:
        print(question.build_question())
        question.is_question_asked = True

        # Ввод ответа пользователя
        user_answer = input()
        # Запись ответа пользователя в экземпляр класса Question
        question.answer = user_answer
        # Вывод результатов ответа на вопрос
        print(question.build_feedback(user_answer))

    # Печать результатов теста
    print(count_results(questions))


main()
