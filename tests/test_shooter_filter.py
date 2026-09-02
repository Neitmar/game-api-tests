import requests
import pytest

@pytest.mark.xfail(
    raises=AssertionError,
    reason="BUG-001: фильтр ?category=shooter возвращает игры с другим genre",
)
def test_shooter_filter():
    response = requests.get("https://www.freetogame.com/api/games?category=shooter")
    games = response.json()
    for game in games:
        assert game["genre"] == "Shooter", f"Пришла игра не того жанра: {game['title']}"

def test_status_code_is_200():
    response = requests.get("https://www.freetogame.com/api/games")
    assert response.status_code == 200