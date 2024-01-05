def main():
    album = {
        "Artist": "Snoop Dogg",
        "Album name": "Doggystyle",
        "Year": 1993,
        "Tracks": [
            ("Bathtub", 111),
            ("G Funk Intro", 145),
            ("Gin And Juice", 211),
            ("W Balls", 37),
            ("Tha Shiznit", 244),
            ("Untitled", 37),
            ("Lodi Dodi", 264),
            ("Murder Was The Case (Death After Visualizing Eternity)", 218)
        ]
    }
    while True:
        print('''
              ----XD---- Main Album Menu ----XD----
                exit = Exit.
                album = Prints Album info.
                tracklist = Prints Tracklist info.
                edit album = Album edit menu.
                edit tracklist = Tracklist edit menu.
                duration = Prints total duration of this album.
                XD = secret
              ''')
        choice = input("Your choice: ")
        if choice.startswith("exit"):
            break
        elif choice.startswith("edit album"):
            edit_album(album)
        elif choice.startswith("edit tracklist"):
            edit_tracklist(album)
        elif choice.startswith("album"):
            print_album(album)
        elif choice.startswith("tracklist"):
            print_tracklist(album)
        elif choice.startswith("duration"):
            total_duration(album)
        elif choice.startswith("XD"):
            XD()
        else:
            print("Bad choice, try again")


def print_album(album):
    for key, value in album.items():
        print(f"{key} - {value}")


def print_tracklist(album):
    print("---TRACKLIST INFO---")
    for index, track_info in enumerate(album["Tracks"], start=1):
        track_name, track_duration = track_info
        print(f"{index}. {track_name} - {format_duration(track_duration)}")


def edit_album(album):
    while True:
        print("""
            ----Album edit menu----
            1. Edit artist name.
            2. Edit album name.
            3. Edit album year.
            4. Tracklist edit menu.
            0. Back
            album = Prints Album info.
            exit = Exits program.
            """)
        choice = input("Your choice: ")
        if choice.startswith("0"):
            break
        elif choice.startswith("exit"):
            quit()
        elif choice.startswith("album"):
            print_album(album)
        elif choice.startswith("1"):
            new_artist_name = input("Input new artist name: ")
            album["Artist"] = new_artist_name
        elif choice.startswith("2"):
            new_album_name = input("Input new album name: ")
            album["Album name"] = new_album_name
        elif choice.startswith("3"):
            new_album_year = int(input("Input new album year: "))
            album["Year"] = new_album_year
        elif choice.startswith("4"):
            edit_tracklist(album)
        else:
            print("Wrong choice")


def edit_tracklist(album):
    while True:
        print("""
            ----Tracklist edit menu----
            0. Back
            1. Edit track name.
            2. Edit track duration.
            3. Add new track.
            4. Album edit menu.
            5. Remove track.
            exit = Exits program
            tracklist = Prints Tracklist info.
            album = Prints Album info.
            """)
        choice = input("Your choice: ")
        if choice.startswith("0"):
            break
        elif choice.startswith("exit"):
            quit()
        elif choice.startswith("tracklist"):
            print_tracklist(album)
        elif choice.startswith("album"):
            print_album(album)           
        elif choice.startswith("1"):
            print_tracklist(album)
            chose_track = int(input("Chose track number to edit: "))
            new_track_name = input("Input new track name: ")
            album["Tracks"][chose_track-1] = (new_track_name, album["Tracks"][chose_track-1][1])
        elif choice.startswith("2"):
            print_tracklist(album)
            chose_track = int(input("Chose track number to edit: "))
            new_track_duration = input("Input new duration (MM:SS): ")
            album["Tracks"][chose_track-1] = (album["Tracks"][chose_track-1][0], parse_duration(new_track_duration))
        elif choice.startswith("3"):
            print_tracklist(album)
            track_info = input("Input new track name, duration (MM:SS): ") 
            album["Tracks"].append(parse_track_info(track_info))
        elif choice.startswith("4"):
            edit_album(album)
        elif choice.startswith("5"):
            print_tracklist(album)
            del_choice = int(input("Choose track to delete: "))
            if 1 <= del_choice <= len(album["Tracks"]):
                del album["Tracks"][del_choice - 1]
                break
            else:
                print("Invalid track number. Please choose a valid track next time.")
                break
        else:
            print("Wrong choice")

