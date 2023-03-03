#fibonacci denerator

def  fibonacci(n):
	if n == 1  or n == 0:

		return n;

	else:

		return fibonacci(n-2) + fibonacci(n - 1)


numero = int(input("ingrese un numero entero  positivo: "))

if numero < 0:
	print("Numero no valido")

i = 0

print("Secesion de fibonacci: ")

for i in range(0, numero):
	print(fibonacci(i))
