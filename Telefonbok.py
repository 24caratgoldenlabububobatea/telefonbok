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
    
vis_alle()