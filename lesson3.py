# if , while , for

# Nardba if
if 5==5:
    print(5)


x = 5
if x >10:
    print("The condition is met!")
else:
    print("The condition is not met!")


x = 5
if x==1:
    print("X == 1")
elif x==2:
    print("X == 2")
elif x==5:
    print("X == 5")
else:
    print("None of the conditions are met!")

# while
x = 0

while x < 10:
    print("Hello! My name is Josip")
    x = x + 1

# Beskonačna petlja
''' while True:
    print("Hello World") '''
 

# for

for i in range(10):
    print("<for>Hello World")

#---------------
n = 55
isPri = True

for x in range(2 , n):
    if n % x == 0:
        isPri = False

if isPri == True:
    print('Number', n , 'is prime!')
else:
    print('Number', n , 'is not prime!')


#------------------

for n in range(2 , 11):
    isPri = True
    for x in range(2 , n):
        if n % x == 0:
            isPri = False

    if isPri == True:
        print('Number', n , 'is prime!')
    else:
        print('Number', n , 'is not prime!')