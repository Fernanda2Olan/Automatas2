def separar_por_caracteres(cadena):
    caracteres = []
    for caracter in cadena:
        caracteres.append(caracter)
    return caracteres

cadena_usuario = input("Ingrese una cadena de texto: ")

caracteres_separados = separar_por_caracteres(cadena_usuario)
print("Cadena separada por caracteres: ", caracteres_separados)