def format_duration(seconds):
    seconds_left = seconds % 60
    minutes = seconds // 60
    return f"{minutes:02}:{seconds_left:02}"

def parse_duration(track_duration):
    if isinstance(track_duration, str):
        parts = track_duration.split(":")
        minutes = int(parts[0])
        seconds = int(parts[1])
        return minutes * 60 + seconds
    elif isinstance(track_duration, int):
        return track_duration
    else:
        raise ValueError("Invalid track duration format")


def parse_track_info(track_info):
    parts = track_info.split(", ")
    track_name = parts[0]
    duration_parts = parts[1].split(":")
    minutes = int(duration_parts[0])
    seconds = int(duration_parts[1])
    track_duration = minutes * 60 + seconds
    return track_name, track_duration


def total_duration(album):
    album_duration = 0
    for track_info in album["Tracks"]:
        album_duration += track_info[1]
    print("Total album duration in seconds: ", album_duration)
    print("Totel album duration in (MM:SS) format:", format_duration(album_duration))


def XD():
    print("""
                                                -----
                                              /      \\
                                              )      |
       :================:                      "    )/
      /||              ||                      )_ /*
     / ||    System    ||                          *
    |  ||     Down     ||                   (=====~*~======)
     \ ||press any key ||                  0      \ /       0
       ==================                //   (====*====)   ||
........... /      \.............       //         *         ||
:\        ############            \    ||    (=====*======)  ||
: ---------------------------------     V          *          V
: |  *   |__________|| ::::::::::  |    o   (======*=======) o
\ |      |          ||   .......   |    \\         *         ||
  --------------------------------- 8   ||   (=====*======)  //
                                     8   V         *         V
  --------------------------------- 8   =|=;  (==/ * \==)   =|=
  \   ###########################  \   / ! \     _ * __    / | \\
   \  +++++++++++++++++++++++++++   \  ! !  !  (__/ \__)  !  !  !
    \ ++++++++++++++++++++++++++++   \        0 \ \V/ / 0
     \________________________________\     ()   \o o/   ()
      *********************************     ()           ()
          """)
    input("Say anything if you have anything left to say: ")


if __name__ == "__main__":
    main()

""" Komandinio/individualaus darbo užduotis
===[ Muzikos Albumas ]===

Reikalavimai:

* Žodynas albumas turi turėti atlikėją ir pavadinimą, gali turėti ir kitų atributų
* Albumo žodyne sukurkite takelių (dainų) sąrašą, kur kiekvienas takelis yra žodynas, talpinantis eilės numerį, pavadinimą ir trukmę sekundėmis. 
** Bonus: trukmės įvedimas "minutės:sekundės" formatu (žmogui suprantamu).
* Programa turi leisti vartotojui užpildyti/pakeisti albumo informaciją (pavadinimą, atlikėją, ...)
* Programa turi leisti vartotojui sukurti/ištrinti takelį, užpildant takelio informaciją (pavadinimą, trukmę)
* Galimybė peržiūrėti albumą, išspausdinant takelių kiekį ir bendrą jų trukmę šalia kitų atributų.
* Peržiūrėti albumo dainas. Bonus: išrūšiuotas pagal eilės numerį. Takelio trukmė turi būti pateikta žmogui suprantama laiko išraiška.

Pastabos:
* Stenkitės nekartoti kodo - funkcionalumui, kuriam kodas kartotųsi, parašykite atskiras funkcijas ir jas panaudokite kelis kartus kur reikia.
"""
