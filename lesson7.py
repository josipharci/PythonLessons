#Datoteke

f = open('E:\GithubRepozitori\PythonLessons\datoteka.txt' , "w")

#f.close()

with open('E:\GithubRepozitori\PythonLessons\datoteka.txt') as f:
    fullFile = f.read()
    print(fullFile)
    fullFile = f.read()
    print(fullFile)
