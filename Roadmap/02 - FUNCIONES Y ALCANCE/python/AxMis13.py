# función sin parámetros y sin retorno
def voltear_palabra():
    cadena = input("\nIntroduce una palabra: ")
    print(f"Tu palabra volteada: {cadena[::-1]}\n")

voltear_palabra()

# función con parámetros
def es_palindromo(palabra):
    if palabra == palabra[::-1]:
        print(f"{palabra} es palíndromo")
    else:
        print(f"{palabra} no es palíndromo")

es_palindromo("Palabra")
es_palindromo("ana")

# función con parámetros y retorno
def factorial(numero):
    if numero == 1:
        return numero
    else:
        return numero * factorial(numero - 1)
    
numero = int(input("\nIntroduce un número: "))
resultado = factorial(numero)
print(f"El factorial de {numero} es: {resultado}")

# crear una función dentro de otra, aplicando el concepto de variable local y global
# y utilizando una función propia del lenguaje
def funcion_super():
    limite = int(input("\nIntroduce un número: "))    # aquí limite es local
    
    def funcion_inter():
        count = 0
        for num in range(2, limite, 2): # se puede acceder a limite ya que la función está anidada, pero no se puede modificar
            if count == 10:
                print("")
                count = 0
            
            print(num, end=" ")
            count += 1
        
        print(f"\nValor de la varible global: {numero}")   # numero es una variable global declarada anteriormente
        print(f"Valor de límite: {limite}")
        return 1
    
    valor_devuelto = funcion_inter()

    if valor_devuelto:
        print(f"Se han impreso todos los múltiplos de 2 hasta el límite introducido")

funcion_super()

def funcion_super():
    limite = int(input("\nIntroduce un número: "))    # aquí limite es local, diferente a la función anterior
    
    def funcion_inter():
        nonlocal limite # con nonlocal se puede modificar la variable
        count = 0
        for num in range(2, limite, 2): # range() es una función propia del lenguaje
            if count == 10:
                print("")
                count = 0
            
            print(num, end=" ")
            count += 1
        
        numero = 2  # numero sige siendo global y se puede modificar
        print(f"\nValor modificado de la varible global: {numero}")
        limite = 1  # aquí se modifica limite
        print(f"Valor modificado de límite: {limite}")
        return 1
    
    valor_devuelto = funcion_inter()

    if valor_devuelto:
        print(f"Se han impreso todos los múltiplos de 2 hasta el límite introducido\n")

funcion_super()

# Ejercicio opcional
def mi_funcion(cad1, cad2):
    count = 0
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print(f"{cad1} {cad2}")
        elif num % 3 == 0:
            print(cad1)
        elif num % 5 == 0:
            print(cad2)
        else:
            print(num)
            count += 1

    return count

numeros_impresos = mi_funcion("Hola", "Mundo")
print(f"\nCantidad de veces que se imprimió un número: {numeros_impresos}\n")
