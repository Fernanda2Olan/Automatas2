

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


with open ('gramatica.txt', 'r', encoding= 'utf-8') as file:
    cadena_usuario = file.read().strip()
    caracteres_denegados = analizar(cadena_usuario)
    
    
def archivoTokens(listaTokens):
    with open('tokens.txt', 'w', encoding= 'utf-8') as file:
        for token in listaTokens:
            file.write(f"{token}\n")
            
if caracteres_denegados:
    print(caracteres_denegados)
else: listaTokens = []
for componente in cadena_usuario.split():
        token, data = load_sustantivo(componente)
        print(f"\La palabra {componente} tiene como token {token} ")
        listaTokens.append(token)
        
archivoTokens(listaTokens)