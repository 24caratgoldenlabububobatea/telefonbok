#link til github repo: https://github.com/24caratgoldenlabububobatea/telefonbok
telefonbok = []

telefonbok.append({
    "person1": {
        "navn": "jonathan",
        "nummer": "48128944"
    }
})

telefonbok.append({
    "person2": {
        'navn': 'bob',
        "nummer": 48104755
    }
})

def vis_alle():
    for person in telefonbok:
        for key, info in person.items():
            print(f"{info['navn']}: {info['nummer']}.") #omg dette tok så lang tiddddd TᴖT
    
def legg_til():
    navn = input("Hva er ditt navn?: ")
    nummer = input("Hva er ditt nummer?: ")

    for person in telefonbok:
        info = next(iter(person.values()))
        if info['navn'].lower() == navn.lower():
            info['nummer'] = nummer
            print(f"{navn} finnes allerede i telefonboken. Nummer oppdatert.")
            return

    x = 3
    while any(f"person{x}" in p for p in telefonbok):
        x += 1
    
    telefonbok.append({
        f"person{x}": {
            "navn": navn,
            "nummer": nummer
        }
    })
    print(f"{navn} ble lagt til i telefonboka.")


def søk():
    navn_søk = input("Skriv navnet på personen du søker etter: ").lower()

    for person in telefonbok:
        info = next(iter(person.values()))
        if info['navn'].lower() == navn_søk:
            print(f"{info['navn']} finnes i telefonboken med nummer: {info['nummer']}")
            return 

    print(f"{navn_søk} finnes ikke i telefonboken.")

def main_menu():
    while True:
        print("\n--- Hovedmeny ---")
        print("1. Søk i telefonbok")
        print("2. Vis alle i telefonbok")
        print("3. Legg til ny person")
        print("4. Avslutt programmet")
        valg = input("Velg et alternativ (1-4): ").lower()

        if valg == "1":
            søk()
        elif valg == "2":
            vis_alle()
        elif valg == "3":
            legg_til()
        elif valg == "4" or valg == "avslutt":
            print("Programmet avsluttes.")
            break
        else:
            print("Ugyldig valg, prøv igjen.")


main_menu()#Yipe!!!!!:P

        