

gramatica: {'a', 'á', 'ä', 'b', 'c', 'd', 'e', 'é',' ë', 'f', 'g', 'h', 'i',
            'í', 'ï', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'ó', 'ö', 'p', 'q',
            'r', 's', 't', 'u', 'ú', 'v', 'w', 'x', 'y', 'z', '0', '1', '2'
            '3', '4', '5', '6', '7', '8', '9', ',', '.', '¿', '?', '¡', '!',
            ':', ';', '_', ' '}



def analizar(cadena, gramatica):
    for caracteres in cadena:
        if caracteres.lower() not in gramatica:
            return f"ERROR, esos carácteres no están permitidos '{caracteres}'"
        return ''




def load_sustantivo(palabra):
    with open('Recursos.txt', encoding = 'utf-8') as fid:
        for line in fid:
            data = line.split(':')
            for db_string in data:
                if  palabra in db_string:
                    return int (data[0]), data
    return 0, ''

