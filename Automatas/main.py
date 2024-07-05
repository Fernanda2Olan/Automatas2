import buscador
import aceptacionCaracteres

cadena_usuario = input ("Ingrese una cadena de texto: ")

if aceptacionCaracteres.validar(cadena_usuario):
    for componente in cadena_usuario.split():
        print((f"\t Buscando la palabra {componente}"))
    buscador.find_sustantivos(componente)