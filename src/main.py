print("Syria Security Incident Tracker")
print("Retrieving security incidents...")
from fetch import retrieve_incidents
incident_data=retrieve_incidents()