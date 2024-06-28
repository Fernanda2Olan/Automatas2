#Validación de caracteres en la gramatica latina

import string

def gramaticass():
    return "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ0123456789!/,.-_'?*:;?{}[]"

def separar_por_caracteres(cadena):
    return [char for char in cadena]

def es_caracter_valido(caracter):
    return caracter in gramaticass()

cadena_usuario = input("Ingrese una cadena de texto: ")

caracteres_separados = separar_por_caracteres(cadena_usuario)
print("Cadena separada por caracteres: ", caracteres_separados)