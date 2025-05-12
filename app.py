parole_sospette = {
    "shock": -4,
    "incredibile": -2, 
    "complotto": -4,
    "miracoloso": -2,
    "scandalo": -2,
    "segreto": -3,
    "allarme": -2,
    "terribile": -3,
    "cospirazione": -4,
    "pericolo": -2
}

parole_affidabili = {
    "studio": 2,
    "ricerca": 2,
    "esperti": 3,
    "ufficiale": 2, 
    "verificato": 4,
    "scientifico": 3,
    "analisi": 2,
    "conferma": 2,
    "documento": 2,
    "fonte": 3
}

while True:
    notizia = input("Scrivi una notizia (o fine per terminare): ")
    if notizia == "fine":
        break
    
    punti = 0
    notizia = notizia.lower()
    
    for parola in parole_sospette:
        if parola in notizia:
            punti = punti - 2
            
    for parola in parole_affidabili:
        if parola in notizia:
            punti = punti + 2
            
    if punti < 0:
        print("La notizia è: FAKE NEWS")
    elif punti == 0:
        print("La notizia è: DUBBIA")
    elif punti > 0:
        print("La notizia è: VERA")