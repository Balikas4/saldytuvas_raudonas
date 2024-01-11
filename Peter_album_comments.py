# Sąrašas, kuriame saugosime sukurtus albumus
albums = []

# Funkcija skirta formatuoti dainos trukmę iš sekundžių į minutės:sekundės formatą
def formatted_duration(seconds):
    minutes_count = seconds // 60  
    seconds_count = seconds % 60
    return f"{minutes_count}:{seconds_count:02}"

# Funkcija sukurti naują albumą
def create_album():
    # Įvesti atlikėjo vardą
    artist = input("Įveskite atlikėją: ")
    # Įvesti albumo pavadinimą
    album_name = input("Įveskite albumo pavadinimą: ")
    # Sukurti naują albumo objektą
    new_album = {"Atlikėjas": artist, "Albumas": album_name, "Albumo dainos": {}}
    # Pridėti naują albumą prie sąrašo
    albums.append(new_album)
    # Informacija apie sėkmingai sukurtą albumą
    print(f"Albumas '{album_name}' sukurtas sėkmingai!")
    # Grąžinti naują albumo objektą
    return new_album

def choose_album():
    print("\nTurimi albumai:")
    for index, album_name in enumerate(albums, 1):  # album_list turi būti globalus sąrašas su visais albumais
        print(f"{index}. {album_name}")
    
    while True:
        try:
            choice_index = int(input("Pasirinkite albumo numerį: "))
            if 1 <= choice_index <= len(albums):
                return albums[choice_index - 1]  # Grąžiname pasirinkto albumo pavadinimą
            else:
                print("Tokio albumo nėra. Bandykite dar kartą.")
        except ValueError:
            print("Netinkamas pasirinkimas. Įveskite skaičių.")

# Funkcija pridėti dainą į albumą
def add_track(album):
    # Tikrinimas, ar pasiekta maksimali dainų skaičiaus riba
    if len(album["Albumo dainos"]) >= 15:
        print("Pasiekėte maksimalų dainų kiekį (15 dainų).")
        return album

    while True:
        try:
            # Įvesti dainos numerį albume
            track_number = int(input("Įveskite dainos numerį albume (nuo 1 iki 15): "))
            # Tikrinimas, ar numeris yra tinkamas
            if 1 <= track_number <= 15:
                break
            else:
                print("Klaida! Įveskite skaičių nuo 1 iki 15.")
        except ValueError:
            print("Klaida! Įvestas netinkamas skaičius. Bandykite dar kartą.")
    
    # Įvesti dainos pavadinimą
    title = input("Dainos pavadinimą: ")
    while True:
        try:
            # Įvesti dainos trukmę sekundėmis
            duration = int(input("Įveskite dainos trukmę sekundėmis: "))
            # Tikrinimas, ar trukmė yra teigiama
            if duration > 0:
                break
            else:
                print("Klaida! Įveskite teigiamą sveikąjį skaičių.")
        except ValueError:
            print("Klaida! Įvestas netinkamas skaičius. Bandykite dar kartą.")
    
    # Atnaujinti bendrą albumo trukmę ir tikrinti maksimalią trukmės ribą
    total_duration = sum(track['trukmė'] for track in album['Albumo dainos'].values()) + duration
    if total_duration > 3600:  # 60 minutes * 60 seconds
        print("Pasiekėte maksimalią albumo trukmę (60 minučių)")
        return album

    # Pridėti dainą į albumą
    album["Albumo dainos"][track_number] = {"Dainos pavadinimas": title, "trukmė": duration}
    # Grąžinti atnaujintą albumo objektą
    return album

# Funkcija peržiūrėti albumą
def view_album(album):
    # Atspausdinti albumo informaciją
    print(f"Atlikėjas: {album['Atlikėjas']}")
    print(f"Albumo pavadinimas: {album['Albumas']}")
    print(f"Dainų skaičius: {len(album['Albumo dainos'])}")
    # Suskaičiuoti ir atspausdinti bendrą albumo trukmę
    total_duration = sum(track['trukmė'] for track in album['Albumo dainos'].values())
    print(f"Trukmė viso: {formatted_duration(total_duration)}")

# Funkcija peržiūrėti albumo dainas
def view_tracks(album):
    # Atspausdinti dainų sąrašą su numeriais ir trukmėmis
    for track_number, track in sorted(album['Albumo dainos'].items()):
        print(f"{track_number}. {track['Dainos pavadinimas']} ({formatted_duration(track['trukmė'])})")

# Funkcija ištrinti dainą iš albumo
def delete_track(album):
    # Tikrinti, ar albumas neturi dainų
    if not album["Albumo dainos"]:
        print("Albumas neturi dainų!")
        return album

    while True:
        try:
            # Įvesti dainos numerį, kurią norima ištrinti
            track_number = int(input("Įveskite dainos numerį, kurią norite ištrinti: "))
            # Tikrinti, ar toks numeris yra albumo dainų sąraše
            if track_number in album["Albumo dainos"]:
                # Ištrinti dainą
                del album["Albumo dainos"][track_number]
                print(f"Daina nr. {track_number} ištrinta sėkmingai!")
                break
            else:
                print("Toks dainos numeris albumo sąraše nerastas.")
        except ValueError:
            print("Įvestas netinkamas skaičius. Bandykite dar kartą.")

    return album

# Pagrindinė funkcija, skirta valdyti albumus
def main_menu():
    album = {}  # Sukuriamas tuščias albumo žodynas
    while True:
        # Meniu pasirinkimai
        print("\nAlbumo valdymas")
        print("1. Sukurti albumą")
        print("2. Pasirinkti albumą")
        print("3. Pridėti dainą")
        print("4. Ištrinti dainą")
        print("5. Peržiūrėti albumą")
        print("6. Peržiūrėti dainas")
        print("7. Išeiti")
        # Vartotojo pasirinkimas
        choice = input("Pasirinkite ką norite daryti: ")

        if choice == "1":
            album = create_album()
        elif choice == "2":
            # Ši dalis dar nėra implementuota, bet čia galite pridėti funkcionalumą, kuris leistų vartotojui pasirinkti albumą iš sąrašo
            pass
        elif choice == "3":
            album = add_track(album)
        elif choice == "4":
            album = delete_track(album)
        elif choice == "5":
            view_album(album)
        elif choice == "6":
            view_tracks(album)
        elif choice == "7":
            break
        else:
            print("Neteisingas pasirinkimas. Bandykite dar kartą.")

if __name__ == "__main__":
    main_menu()