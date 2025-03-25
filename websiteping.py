import subprocess
import json
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
if __name__=="__main__":
    ping()