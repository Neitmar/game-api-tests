import requests

class FreeToGameClient:
    BASE_URL = "https://www.freetogame.com/api"

    def get_games(self, category=None):
        url = f"{self.BASE_URL}/games"
        params = {}
        if category is not None:
            params["category"] = category
        return requests.get(url, params=params)