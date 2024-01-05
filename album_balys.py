def main():
    album = {
        "Artist":"Snoop Dogg",
        "Album name":"Doggystyle",
        "Year": 1993,
        "Tracks": []
        }
    while True:
        print('''
              ----XD---- Main Album Menu ----XD----
                exit = Exit.
                album = Prints Album info.
                tracklist = Prints Tracklist info.
                edit album = Album edit menu.
                edit tracklist = Tracklist edit menu.
                XD = secret
              ''')
        choice = input("Your choice: ")
        if choice.startswith("exit"):
            break                                       #Turbut galima naudoti ir quit()
        elif choice.startswith("edit album"):
            edit_album(album)
        elif choice.startswith("edit tracklist"):
            edit_tracklist(album)
        elif choice.startswith("album"):
            print_album(album)
        elif choice.startswith("tracklist"):
            print_tracklist(album)
        elif choice.startswith("XD"):
            XD()
        else:
            print("Bad choice, try again")


def print_album(album):
    for key, value in album.items():
        print(f"{key} - {value}")


def print_tracklist(album):
    print("---TRACKLIST INFO---")
    for index, track in enumerate(album["Tracks"], start=1):
        print(f"{index}. {track['track name']} - {track['track duration']} seconds")


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
            chose_track = int(input("Chose track number to edit"))
            new_track_name = input("Input new track name: ")
            album["Tracks"][chose_track - 1]["track name"] = new_track_name
        elif choice.startswith("2"):
            print_tracklist(album)
            chose_track = int(input("Chose track number to edit"))
            new_track_duration_s = int(input("Input new duration seconds: "))
            album["Tracks"][chose_track-1]["track duration"] = new_track_duration_s        
        elif choice.startswith("3"):
            print_tracklist(album)
            new_track_name = input("Input new track name: ")    #Upgrade into 1 input
            new_track_duration_s = int(input("Input new duration seconds: "))
            new_track = {"track name": new_track_name, "track duration": new_track_duration_s}
            album["Tracks"].append(new_track)
        elif choice.startswith("4"):
            edit_album(album)
        else:
            print("Wrong choice")


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
    input("Say anything if you have anything left to say")


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
