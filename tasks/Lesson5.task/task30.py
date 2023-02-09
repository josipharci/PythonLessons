'''
Napišite program koji s tipkovnice učitava tri cijela broja: redni broj 
dana u mjesecu, redni broj mjeseca u godini i redni broj godine. 
Prekontrolirajte jesu li učitane vrijednosti ispravne (ispravne 
vrijednosti su: dan - [1, 31], mjesec - [1, 12], godina - [0, 2020]). Za 
ulazne podatke 19, 2, 2017, ispišite datum u sljedećem formatu:
19. veljače, 2017

'''

Day = int(input("Day:"))
Month=int(input("Month:"))
Years=int(input("Years:"))

if Day < 0 or Day > 31 or Month < 0 or Month > 12 or Years > 2020 or Years < 0:
    print("Error")
else:
     if Month == 1:
        Mon = "Sječanja"
     elif Month == 2:
        Mon = "Veljače"
     elif Month == 3:
        Mon = "Ožuljaka"
     elif Month == 4:
        Mon = "Travanja"
     elif Month == 5:
        Mon = "Svibanja"
     elif Month == 6:
        Mon = "Lipanja"
     elif Month == 7: 
        Mon = "Srpnja"
     elif Month == 8:
        Mon = "Kolovoza"
     elif Month == 9:   
        Mon = "Rujna"
     elif Month == 10: 
        Mon = "Listopada"
     elif Month == 11:
        Mon = "Studenog"
     elif Month == 12:   
        Mon = "Prosinca"
     else:
        print("Greška u formatu:")
    
print(Day,"." ,Mon,",", Years,"." , sep="")