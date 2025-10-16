import requests

response = requests.get("https://api.open-meteo.com/v1/forecast?latitude=55.75&longitude=37.62&current_weather=true")

print("Статус-код:", response.status_code)
print("Тип данных:", response.headers.get("Content-Type"))
print("Тело ответа (первые 200 символов):")
print(response.text[:200])