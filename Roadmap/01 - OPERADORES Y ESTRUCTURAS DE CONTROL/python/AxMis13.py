# Operadores aritméticos
mi_suma = 13 + 7
mi_rest = 13 - 7
mi_mult = 13 * 7
mi_divi = 13 / 7
mi_resto = 13 % 7
mi_poten = 13 ** 7
mi_floor_div = 13 // 7

print(f"""Operadores aritméticos:\n
    Números utilizados para operar: 13 y 7
    Suma: {mi_suma}
    Resta: {mi_rest}
    Multiplicación: {mi_mult}
    División: {mi_divi}
    Modulo: {mi_rest}
    Potencia: {mi_poten}
    División redondeada hacia abajo: {mi_floor_div}
""")

# Operadores lógicos
mi_var_and = True and False
mi_var_or = True or False
mi_var_not = not mi_var_and

print(f"""Operadores lógicos:\n
    Operador de conjunción (True and False): {mi_var_and}
    Operador de disyunción (True or False): {mi_var_or}
    Operador de negación (not(True and False)): {mi_var_not}
""")

# Operadores de comparación
mi_var_igual = 13 == 7
mi_var_difer = 13 != 7
mi_var_mayor = 13 > 7
mi_var_menor = 13 < 7
mi_var_mayoroigual = 13 >= 7
mi_var_menoroigual = 13 <= 7

print(f"""Operadores de comparación:\n
    Números utilizados para operar: 13 y 7
    Operador de igualdad: {mi_var_igual}
    Operador de diferencia: {mi_var_difer}
    Operador mayor que: {mi_var_mayor}
    Operador menor que: {mi_var_menor}
    Operador mayor o igual: {mi_var_mayoroigual}
    Operador menor o igual: {mi_var_menoroigual}
""")

# Sentencia condicional
edad = int(input("Introduce tu edad: "))

if edad <= 0:
    print("No puedes utilizar una pc con 0 años, es ¡IMPOSIBLE!")
elif edad >= 1 and edad < 7:
    print("¡Imposible que tengas esa edad y puedas entender esto!")
elif edad >= 7 and edad <= 10:
    print("Eres una personita con mucha curiosidad.")
elif edad > 10 and edad < 18:
    print("Aprovecha bien este tiempo, sé lo que te digo")
elif edad >= 18 and edad < 30:
    print("¡Momento de aprender sobre la vida de adultos!\nTe deseo suerte ;D")
elif edad >= 30 and edad <= 65:
    print("Has progresado mucho a lo largo del tiempo, pronto podrás relajarte :)")
elif edad > 65 and edad < 100:
    print("Relajate y disfruta el tiempo que pasa")
elif edad >= 100 and edad < 110:
    print("¡Has visto muchas cosas en esta vida!")
else:
    print("¡Díme el secreto para vivir tantos años!")

# Sentencias iterativas

opcion = "si"
while opcion == "si":
    numero = int(input("\nIngresa un número: "))

    for i in range(1, 11):
        print(f"{numero} * {i} = {numero * i}")
    else:
        print("Aquí tienes los primeros 10 múltiplos, disfrútalos :D\n")

    opcion = input("¿Quieres ingresar otro número? (si, no): ")
else:
    print("\n¡Puedes continuar! :)\n")

# Sentencia de excepción
dividendo = int(input("Ingresa un número: "))
divisor = int(input("Ingresa otro número: "))
try:
    print(f"\n{dividendo} / {divisor} = {dividendo / divisor}\n")
except Exception as error:
    print("¡Ha ocurrido un error!")
    print(f"{error}\n")

# Ejercicio opcional
count = 0
for num in range(10, 56):
    if num is 16:
        continue
    elif num % 3 == 0:
        continue
    else:
        if count == 10:
            print("")
            count = 0

        print(num, end=" ")
        count += 1
        