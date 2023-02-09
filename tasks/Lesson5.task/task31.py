'''
Učitavajte brojeve koji predstavljaju dobiveni broj bodova na ispitu. 
Za broj bodova [0,50>, ispišite "Nedovoljan!", za broj bodova [50, 
62.5> ispišite "Dovoljan!", za broj bodova [62.5, 75> ispišite "Dobar!", 
za broj bodova [75, 87.5> ispišite "Vrlo dobar!", a za broj bodova 
[87.5, 100] ispišite "Odličan!". U slučaju da je uneseni broj izvan 
raspona brojeva <0, 100>, ispišite prikladnu poruku i prekinite daljnje 
učitavanje broja bodova.

'''

Bodovi = (input("Unesi bodove:"))
Bodovi = float(Bodovi)

if Bodovi > 0 and Bodovi < 50:
    print("Nedovoljan(1)")
elif Bodovi > 50 and Bodovi < 62.5:
    print("Dovoljan(2)")
elif Bodovi > 62.75 and Bodovi < 75:
    print("Dobar(3)")
elif Bodovi > 75 and Bodovi < 87.5:
    print("Vrlo Dobar(4)")
elif Bodovi > 87.5 and Bodovi < 100:
    print("Odličan(5)")
else:
    print("Neodgovara broj bodova")