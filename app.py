print("Hello World!")

#Drawnig a shape
 
print("    /| ")
print("   / | ")
print("  /  | ")
print(" /   | ")
print("/____| ")

#Variable & Data Types

character_name = "Josip Harci"
character_age = "23"
character_like="programming"
character_learning="python"

print("I am " + character_name + ".")
print("I am " + character_age + " years old. ")
print("I like " + character_like +  ".")
print("I'm learning " + character_learning + ".")

#Osnove

print("Osijek\nAcademy")

phrase="Osije Academy"
print(phrase)
print(phrase + " is cool ")
print(phrase.upper())
print(phrase.isupper()) #False
print(phrase.upper().isupper()) #True
print(len(phrase)) #13
print(phrase[0]) # O

name= input("what is your name?")
print(" Hello " + name)

birht_year = input("Enter your birth year:")
age= 2022 - int(birht_year)
print(age)