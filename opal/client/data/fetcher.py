import aiohttp
from typing import Dict, Any, Tuple

from horizon.config import BACKEND_SERVICE_URL, CLIENT_TOKEN
from horizon.utils import get_authorization_header


def tuple_to_dict(tup: Tuple[str, str]) -> Dict[str, str]:
    return dict([tup])


class DataFetcher:
    """
    fetches policy data from backend
    """
    def __init__(self, backend_url=BACKEND_SERVICE_URL, token=CLIENT_TOKEN):
        self._backend_url = backend_url
        self._token = token
        self._auth_headers = tuple_to_dict(get_authorization_header(token))

    async def fetch_policy_data(self) -> Dict[str, Any]:
        async with aiohttp.ClientSession() as session:
            async with session.get(
                f"{self._backend_url}/policy-config",
                headers=self._auth_headers
            ) as response:
                return await response.json()


data_fetcher = DataFetcher()


