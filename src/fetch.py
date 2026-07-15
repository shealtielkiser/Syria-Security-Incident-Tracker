from dotenv import load_dotenv
from datetime import datetime, timedelta
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
                print(error)
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

def retrieve_incidents(session):
    """Retrieve the last 7 days of security incidents from the ACLED API
    Returns:
       dict: Incident data returned by ACLED API in JSON format
    Raises:
        Exception: If request fails after all retry attempts
    """
    #Generate the date range

    start_date = "2025-07-01" 
    end_date = "2025-07-08"
    url = "https://acleddata.com/api/acled/read?_format=json"
    params = {"country": "Syria",
              "event_date": f"{start_date}|{end_date}", 
              "event_date_where": "BETWEEN",
              "fields": "event_date|event_type|admin1|actor1|fatalities",}
    for attempt in range(1, 4):  # Retry server errors
        try:
            response = session.get(url, params=params)
        except requests.RequestException as error:
            raise Exception(f"Unable to contact ACLED API. Please check your internet connection.") from error

        if response.status_code == 200:
            return response.json()
        elif 400 <= response.status_code < 500:
            error = response.json()
            message = error.get("message", "Unknown client error.")
            raise Exception(message)
        elif 500 <= response.status_code:
             continue  # Retry on server errors
    raise Exception(f"Request failed after {attempt} attempts. \n"
        "The ACLED server may be unavailable. Please try again later. \n"
        f"Status code: {response.status_code}")
