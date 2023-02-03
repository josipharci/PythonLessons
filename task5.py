#Kreirajte dvije brojčane varijable te uz pomoć skraćenih aritmetičkih 
#operatora (zbrajanje, oduzimanje, množenje, dijeljenje, ostatak 
#dijeljenja, potenciranje, cjelobrojno dijeljenje) ispišite rezultate.
#Napomena: nakon svakog korištenja skraćenog aritmetičkog 
#operatora potrebno je varijablu čija se vrijednost mijenja postaviti na 
#početnu vrijednost

num1 = int(input("Number1:"))
num2 = int(input("Number2:"))

num1+=num2
print('num1+=num2 =', num1)

num1-=num2
print('num1-=num2 =', num1)

num1*=num2
print('num1*=num2 =', num1)

num1/=num2
print('num1/=num2 =', num1)

num1%=num2
print('num1%=num2 =', num1)

num1**=num2
print('num1**=num2 =', num1)

num1//=num2
print('num1//=num2 =', num1)

num1=num2
print('num1=num2 =', num1)