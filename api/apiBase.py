import requests
from typing import Optional, Dict, Any, Union


class APIBase:
    """
    A generic base class for working with HTTP-based APIs.
    """

    def __init__(self, base_url: str, headers: Optional[Dict[str, str]] = None, timeout: int = 10):
        self.base_url = base_url.rstrip("/")
        self.headers = headers or {}
        self.timeout = timeout

    def send_request(
        self,
        endpoint: str,
        method: str = "GET",
        params: Optional[Dict[str, str]] = None,
        data: Optional[Union[Dict, str]] = None,
        json: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Any:
        """
        Sends an HTTP request and returns the parsed JSON response.
        """
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        request_headers = self.headers.copy()
        if headers:
            request_headers.update(headers)

        # Remove any parameters that are None
        if params:
            params = {k: v for k, v in params.items() if v is not None}

        try:
            response = requests.request(
                method=method.upper(),
                url=url,
                headers=request_headers,
                params=params,
                data=data,
                json=json,
                timeout=self.timeout,
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            raise RuntimeError(f"HTTP error occurred: {http_err} - Response: {response.text}")
        except requests.exceptions.RequestException as err:
            raise RuntimeError(f"Error during request to {url}: {err}")
        except ValueError:
            raise RuntimeError("Invalid JSON response")
