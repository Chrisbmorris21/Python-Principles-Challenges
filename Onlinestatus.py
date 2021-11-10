statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
    }


def online_count(statuses):
    
    countOnline = 0
    
    for key in statuses:
        
        if statuses[key] == "online":
            countOnline = countOnline+1

    return int(countOnline)

online_count(statuses)
