#!/usr/bin/env python3

def mostrar_menu():
    print("\n=== Conversor de Unidades ===\n")
    print("\n1. Kilogramos a gramos")
    print("\n2. Gramos a kilogramos")
    print("\n3. Libras a kilogramos")
    print("\n4. Kilogramos a libras")
    print("\n5. Salir")

def kg_a_gramos():
    while True:
        try:
            numero = input("\nEscribe el número de kilogramos para convertir a gramos: ")
            numero_limpio = numero.replace(",", "")
            numero = float(numero_limpio)
            break
        except ValueError:
            print("\n[!] Por favor, escriba una cifra.")

    gramos = numero * 1000
    print(f"\nEquivale a: {gramos:,.2f} Gramos.")

def gramos_a_kg():
    while True:
        try:
            numero = input("\nEscribe el número de gramos para convertir a kilogramos: ")
            numero_limpio = numero.replace(",", "")
            numero = float(numero_limpio)
            break
        except ValueError:
            print("\n[!] Por favor, escriba una cifra.")

    kilogramos = numero / 1000
    print(f"\nEquivale a: {kilogramos:,.2f} kilogramos.")

def libras_a_kg():
    while True:
        try:
            numero = input("\nEscribe el número de libras para convertir a kilogramos: ")
            numero_limpio = numero.replace(",", "")
            numero = float(numero_limpio)
            break
        except ValueError:
            print("\n[!] Por favor, escriba una cifra.")

    kilogramos = numero / 2.205
    print(f"\nEquivale a: {kilogramos:,.2f} kilogramos.")

def kg_a_libras():
    while True:
        try:
            numero = input("\nEscribe el número de kilogramos para convertir a libras: ")
            numero_limpio = numero.replace(",", "")
            numero = float(numero_limpio)
            break
        except ValueError:
            print("\n[!] Por favor, escriba una cifra.")

    libras = numero * 2.205
    print(f"\nEquivale a: {libras:,.2f} Libras.")

while True:
    mostrar_menu()
    opcion = input("\nElige una opción (1-5): ")

    if opcion == "1":
        kg_a_gramos()

    elif opcion == "2":
        gramos_a_kg()

    elif opcion == "3":
        libras_a_kg()

    elif opcion == "4":
        kg_a_libras()

    elif opcion == "5":
        print("\n¡Hasta luego!\n")
        break

    else:
        print("\n[!] Opción no válida. Intenta de nuevo.")
