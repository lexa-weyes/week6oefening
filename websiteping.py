import subprocess
def ping(IP_adress):
    try:
        print(f"ping: {IP_adress}")
        result=subprocess.Popen(f"ping {IP_adress}")
        print(result)
    except:
        print("Geen IP-adress mee gegeven")

if __name__=="__main__":
    ping()