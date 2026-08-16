import requests

response = requests.get("https://www.freetogame.com/api/games?category=shooter")
games = response.json()

for game in games:
    assert game["genre"] == "Shooter", f"Пришла игра не того жанра: {game['title']}"