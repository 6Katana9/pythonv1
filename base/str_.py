'==================Строки(str)=================='
# строки - неизменяемый тип данных, который предназначен для хранения текста (последовательности символов), заключенного в одинарные или двойные кавычки

string1 = 'строка с одинарными кавычками'

string2 = "строка с двойными кавычками"

# error = 'не правильная строка"

string3 = "Don't"

string4 = " Мой никнейм 'Katana' "

string5 = '''
 Привет
 как 
 дела 
'''

string6 = """ Привет 
как 
ты
"""

str7 = 'Привет' + ' ' + 'как дела?'
# print(str7)

# Конкатенация - склеивание строк 

str8 = 'Ha ' * 100
# print(str8)


'=================Экранизация======================'
# '\n' - перенос на новую строку
# print('hello world') # hello world
# print('hello\nworld') # hello
                      # world

# '\t' - табуляция 
# print('hello\tworld') # hello   world

# print('Don\'t')
# print("Don\"t")


# '\v' - перенос на новую строку со смещением вправо на длинну предыдущей строки

# print('hello\vworld\vmetalabs')

# '\r' - перенос каретки на начало строки 
# print('Hello world\rGO')

'==================Форматирование строк====================='
# title = 'iPhone 16'
# price = 150000

# message = f'Я купил {title} за {price} сом'
# print(message)

# message2 = 'Я купил {} за {} сом'
# print(message2.format(price, title))
# print(message2.format('sdhfdjfdfs', 1324000)) 

# message3 = 'Я купил %s за %s сом'
# print(message3 % (title, price))


'===================Методы строк======================='
# методы - функции, которые относятся к определенному классу (типу данных), к ним мы обращаемся через точку

# str1 = 'hello'
# print(str1.upper()) # hello -> HELLO
# print('HELLO'.lower()) # HELLO -> hello
# print('HeLlO'.swapcase()) # HeLlO -> hElLo
# print('hello woRld'.capitalize()) # hello woRld -> Hello world
# print('helLo woRld'.title()) # helLo woRld -> Hello World

# print(dir(str))

# print('hello'.center(11)) # '   hello   '
# print('hello'.center(11, '*')) # '***hello***'
# print('hello world'.count('l')) # 3
# print('hello world'.count('ll')) # 1
# print('hello world'.startswith('he')) # True 
# print('hello world'.startswith('H')) # False
# print('hello world'.endswith('rld')) # True
# print('hello world'.endswith('gsd')) # False
# print('hello world'.islower()) # True
# print('heLlo world'.islower()) # False
# print('hello world'.isupper()) # False
# print('Hello world'.isupper()) # False
# print('HELLO WORLD'.isupper()) # True
# print('hello'.isdigit()) # False
# print('hello43434'.isdigit()) # False
# print('4343'.isdigit()) # True
# print('hello'.isalpha()) # True
# print('hello1231'.isalpha()) # False
# print('1233'.isalpha()) # False
# print('hello 123'.isalnum()) # False
# print('hello123'.isalnum()) #  True
# print('hello'.isalnum()) #  True
# print('123'.isalnum()) #  True
# print('hello world'.replace('e', 'i')) # hillo world
# print('hello world'.replace('o', 'i')) # helli wirld
# print('hello world'.replace('l', 'i', 3)) # heiio worid
# ''.split()
# ''.join()

'=====================Индексы==========================='
# index - порядковый номер элемента в последовательности (символа в строке) индексация начинается с 0

# 'h e l l o   w o r l d'
#  0 1 2 3 4 5 6 7 8 9 10
#               ... -2 -1

string = 'hello world'
print(string[0]) # h
print(string[10]) # d
print(string[-1]) # d
print(string[5]) # ' '

# срез - подстрока строки (часть строки) - str[start:end:step]
print(string[2:5]) # llo
print(string[0:4]) # hell
print(string[4:]) # o world
print(string[:]) # hello world
print(string[::2]) # hlowrd
print(string[::-1]) # dlrow olleh
print(string[:-5:-1]) # dlro

str10 = 'hello'
print(str10.replace('h','d')) # dello
print(str10) # hello 
