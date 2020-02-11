def convert_spisok_v_slovar(spisok):
    '''
    Конвертирует список в словарь
    '''
    slovar = {}
    if type(spisok) == type(slovar):
        #print('Заданный список - уже является словарем!')
        return spisok
    
    for element in spisok:
        if slovar.get(element) == None:
            slovar[element] = 1
        else:
            slovar[element] += 1
            
    return slovar