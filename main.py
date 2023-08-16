from question import Question
from utils import load_data, create_question_list, count_results

# Основной код программы
if __name__ == '__main__':
    # Файл с вопросами для теста
    filename_ = 'questions.json'
    # Перечень вопросов, загруженный из файла questions
    question_list = load_data(filename_)
    # Список вопросов (экземпляров класса Question) для запуска программы
    questions = create_question_list(question_list, [], Question)

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
