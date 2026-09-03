from api.client import FreeToGameClient
import pytest

@pytest.mark.xfail(
    raises=AssertionError,
    reason="BUG-001: фильтр ?category=shooter возвращает игры с другим genre",
)
def test_shooter_filter():
    client = FreeToGameClient()
    response = client.get_games("shooter")
    wrong_genre = []
    for game in response.json():
        if game["genre"] != "Shooter":
            wrong_genre.append(game["title"])
    assert len(wrong_genre) == 0, f"Игры не того жанра: {wrong_genre}"

def test_status_code_is_200():
    client = FreeToGameClient()
    response = client.get_games()
    assert response.status_code == 200