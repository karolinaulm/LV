brojevi=[]

while True:
    unos=input("Unesi broj ili 'Done':")

    if unos=="Done":
        break
    try:
        broj=float(unos)
        brojevi.append(broj)
    except ValueError:
        print("Greška!")

print("Korisnik je unio ",len(brojevi), "brojeva")
print("Srednja vrijednost brojeva je:", sum(brojevi)/len(brojevi))
print("Minimalna vrijednost brojeva je:",min(brojevi))
print("Maksimalna vrijednost brojeva je:",max(brojevi))    

brojevi.sort()
print(brojevi)
