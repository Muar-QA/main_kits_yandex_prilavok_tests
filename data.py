# data.py

# 1. Данные для создания пользователя. 
# создать пользователя и получить authToken для дальнейших тестов наборов.
user_body = {
    "firstName": "Aлина",
    "phone": "+79999999999",
    "address": "Москва, ул. Пушкина, д. 10",
    "email": "test@example.com",
    "password": "123456"
}

# 2. Базовое тело запроса для создания набора (Kit).
kit_body = {
    "name": "Тестовый набор"
}

    # Заголовок Authorization с токеном (формат Bearer, как требует документация)
kit_headers = {
    "Authorization": "Bearer ",
    "Content-Type": "application/json"
}
