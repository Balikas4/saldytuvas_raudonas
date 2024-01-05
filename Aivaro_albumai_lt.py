albumas = []

def prideti_albuma(atlikejas, pavadinimas):
    album = {'atlikejas': atlikejas, 'pavadinimas': pavadinimas}
    albumas.append(album)
    print(f'Albumas {pavadinimas} {atlikejas} prideti. ')

def isimti_albuma(atlikejas, pavadinimas):
    for album in albumas:
        if album['atlikejas'] == atlikejas and album['pavadinimas'] == pavadinimas:
            albumas.remove(album)
            print(f"Albumas {pavadinimas} {atlikejas} pasalintas. ")
            return
        print(f"Albumas {pavadinimas} {atlikejas} nerastas")

def sarasas():
    print('Albumai kolekcijoje: ')
    for list, album in enumerate(albumas, start=1):
        print(f'{list} {album['pavadinimas']}{album['atlikejas']}')

def main():
    while True:
        print('''
              ---Pasirink ka nori daryti---
              0 = Iseiti.
              1 == Prideti.
              2 = Istrinti.
              3 = Atspausdinti albumus.
              ''')
        pasirinkimas =input(" Jusu pasirinkimas: ")
        if pasirinkimas == "0":
            break
        elif pasirinkimas == "1":
            atlikejas = input("Atlikejas: ")
            pavadinimas = input("Pavadinimas: ")
            prideti_albuma(atlikejas, pavadinimas)
        elif pasirinkimas == "2":
            atlikejas = input("Atlikejas: ")
            pavadinimas = input("Pavadinimas: ")
            isimti_albuma(atlikejas, pavadinimas)
        elif pasirinkimas == "3":
            sarasas()
        else:
            print("Blogas pasirinkimas")

main()