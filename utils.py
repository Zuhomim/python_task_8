import json


def load_data(filename):
    """Загружает данные из файла json"""
    with open(filename, mode='r', encoding='utf-8') as file:
        return json.load(file)


def create_question_list(data_, questions_, question_class):
    """Создает список экземпляров класса Question на основе полученных данных"""
    for item in data_:
        question_item = question_class(item["q"], int(item["d"]), item["a"])
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
