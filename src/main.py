#Coordinates workflow and displays the analyst dashboard

from fetch import authenticate, retrieve_incidents
from parser import parse_incidents
from analysis import summarize_incidents

session = authenticate()
incident_data = retrieve_incidents(session)
parsed_incidents=parse_incidents(incident_data["data"])
summary=summarize_incidents(parsed_incidents)
start_date= incident_data["start date"]
end_date= incident_data["end date"]

WIDTH=60
print("=" * WIDTH)
title= "SYRIA SECURITY INCIDENT TRACKER"
print(title.center(WIDTH))
print("=" * WIDTH)

print()
print("-" * WIDTH)
print("Reporting Period")
print("-" * WIDTH)
print(f"{start_date} - {end_date}")

print()
if summary["total incidents"]== 0:
    print("No security incidents were reported during the selected reporting period.")
    print()
else:
    print("-" * WIDTH)
    print("Overall Activity")
    print("-" * WIDTH)

    label_incidents="Total incidents"
    line_incidents=f"{label_incidents.ljust(30)}{str(summary["total incidents"]).rjust(15)}"
    print(line_incidents)
    label_fatalities="Total fatalities"
    line_fatalities=f"{label_fatalities.ljust(30)}{str(summary["total fatalities"]).rjust(15)}"
    print(line_fatalities)

    print()
    print("-" * WIDTH)
    print("Incident Patterns")
    print("-" * WIDTH)
    print("Most Common Event Type(s)")
    for event in summary["most common event type"]:
        print(f"• {event}")
    print()
    print("Most Active Governorate(s)")
    for admin1 in summary["most common governorate"]:
        print(f"• {admin1}")
    print()
    print("Most Active Actor(s)")
    for actor1 in summary["most common actor"]:
        print(f"• {actor1}")
    print()