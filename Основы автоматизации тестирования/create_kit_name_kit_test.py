import sender_stand_request
import data


#Создание нового пользователя и запоминание токена авторизации
def get_new_user_token():
    user_body = data.user_body
    response_user = sender_stand_request.post_new_user(user_body)
    return response_user.json()["authToken"]


# эта функция меняет значение в параметре name
def get_kit_body(name):
    # копирование словаря с телом запроса из файла data, чтобы не потерять данные в исходном словаре
    current_body = data.kit_body.copy()
    # изменение значения в поле name
    current_body["name"] = name
    # возвращается новый словарь с нужным значением name
    return current_body


# Функция для позитивной проверки
# Проверка создания набора. Пользовталеь авторизован. Код = 201
def positive_assert(name):
    # В переменную kit_body сохраняется обновленное тело запроса
    kit_body = get_kit_body(name)
    # в переменную kit_response сохраняется результат запроса на создание набора, пользователь авторизован
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    # Проверяется, что код ответа равен 201
    assert kit_response.status_code == 201
    # Проверяется, что в ответе есть поле auth_token, и оно равно значению name
    assert kit_response.json()["name"] == kit_body["name"]


# Функция для негативной проверки
# Ошибка. Набор не создается. Пользователь авторизован. Код = 400
def negative_assert(name):
    # В переменную kit_body сохраняется обновленное тело запроса
    kit_body = get_kit_body(name)
    # В переменную kit_response сохраняется результат запроса на создание набора, пользователь авторизован
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    # Проверяется, что код ответа равен 400
    assert kit_response.status_code == 400
    # Проверка, что в теле ответа атрибут "code" равен 400
    assert kit_response.json()["code"] == 400

    # Функция для негативной проверки
    # В ответе ошибка: "Не все необходимые параметры были переданы"


def negative_assert_no_kit_body(kit_body):
    # В переменную response сохрани результат вызова функции
    response = sender_stand_request.post_new_client_kit(kit_body)
        # Проверь, что код ответа — 400
    assert response.status_code == 400
       # Проверка, что в теле ответа атрибут "code" равен 400
    assert response.json()["code"] == 400


# Тест 1. PASSED. Допустимое количество символов - 1. name = "a"
#def test_create_user_2_letter_in_first_name_get_success_response():
def test_1_create_kit_name_1_letter_get_success_response():
    positive_assert("а")

# Тест 2. PASSED. Допустимое количество символов - 511. name = "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"
def test_2_create_kit_name_511_letter_get_success_response():
    positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")

# Тест 3. FAILED. Количество символов меньше допустимого - 0. name = ""
def test_3_create_kit_name_0_letter_get_success_response():
    negative_assert("")

# Тест 4. FAILED. Количество символов больше допустимого - 512. name = "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD"
def test_4_create_kit_name_512_letter_get_error_response():
    negative_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")

# Тест 5. PASSED. Разрешены английские буквы. name = "QWErty"
def test_5_create_kit_name_english_letter_get_success_response():
    positive_assert("QWErty")

# Тест 6. PASSED. Разрешены русские буквы. name = "Мария"
def test_6_create_kit_name_russian_letter_get_success_response():
    positive_assert("Мария")

# Тест 7. PASSED. Разрешены спецсимволы. name = '"№%@",'
def test_7_create_kit_name_special_simbol_get_success_response():
    positive_assert('"№%@,"')

# Тест 8. PASSED. Разрешены пробелы. name = Человек и КО
def test_8_create_kit_name_space_get_success_response():
    positive_assert(" Человек и КО ")

# Тест 9. PASSED. Разрешены цифры. name = "123"
def test_9_create_kit_name_numbers_get_success_response():
   positive_assert("123")


# Тест 10. FILED. Параметр не передан в запросе. name = null
def test_10_create_kit_no_name_get_error_response():
    # Копируется словарь с телом запроса из файла data в переменную kit_body
    kit_body = data.kit_body.copy()
    # Удаление параметра name из запроса
    kit_body.pop("name")
    # Проверка полученного ответа
    negative_assert_no_kit_body(kit_body)


# Тест 11. FILED. Передан другой тип параметра (число). name =  123
def test_11_create_kit_name_number_type_get_error_response():
    negative_assert(123)