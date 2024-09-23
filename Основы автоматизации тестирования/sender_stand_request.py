import configuration
import requests
import data
import create_kit_name_kit_test

# Создание пользователя
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body, # тело
                         headers=data.headers) # заголовки


def post_new_client_kit(kit_body):
    # копирование словаря с телом запроса из файла data, чтобы не потерять данные в исходном словаре
    headers_dict = data.headers.copy()
    # Передаем параметр authToken
    headers_dict["Authorization"] = "Bearer " + create_kit_name_kit_test.get_new_user_token();
    # Возвращаем ответ созданного набора под авторизованным пользователем
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_KIT_PATH,  # подставялем полный url
                         json=kit_body, # тело
                         headers=headers_dict)  # заголовки