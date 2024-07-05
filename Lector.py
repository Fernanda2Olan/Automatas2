def load_sustantivo_sentimientos(palabra):
    fid = open("sql/Recursos.txt")
    for line in fid:
        data = line.split(':')
        for db_string in data [1].split(','):
       
            if  palabra in db_string:
                 print(f"\n\t Si lo encontre y su token es {data[0]}\n")
                 fid.close()
                 return data[0]
    
        fid.close()