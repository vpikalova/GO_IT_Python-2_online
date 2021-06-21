import sys
slovar = {'а':'a','б':'b','в':'v','г':'g','д':'d','е':'e','ё':'yo',
      'ж':'zh','з':'z','и':'i','й':'i','к':'k','л':'l','м':'m','н':'n',
      'о':'o','п':'p','р':'r','с':'s','т':'t','у':'u','ф':'f','х':'h',
      'ц':'c','ч':'ch','ш':'sh','щ':'sch','ъ':'','ы':'y','ь':'','э':'e',
      'ю':'u','я':'ya', 'А':'A','Б':'B','В':'V','Г':'G','Д':'D','Е':'E','Ё':'YO',
      'Ж':'ZH','З':'Z','И':'I','Й':'I','К':'K','Л':'L','М':'M','Н':'N',
      'О':'O','П':'P','Р':'R','С':'S','Т':'T','У':'U','Ф':'F','Х':'H',
      'Ц':'C','Ч':'CH','Ш':'SH','Щ':'SCH','Ъ':'','Ы':'y','Ь':'','Э':'E',
      'Ю':'U','Я':'YA'}
 
def normalize(string):
    string_final = ""
    for i in string:
        if i in slovar:
            string_final += slovar[i]
        elif i.isdigit() or 65<=ord(i)<=90 or 97<=ord(i)<=122: 
            string_final += i
        else:
            string_final += "_"
    return string_final

def main():
    ## Проверяем функцию на тестовой строке
    try:
        print(normalize(sys.argv[1]))
    except:
        print(normalize("TEST String 1234 <><,. Привет Саша Тыква Щука"))

if __name__ == '__main__':
    main()
    
