import sender_stand_request
import data


    # Функция для изменения значения в параметре name в теле запроса
def get_kit_body(name):
    # Копируется словарь с телом запроса из файла data
    current_body = data.kit_body.copy()
    # Изменение значения в поле name
    current_body["name"] = name
    # Возвращается новый словарь с нужным значением name
    return current_body


    # Функция для позитивной проверки
def positive_assert(kit_body):
    # Получаем токен для авторизации
    auth_token = sender_stand_request.get_new_user_token()
    # В переменную kit_response сохраняется результат запроса на создание набора
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)

    # Проверяется, что код ответа равен 201
    assert kit_response.status_code == 201
    # Проверяется, что в ответе поле name совпадает с полем name в запросе
    assert kit_response.json()["name"] == kit_body["name"]


    # Тест 1. Допустимое количество символов (1)
def test_create_kit_1_letter_in_name_get_success_response():
    kit_body = get_kit_body("a")
    positive_assert(kit_body)

    # Тест 2. Допустимое количество символов (511)
def test_create_kit_511_letters_in_name_get_success_response():
    kit_body = get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")
    positive_assert(kit_body)


    # Функция для негативной проверки (код 400)
def negative_assert_code_400(kit_body):
    # Получаем токен для авторизации
    auth_token = sender_stand_request.get_new_user_token()
    # В переменную kit_response сохраняется результат запроса на создание набора
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)

    # Проверяется, что код ответа равен 400
    assert kit_response.status_code == 400

    # Тест 3. Ошибка. Количество символов меньше допустимого (0)
def test_create_kit_0_letters_in_name_get_error_response():
    kit_body = get_kit_body("")
    negative_assert_code_400(kit_body)

    # Тест 4. Ошибка. Количество символов больше допустимого (512)
def test_create_kit_512_letters_in_name_get_error_response():
    kit_body = get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")
    negative_assert_code_400(kit_body)

    # Тест 5. Разрешены английские буквы
def test_create_kit_english_letters_in_name_get_success_response():
    kit_body = get_kit_body("QWErty")
    positive_assert(kit_body)

    # Тест 6. Разрешены русские буквы
def test_create_kit_russian_letters_in_name_get_success_response():
    kit_body = get_kit_body("Мария")
    positive_assert(kit_body)

    # Тест 7. Разрешены спецсимволы
def test_create_kit_special_symbols_in_name_get_success_response():
    kit_body = get_kit_body('"№%@",')
    positive_assert(kit_body)

    # Тест 8. Разрешены пробелы
def test_create_kit_spaces_in_name_get_success_response():
    kit_body = get_kit_body(" Человек и КО ")
    positive_assert(kit_body)

    # Тест 9. Разрешены цифры
def test_create_kit_numbers_in_name_get_success_response():
    kit_body = get_kit_body("123")
    positive_assert(kit_body)

    # Тест 10. Ошибка. Параметр не передан в запросе
def test_create_kit_no_name_get_error_response():
    # Копируется словарь с телом запроса из файла data
    kit_body = data.kit_body.copy()
    # Удаление параметра name из запроса
    kit_body.pop("name")
    # Проверка полученного ответа
    negative_assert_code_400(kit_body)

# Тест 11. Ошибка. Параметр name имеет неверный тип (число вместо строки)
def test_create_kit_wrong_type_name_get_error_response():
    # Копируем словарь с телом запроса из файла data, чтобы не потерять исходные данные
    kit_body = data.kit_body.copy()
    # Присваиваем значение 123 (число, без кавычек). 
    # В JSON это будет тип number, а не string — именно это мы и хотим проверить.
    kit_body["name"] = 123
    # Проверка полученного ответа
    negative_assert_code_400(kit_body)


