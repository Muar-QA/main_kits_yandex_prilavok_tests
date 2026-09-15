import requests
import configuration
import data


# Функция для создания нового пользователя
def post_new_user(body):
    return requests.post(
        configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
        json=body
    )


# Функция для получения токена авторизации нового пользователя
def get_new_user_token():
    # Создаём пользователя
    response = post_new_user(data.user_body)
    # Возвращаем authToken из ответа
    return response.json()["authToken"]


# Функция для создания набора (kit) с передачей токена авторизации
def post_new_client_kit(kit_body, auth_token):
    # Заголовок Authorization с токеном (формат Bearer, как требует документация)
    headers = {
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json"
    }
    return requests.post(
        configuration.URL_SERVICE + configuration.CREATE_KIT_PATH,
        json=kit_body,
        headers=headers
    )