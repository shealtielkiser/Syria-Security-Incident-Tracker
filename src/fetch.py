def retrieve_incidents():
    """Retrieve the last 7 days of security incidents from the ACLED API
    Returns:
       dict: Incident data returned by ACLED API in JSON format
    Raises:
        Exception: If request fails after all retry attempts
    """
    return{}
from dotenv import load_dotenv
import os
import requests
load_dotenv()  # Load environment variables from .env file  
def authenticate():
    """
    Authenticate with the ACLED API.

    Returns:
        requests.Session:
            An authenticated session object.

    Raises:
        Exception:
            If authentication fails, the network is unavailable,
            or the server remains unavailable after three retries.
    """
    username = os.getenv('ACLED_USERNAME')
    password = os.getenv('ACLED_PASSWORD')
    if not username or not password:
        raise Exception ("Authentication failed. Please check your username and password.")
    payload = {"name": username, "pass": password}
    session = requests.Session()
    for attempt in range(1, 4):  # Retry server errors
            try:
                response = session.post("https://acleddata.com/user/login?_format=json", json=payload)
            except requests.RequestException as error:
                raise Exception(f"Unable to contact ACLED API. Please check your internet connection.") from error

            if response.status_code == 200:
                return session
            elif 400 <= response.status_code < 500:
                error = response.json()
                message = error.get("message", "Unknown client error.")
                raise Exception(message)
            elif 500 <= response.status_code:
                 continue  # Retry on server errors
    raise Exception(f"Authentication failed after {attempt} attempts. \n"
        "The ACLED server may be unavailable. Please try again later. \n"
        f"Status code: {response.status_code}")

