import subprocess
import json
import time
from datetime import datetime
def ping(IP_adress):
    try:
        #print(f"ping: {IP_adress}")
        result=subprocess.run(f"ping {IP_adress}", shell=True, capture_output=True, text=True)
    except:
        print("Geen IP-adress mee gegeven")
    return result.stdout

def servers_to_log(servers, filename="servers.json"):
    with open(filename, 'w') as f:
        json.dump(servers, f, indent=4)

def servers_naam_to_log(servers, filename="servers_naam.json"):
    with open(filename, 'w') as f:
        json.dump(servers, f, indent=4)

def servers_from_log():
    try:
        with open("servers.json", 'r') as servers:
            return json.load(servers)
    except FileNotFoundError:
        return []

def servers_naam_from_log():
    try:
        with open("servers_naam.json", 'r') as naam_servers:
            return json.load(naam_servers)
    except FileNotFoundError:
        return []
def datum_log():
    try:
        with open("history.json", 'r') as geschiedenis:
            data = json.load(geschiedenis)
            if not isinstance(data, list):  # Zorgt ervoor dat data een lijst is
                data = []
    except (FileNotFoundError, json.JSONDecodeError):
        data = []  # Als het bestand niet bestaat of corrupt is, begin met een lege lijst

    tijd = datetime.now().isoformat()
    data.append(f"timestamp: {tijd}")

    with open("history.json", 'w') as f:
        json.dump(data, f, indent=4)

    
def geschiedenis_log(naam_server,getal):
    try:
        with open("history.json", 'r') as geschiedenis:
            data = json.load(geschiedenis)
            if not isinstance(data, list):  # Zorgt ervoor dat data een lijst is
                data = []
    except (FileNotFoundError, json.JSONDecodeError):
        data = []  # Als het bestand niet bestaat of corrupt is, begin met een lege lijst
    match getal:
        case 0:
            data.append(f"{naam_server}: Received {getal}.")
        case 1:
            data.append(f"{naam_server}: Received {getal}.")
        case 2:
            data.append(f"{naam_server}: Received {getal}.")
        case 3:
            data.append(f"{naam_server}: Received {getal}.")
        case 4:
            data.append(f"{naam_server}: Received {getal}.")
    with open("history.json", 'w') as f:
        json.dump(data, f, indent=4)


if __name__=="__main__":
    ping()