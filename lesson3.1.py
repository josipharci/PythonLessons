# NAREDBA break i continue

# Break
for n in range(2,11):
    isPri = True
    for x in range(2 , n):
        if n % x == 0:
            isPri = False
            break
        if isPri == True:
            print('Number', n , 'is prime!')
        else:
            print('Number', n , 'is not prime!')

# Continue
for num in range(2,6):
    if num % 2 == 0:
        print("Even number:", num)
        continue
    print("Odd number:", num)