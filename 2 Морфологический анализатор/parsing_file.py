from convert import convert_spisok_v_slovar
def read_file(name_file):
    '''
    Функция для считывания текстовых файлов
    
    name_file - имя файла с расширением
    
    Возвращает список(массив) строк файла
    '''
    file = open(name_file, 'r', encoding='utf-8')
    return [line.strip() for line in file]

def parsing_from_slova_only_spisok_strok(massive_strok, razdelitely):
    massive_slov = []
    razdelitely = convert_spisok_v_slovar(razdelitely)
    
    for stroka in massive_strok:
        massive_slov.append(parsing_from_slova_only_stroka(stroka, razdelitely))
    return massive_slov

def parsing_from_slova_only_stroka(stroka, razdelitely):
    '''
    Функция по разбиению строки на слова по символам из словаря razdelitely
    !Можно закинуть список, он преобразуется в словарь!
    
    На выход, подается список слов
    '''
    spisok_slov = []
    slovo = ''
    razdelitely = convert_spisok_v_slovar(razdelitely)
    
    for symbol in stroka:
        if razdelitely.get(symbol) == None:
            slovo += symbol
        else:
            spisok_slov.append(slovo)
            slovo = ''
            
    if slovo != '':
        spisok_slov.append(slovo) 
    return spisok_slov

