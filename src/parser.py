#Normalizes API respondse into consistent internal format

def parse_incidents(incident_data):
    parsed_incidents=[]
    for incident in incident_data:
        parsed_incident = {"event_date": incident.get("event_date", "Unknown"),
                            "event_type": incident.get("event_type", "Unknown"),
                            "admin1": incident.get("admin1", "Unknown"),
                            "actor1": incident.get("actor1", "Unknown"),
                            "fatalities": incident.get("fatalities", 0)}
        parsed_incidents.append(parsed_incident)
    return parsed_incidents

