import requests

response = requests.get("https://www.freetogame.com/api/games?platform=pc")
games = response.json()

assert response.status_code == 200
assert games[0]["title"] == "Overwatch", f"Получил: {games[0]['title']}"