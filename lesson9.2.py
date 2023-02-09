# N-terac

nTerac = ('a' , 'bcd' , 123)
nTerac2 = ('a' , 'bcd' , 123 , 55)
print(nTerac)

#Dohvačanje vrijedonsti

print(nTerac[2])
print(nTerac2[0:3])

nTerac3 = (11 , 22 ,33)
var1,var2,var3 = nTerac3

print(var1 ,var2 ,var3)


#N-terac je nepromjeniv
'''
nTerac4 = (11,22,33)
nTerac4[0]= 0

print(nTerac4)

'''

nTerac5 = (11,22,33)
del nTerac5
print("N-terac nakon brisanja:")
print(nTerac5)