#Communicates with ACLED API and retrieves incident data

#Third party libraries
from urllib import response

from urllib import response

from dotenv import load_dotenv
from datetime import datetime, timedelta
import os
import requests

#Load API credentials from local .env file before
#created an authenticated session
load_dotenv()  
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

    #Retry failed requests to tolerate network or API issues
    for attempt in range(1, 4): 
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

def get_page(session, url, params):
    """
    Retry failed requests to tolerate network or API issues.

    Args:
        session (requests.Session): An authenticated session object.
        url (str): The URL of the ACLED API endpoint.
        params (dict): The query parameters for the request.

    Returns:
        dict: The JSON response from the ACLED API.

    Raises:
        Exception: If the request fails after all retry attempts.
    """

    
    for attempt in range(1, 4):
        try:
            response = session.get(url, params=params)
            if response.status_code == 200:
                return response
        except requests.RequestException as error:
            print(error)
            raise Exception(f"Unable to contact ACLED API. Please check your internet connection.") from error

        if response.status_code == 200:
            incident_data = response.json()
            return incident_data
                   
        elif 400 <= response.status_code < 500:
            error = response.json()
            message = error.get("message", "Unknown client error.")
            raise Exception(message)
    
        elif 500 <= response.status_code:
             if attempt == 3:
                raise Exception(f"Request failed after {attempt} attempts. \n"
                                "The ACLED server may be unavailable. Please try again later. \n"
                                f"Status code: {response.status_code}")

def retrieve_incidents(session):
    """Retrieve the last 7 days of security incidents from the ACLED API
    Returns:
       dict: Incident data returned by ACLED API in JSON format
    Raises:
        Exception: If request fails after all retry attempts
    """
    start_date = "2024-07-21"
    end_date = "2025-07-28"
    url = "https://acleddata.com/api/acled/read?_format=json"
    params = {"country": "Syria",
            "event_date": f"{start_date}|{end_date}", 
            "event_date_where": "BETWEEN",
            "fields": "event_date|event_type|admin1|actor1|fatalities",
            "page":1}
    params["page"] = 1
    all_incidents = []

    while True:
        response = get_page(session, url, params)
        incident_data = response.json()

        all_incidents.extend(incident_data["data"])

        if len(incident_data["data"]) < 5000:
            break

        params["page"] += 1

    incident_data["start date"]=start_date
    incident_data["end date"]= end_date
    incident_data["data"] = all_incidents
    
    return incident_data
    
    
