def formatted_duration(seconds):
    minutes_length = seconds // 60  
    seconds_length = seconds % 60
    return f"{minutes_length}:{seconds_length:02}"

def choose_album(album_list):
    print("\nGalimi albumai:")
    for number, album in enumerate(album_list, 1):
        print(f"{number}. {album['Albumas']}")
    try:
        choice = int(input("Pasirinkite albumo numerį: "))
        if 1 <= choice <= len(album_list):
            return album_list[choice - 1]["Albumas"]
        else:
            print("Neteisingas albumo numeris. Bandykite dar kartą.")
            return None
    except ValueError:
        print("Neteisingas pasirinkimas. Bandykite dar kartą.")
        return None

def create_album():
    artist = input("Įveskite atlikėją: ")
    album_name = input("Įveskite albumo pavadinimą: ")
    return {"Atlikėjas": artist, "Albumas": album_name, "Albumo dainos": {}}

def add_track(album_list):
    if not album_list:
        print("Nėra sukurto jokio albumo!")
        return album_list

    album_name = choose_album(album_list)
    if not album_name:
        return album_list

    for album in album_list:
        if album["Albumas"] == album_name:
            break

    if len(album["Albumo dainos"]) >= 15:
        print("Pasiekėte maksimalų dainų kiekį (15 dainų).")
        return album_list

    while True:
        try:
            track_number = int(input("Įveskite dainos numerį albume (nuo 1 iki 15): "))
            if 1 <= track_number <= 15:
                break
            else:
                print("Klaida! Įveskite skaičių nuo 1 iki 15.")
        except ValueError:
            print("Klaida! Įvestas netinkamas skaičius. Bandykite dar kartą.")

    title = input("Dainos pavadinimą: ")

    existing_track = None
    for album in album_list:
        if album["Albumas"] == album_name and track_number in album["Albumo dainos"]:
            existing_track = album["Albumo dainos"][track_number]
            break

    if existing_track:
        print(f"Daina su numeriu {track_number} ir pavadinimu '{existing_track['Dainos pavadinimas']}' jau egzistuoja.")
        change_or_delete = input("Norite pakeisti šios dainos numerį (P) arba ištrinti ją (I)? (P/I): ").upper()
        if change_or_delete == "I":
            del album["Albumo dainos"][track_number]
            print(f"Daina su numeriu {track_number} ištrinta.")
        else:
            print("Pakeiskite dainos numerį.")
            # Grąžiname, kad vartotojas galėtų įvesti naują dainos numerį
            return album_list
        
    while True:
        try:
            duration = int(input("Įveskite dainos trukmę sekundėmis: "))
            if duration > 0:
                break
            else:
                print("Klaida! Įveskite teigiamą sveikąjį skaičių.")
        except ValueError:
            print("Klaida! Įvestas netinkamas skaičius. Bandykite dar kartą.")
    
    total_duration = sum(track['trukmė'] for track in album['Albumo dainos'].values()) + duration
    if total_duration > 3600:  # 60 minutes * 60 seconds
        print("Pasiekėte maksimalią albumo trukmę (60 minučių)")
        return album_list

    album["Albumo dainos"][track_number] = {"Dainos pavadinimas": title, "trukmė": duration}

def delete_track(album_list):
    if not album_list:
        print("Nėra sukurto jokio albumo!")
        return album_list

    album_name = choose_album(album_list)
    if not album_name:
        return album_list

    for album in album_list:
        if album["Albumas"] == album_name:
            break

    if not album["Albumo dainos"]:
        print("Albumas neturi dainų, kurias galima ištrinti.")
        return album_list

    while True:
        try:
            track_number = int(input("Įveskite dainos numerį, kurią norite ištrinti: "))
            if track_number in album["Albumo dainos"]:
                break
            else:
                print("Daina su tokiu numeriu neegzistuoja. Bandykite dar kartą.")
        except ValueError:
            print("Klaida! Įvestas netinkamas skaičius. Bandykite dar kartą.")

    del album["Albumo dainos"][track_number]
    print(f"Daina su numeriu {track_number} ištrinta sėkmingai.")
    return album_list

def view_album(album_list):
    if not album_list:
        print("Nėra sukurto jokio albumo!")
        return

    album_name = choose_album(album_list)
    if not album_name:
        return

    for album in album_list:
        if album["Albumas"] == album_name:
            print(f"Atlikėjas: {album['Atlikėjas']}")
            print(f"Albumo pavadinimas: {album['Albumas']}")
            print(f"Dainų skaičius: {len(album['Albumo dainos'])}")
            total_duration = sum(track['trukmė'] for track in album['Albumo dainos'].values())
            print(f"Trukmė viso: {formatted_duration(total_duration)}")
            break

def view_tracks(album_list):
    if not album_list:
        print("Nėra sukurto jokio albumo!")
        return album_list

    album_name = choose_album(album_list)
    if not album_name:
        return album_list

    for album in album_list:
        if album["Albumas"] == album_name:
            for track_number, track in sorted(album['Albumo dainos'].items()):
                print(f"{track_number}. {track['Dainos pavadinimas']} ({formatted_duration(track['trukmė'])})")
            break
    else:
        print(f"Albumas {album_name} nerastas!")  # Pridėkite šią eilutę
    return album_list

def main_menu():
    album_list = []
    while True:
        print("\nAlbumo valdymas")
        print("1. Sukurti albumą")
        print("2. Pridėti dainą")
        print("3. Ištrinti dainą")
        print("4. Peržiūrėti albumą")
        print("5. Peržiūrėti dainas")
        print("0. Išeiti")
        choice = input("Pasirinkite ką norite daryti: ")

        if choice == "1":
            album_list.append(create_album())
        elif choice == "2":
            album_list = add_track(album_list)
        elif choice == "3":
            album_list = delete_track(album_list)
        elif choice == "4":
            album_list = view_album(album_list)
        elif choice == "5":
            album_list = view_tracks(album_list)
        elif choice == "0":
            break
        else:
            print("Neteisingas pasirinkimas. Bandykite dar kartą.")

if __name__ == "__main__":
    main_menu()