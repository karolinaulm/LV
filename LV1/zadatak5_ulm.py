try:
    fhand = open("song.txt")
    rijeci_dict = {}
    
    for line in fhand:
        line = line.rstrip()
        rijeci = line.split()  
        
        for rijec in rijeci:
            rijec = rijec.lower()
            
            if rijec in rijeci_dict:
                rijeci_dict[rijec] += 1
            else:
                rijeci_dict[rijec] = 1
    
    fhand.close()
  
    jedinstvene = []
    for rijec, broj in rijeci_dict.items():
        if broj == 1:
            jedinstvene.append(rijec)
    
    print(f"Ukupno različitih riječi: {len(rijeci_dict)}")
    print(f"Riječi koje se pojavljuju samo jednom: {len(jedinstvene)}")
    print("Liste riječi:")
    for rijec in jedinstvene:
        print(f"  {rijec}")
        
except FileNotFoundError:
    print("Datoteka 'song.txt' nije pronađena!")
