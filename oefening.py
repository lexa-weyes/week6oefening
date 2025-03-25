import sys
import websiteping
import websiteGenerator

naam_servers=websiteping.servers_naam_from_log()
Servers=websiteping.servers_from_log()

if len(sys.argv) > 1:
    antwoord=websiteping.ping(sys.argv[1])
    if antwoord is None or "100% loss" in str(antwoord):
        print("\033[31mServer is niet online\033[0m")
    elif "0% loss" in str(antwoord):
        print("\033[32mServer online\033[0m")
    else:
        print("\033[38;5;208mSlechte verbinding\033[0m")
else:
    print("Selecteer een optie:")
    antwoord = input("1) Server toevoegen\n2) Server Verwijderen\n3) lijst tonen\n4) Pingen \n5) Stoppen\n>")
    while antwoord!=5:
        try:
            antwoord=int(antwoord)
        except TypeError:
            print("Je moet een getal in te geven.")
        except ValueError:
            print("Je moet een getal ingeven.")
        if type(antwoord)==int:
            match antwoord:
                case 1:
                    print("Server toevoegen gekozen.")
                    naam=input("Geef de naam van de server: ")
                    naam_servers.append(naam)
                    ip_adress=input("Geef het server adress: ")
                    Servers.append(ip_adress)
                case 2:
                    print("Server Verwijderen gekozen.")
                    try:
                        verwijder_naam=input("Geef de naam van de server die je wilt verwijderen: ")
                        for getal in range(len(naam_servers)):
                            if naam_servers[getal] == verwijder_naam:
                                del naam_servers[getal]
                                del Servers[getal]
                        print("server succesvol verwijdert.")
                    except:
                        print("Server staat niet in de lijst")
                case 3:
                    print("Lijst tonen gekozen.")
                    print("+---------------+-----------------------+")
                    print("|\tnaam\t|\tIP-adress\t|")
                    print("+---------------+-----------------------+")
                    for getal in range(len(Servers)):
                        print(f"|\t{naam_servers[getal]}\t{Servers[getal]}\t\t|")
                    print("+---------------+-----------------------+")
                case 4:
                    print("Pingen gekozen")
                    print("")
                    websiteping.datum_log()
                    for getal in range(len(Servers)):
                        sys.stdout.write(naam_servers[getal])
                        reactie = websiteping.ping(Servers[getal])
                        if reactie is None or "100% loss" in str(reactie):
                            sys.stdout.write("\033[31m Server is niet online\033[0m\n")
                        elif "0% loss" in str(reactie):
                            sys.stdout.write("\033[32m Server online\033[0m\n")
                        else:
                            sys.stdout.write("\033[38;5;208m Slechte verbinding\033[0m\n")
                        if "Received = 4"in reactie:
                            websiteping.geschiedenis_log(naam_servers[getal],4)
                        elif "Received = 3"in reactie:
                            websiteping.geschiedenis_log(naam_servers[getal],3)
                        elif "Received = 2"in reactie:
                            websiteping.geschiedenis_log(naam_servers[getal],2)
                        elif "Received = 1"in reactie:
                            websiteping.geschiedenis_log(naam_servers[getal],1)
                        elif "Received = 0"in reactie:
                            websiteping.geschiedenis_log(naam_servers[getal],0)
                    websiteGenerator.genereer()

                case 5:
                    print("Programma sluit.")
                case _:
                    print("Keuze bestaat niet.")
        if antwoord!=5:
            print("Selecteer een optie.")
            antwoord = input("1) Server toevoegen\n2) Server Verwijderen\n3) lijst tonen\n4) Pingen \n5) Stoppen\n>")
        
        websiteping.servers_to_log(Servers)
        websiteping.servers_naam_to_log(naam_servers)


