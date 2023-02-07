'''
U varijablu r spremite neki broj koji predstavlja radijus kugle. Ako je 
radijus ispravno upisan (radijus ne može biti negativan), ispišite 
radijus i volumen kugle, 𝑉 =
4
3
× 𝑟
3 × 𝜋. Inače, ispišite poruku da je 
vrijednost u varijabli r neispravna.

'''

r = 6.3

if r > 0:
    v = 3/4 * r**3 * 3.1415
    print("Radijus je:", r)
    print("Volumen je:" , v)
else:
    print("Vrijednost u varijabli je neispravan")