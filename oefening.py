import sys
import websiteping

naam_servers=[]
Servers=[]

try:
    websiteping.ping(sys.argv[1])
except:
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
                case 5:
                    print("Programma sluit.")
                case _:
                    print("Keuze bestaat niet.")
        if antwoord!=5:
            print("Selecteer een optie.")
            antwoord = input("1) Server toevoegen\n2) Server Verwijderen\n3) lijst tonen\n4) Pingen \n5) Stoppen\n>")


