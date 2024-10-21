import requests

response = requests.get('https://api.github.com/search/repositories?q=html')

print(response.status_code)

