print('Programa sequência Fibonacci')

checkNum = int(input("Insira o numero desejado:"))

firstTerm, secondTerm = 0, 1

while firstTerm < checkNum:
    firstTerm, secondTerm = secondTerm, firstTerm + secondTerm

if firstTerm == checkNum:
    print("Está na Fibonacci")
else:
    print("Não está na Fibonacci")