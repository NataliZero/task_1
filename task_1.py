import requests

# Отправляем GET-запрос
response = requests.get('https://api.github.com/search/repositories?q=html')

# Проверяем статус-код
print(response.status_code)

# Выводим содержимое ответа в формате JSON
print(response.json())
