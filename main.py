import buscador
import aceptacionCaracteres

if __name__ == '__main__':
    archivo_gramatica = open("gramatica.txt")
    if aceptacionCaracteres.valida_caracteres(archivo_gramatica):
        for linea in archivo_gramatica:
            for palabra in linea.split():
                token = buscador.find_sustantivos(palabra)
                print(f"\t Buscando la palabra [{palabra}] -> {token}")
    else:
        print("Error revisa su texto")
        