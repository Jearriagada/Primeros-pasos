# Desafío 1 Jean Arriagada 

#Funcion con prints del menu
def menu():
    print("Ingrese una opcion: ")
    print("1.- Secuencia de fibbonacci")
    print("2.- Triangulo numerico")
    print("3.- Piramide de estrellas")
    print("0.- Salir del programa")

#funcion que calcula la secuencia de fibonacci
def fib(n):
    if n< 2:
        return n
    else:
        return fib (n-1) + fib (n-2)

#funcion para imprimir la secuencia de fibonacci
def secuenciaFibonacci():
    num = int(input("Ingrese el rango a imprimir de Fibonacci: "))
    for x in range(num):
        print(fib(x))

#funcion para imprimir el triangulo numerico
def trianguloNumerico():
    num = int(input("Ingrese la altura del triangulo numerico: "))
    for x in range(num+1):
        for i in range(x):
            print(str(i+1)+" ",end="")
        print("\n")

#Funcion para imprimir la piramide de estrellas
def PiramideEstrellas():
    num = int(input("Ingrese la altura de la piramide de estrellas: "))
    t = num
    for h in range(num+1):
        for x in range(t+1):
            print("  ",end="")
        t = t-1 
        for z in range(2*h-1):
            print("*",end=" ")
        print("\n")

#Funcion main que llama a las demas funciones del menu
def main():
    continuar = True
    while continuar:
        menu()
        opcion = input("Opcion: ")
        if opcion == "1":
            secuenciaFibonacci()
        elif opcion == "2":
            trianguloNumerico()
        elif opcion == "3":
            PiramideEstrellas()
        elif opcion == "0":
            print("Programa terminado")
            continuar=False
            
if __name__ == "__main__":
    main()