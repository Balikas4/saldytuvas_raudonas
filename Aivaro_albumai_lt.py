albumas = []

def prideti_albuma(atlikejas, albumas):
    album = {'atlikejas': atlikejas, 'albumas': albumas}
    albumas.append(album)
    print(f'Albumas {atlikejas} {albumas} prideti. ')

def isimti_albuma(atlikejas_param, albumas_param):
    for a in albumas:
        if a['atlikejas'] == atlikejas_param and a['albumas'] == albumas_param:
            albumas.remove(a)
            print(f"Albumas {atlikejas_param} - {albumas} pasalintas. ")
            return
    print(f"Albumas {atlikejas_param} {albumas_param} nerastas")

def sarasas():
    print('Albumai kolekcijoje: ')
    for list, album in enumerate(albumas, start=1):
        print(f"{list} {album['atlikejas']} {album['albumas']}")

def main():
    while True:
        print('''
              ---Pasirink ka nori daryti---
              0 = Iseiti.
              1 = Prideti diska i kolekcija.
              2 = Istrinti diska is kolekcijos.
              3 = Atspausdinti albumus.
              ''')
        pasirinkimas = input(" Jusu pasirinkimas: ")
        if pasirinkimas == "0":
            break
        elif pasirinkimas == "1":
            atlikejas = input("Atlikejas: ")
            albumas_pavadinimas = input("Albumo pavadinimas: ")
            prideti_albuma(atlikejas, albumas_pavadinimas)
        elif pasirinkimas == "2":
            atlikejas = input("Atlikejas: ")
            albumas_pavadinimas = input("Albumo pavadinimas: ")
            isimti_albuma(atlikejas, albumas_pavadinimas)
        elif pasirinkimas == "3":
            sarasas()
        else:
            print("Neteisingas pasirinkimas")

main()

