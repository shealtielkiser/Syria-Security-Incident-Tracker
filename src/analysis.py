def summarize_incidents(parsed_incidents):
    """Summarize the parsed incident data by counting the number of incidents per event type.
    Args:
        parsed_incidents (list): List of parsed incident dictionaries
    Returns:
        dict: Summary of incidents by event type
    """
    summary = {}
    event_counts = {}
    governorate_counts = {}
    actor_counts = {}

    fatality_count=0
    
    incident_count=len(parsed_incidents)
    summary["total incidents"] = incident_count

    for incident in parsed_incidents:
        fatality_count += incident.get("fatalities", 0)
    summary["total fatalities"] = fatality_count

    for incident in parsed_incidents:
        event_type = incident["event_type"]
        if event_type not in event_counts:
            event_counts[event_type] = 0
        event_counts[event_type] += 1
    most_common_event_count =[]
    max_event=max(event_counts.values())
    for event_type, count in event_counts.items():
        if count == max_event:
            most_common_event_count.append(event_type)
    summary["most common event type"] = most_common_event_count


    for incident in parsed_incidents:
        admin1 = incident["admin1"]
        if admin1 not in governorate_counts:
            governorate_counts[admin1] = 0
        governorate_counts[admin1] += 1
    most_common_governorate = []
    max_governorate_count = max(governorate_counts.values())
    for governorate, count in governorate_counts.items():
        if count == max_governorate_count:
            most_common_governorate.append(governorate)
    summary["most common governorate"] = most_common_governorate

    for incident in parsed_incidents:
        actor1 = incident["actor1"]
        if actor1 not in actor_counts:
            actor_counts[actor1] = 0
        actor_counts[actor1] += 1
    most_common_actor = []
    max_actor_count = max(actor_counts.values())
    for actor, count in actor_counts.items():
        if count == max_actor_count:
            most_common_actor.append(actor)
    summary["most common actor"] = most_common_actor

    return summary


