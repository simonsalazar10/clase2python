nivelAgua=int(input("Cual es el nivel del agua?: "))

#evaluando multiples condiciones
if nivelAgua>0 and nivelAgua<=200:
    print(f"El nivel del agua es: {nivelAgua}, esta muy bajo")
elif nivelAgua>200 and nivelAgua<=400:
    print(f"el nivel del agua es: {nivelAgua}, estamos opperando con normalidad")
elif nivelAgua>400:
    print(f"el nivel del agua es: {nivelAgua}, inicie el progama de evacuacion...")
else:
    print("por favor revisar el nivel del agua")