#Validación de caracteres en la gramatica latina

caracteres = {'a', 'á', 'b', 'c', 'd', 'e', 'é', 'f', 'g', 'h', 'i', 'í', 'j',
              'k', 'l', 'm', 'n', 'ñ', 'o', 'ó', 'p', 'q', 'r', 's', 't',
              'u', 'ú', 'ü', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4',
              '5', '6', '7', '8', '9', ',', '.', ';', ':', '!', '¡', '¿', '?',
              '-', ' '}

def separar_por_caracteres(cadena):
    cadena = cadena.lower()
    for caracters in cadena:
        if caracters not in caracteres:
            return f"Error, el carácter es invalido {caracters}"    
    return list (cadena)

cadena_usuario = input("Ingrese una cadena de texto: ")

caracteres_separados = separar_por_caracteres(cadena_usuario)
print("Cadena separada por caracteres: ", caracteres_separados)