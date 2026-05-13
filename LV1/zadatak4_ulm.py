ime_datoteke = input("Ime datoteke: ")

try:
    fhand = open(ime_datoteke)
    vrijednosti = []
    
    for line in fhand:
        line = line.rstrip() 
        
        if line.startswith("X-DSPAM-Confidence:"):
            parts = line.split(":")
            broj = float(parts[1].strip())
            vrijednosti.append(broj)
    
    fhand.close()
    
    if len(vrijednosti) > 0:
        prosjek = sum(vrijednosti) / len(vrijednosti)
        print(f"Average X-DSPAM-Confidence: {prosjek}")
    else:
        print("Nije pronađena niti jedna X-DSPAM-Confidence linija")
        
except FileNotFoundError:
    print(f"Datoteka '{ime_datoteke}' nije pronađena")
except ValueError:
    print("Greška pri pretvaranju broja")
