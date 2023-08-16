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
        return f'''Вопрос: {self.question_text}\nСложность: {self.difficulty}/5'''

    def build_feedback(self, answer):
        """Возвращает :
        Ответ верный, получено __ баллов...либо...Ответ неверный, верный ответ __
        """
        if answer.lower() == self.right_answer.lower():
            return f'Ответ верный, получено {self.points} баллов!'
        if answer.lower() != self.right_answer.lower():
            return f'Ответ неверный, верный ответ: {self.right_answer}'