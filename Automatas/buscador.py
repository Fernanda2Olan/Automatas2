def find_sustantivos(palabra):
    fid = open('DB/Recursos.txt')
    for line in fid:
        data = line.split(':') #0-> token, 1->lista palabras 
        for db_string in data:
            if palabra in db_string:
                print(f"\n\t Si lo encontre y su token es {data[0]}\n")
                fid.close()
                return data[0]
    
    fid.close()