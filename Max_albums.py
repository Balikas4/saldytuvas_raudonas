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
def add_track(album_dictionary, queue_number, title, duration):
    track_dictionary = {}
    track_dictionary["Eilė"] = queue_number
    track_dictionary["Trackas"] = title
    track_dictionary["Trukmė"] = duration
    list(album_dictionary["Takeliai"]).append(track_dictionary)
    return album_dictionary

def remove_track(album_dictionary, queue_number):
    list(album_dictionary["Takeliai"]).remove(queue_number)
    return album_dictionary

def print_general_info(album_dictionary):
    print(f"General info:\nArtist: {album_dictionary['Atlikėjas']}\nAlbum: {album_dictionary['Albumas']}\nTracks count: {list(album_dictionary['Takeliai']).count}")
    total_duration = 0
    for  track_info in list(album_dictionary['Takeliai']):
        total_duration += track_info['Trukmė']
    print(f"\n Total duration:{total_duration}")

def print_all_tracks(album_dictionary):   
    list(album_dictionary['Takeliai']).sort 
    for  track_info in list(album_dictionary['Takeliai']):
        print(f"Queue number: {track_info['Eilė']} Track title: {track_info['Trackas']} Track duration: {track_info['Trukmė']}")


def main():    
    albums={"Atlikėjas":"Atlikejo pavadinimas", "Albumas":"Albumo pavadinimas", "Takeliai":[{"Eilė":1, "Trackas":"tracko pavadinimas", "Trukmė":5}]}

    while True:
        print('''
              ----Choose what you want to do with your album----
                0 = Exit.
                1 = Modify album information.
                2 = Create track.
                3 = Remove track.
                4 = See album general info(amount of tracks, total duration)
                5 = See all tracks info
              ''')
        choice = input("Your choice: ")
        if choice.startswith("0"):
            break
        elif choice.startswith("1"):
            albums["Atlikėjas"]=input("Enter artist name")
            albums["Albumas"]=input("Enter album title")
            pass
        elif choice.startswith("2"):
            track_number = list(albums["Takeliai"]).count+1
            track_title = input("Enter track title")
            track_duration = int(input("Enter track duration"))
            albums = add_track(albums, track_number, track_title, track_duration)            
        elif choice.startswith("3"):
            index = int(input("Enter track number/index"))
            albums = remove_track(albums, index)            
        elif choice.startswith("4"):
            print_general_info(albums)            
        elif choice.startswith("5"):
            print_all_tracks(albums)
        else:
            print("Bad choice, try again")

main()