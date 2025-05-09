parole_sospette = {
    "shock": -2,
    "incredibile": -2, 
    "complotto": -2,
    "miracoloso": -2,
    "scandalo": -2
}

parole_affidabili = {
    "studio": 2,
    "ricerca": 2,
    "esperti": 2,
    "ufficiale": 2, 
    "verificato": 2
}

def analizza_notizia(titolo):
    punti = 0
    titolo = titolo.lower()
    

    for parola in parole_sospette:
        if parola in titolo:
            punti = punti - 2
        
    for parola in parole_affidabili:
        if parola in titolo:
            punti = punti + 2
   
    if punti < 0:
        return "FAKE NEWS"
    if punti == 0: 
        return "DUBBIA"
    return "VERA"

while True:
    notizia = input("Scrivi una notizia (o fine per terminare): ")
    if notizia == "fine":
        break
        
    risultato = analizza_notizia(notizia)
    print(f"La notizia è: {risultato}")