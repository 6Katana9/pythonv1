'=============Логические и условные операторы============'
# логические операторы - выражения, которые возвращают True, если выражение верное, False - если выражение не верное


'Равенство'
10 == 5 # False
5 == 5 # True
# print('hi' == 2)
'hi' == 'hi' # True
'Hi' == 'hi' # False 
'5' == 5 # False
'+'=='+' # True

'Не равенство'
4 != 5 # True
5 != 5 # False

'Больше'
10 > 10 # False
4 > 1 # True

'Меньше'
5 < 4 # False 
10 < 10 # False 

'Больше или равно'
10 >= 4 # True
10 >= 10 # True
4 >= 5 # False

'Меньше или равно'
10 <= 10 # True
5 <= 10 # True
10 <= 5 # False


'======================And Or Not============================'

#and - и
#or - или
#not - не

a = 5
b = 6 


#True   и    True
a == 5 and b == 6 # True 

#False  и    True
a == 7 and b == 6 # False

#False  и  True
a > 10 and b <= 6 # False

#False  и  False
a == 0 and b == 0 # False

# если все части выражения возвращабт True - будет True
# если хотя бы одна часть выражения False - будет False


#True  или True 
a == 5 or b == 6 # True

#False или True 
a > 10 or b == 6 # True 

#True  или False 
a < 20 or b == 10 # True

#False или False
a == 1 or b == 1 # False


# если хотябы одна часть выражения возвращает True - будет True


not True # False
not False # True

    # True
print(not a == 5)   # False 

                 
not a < 20 or not b == 6 # False

a = 5
b = 6


# 
# print(not b > 20 and a == 5 or b == 6 or a < 6 and b >= 6 or not a == 5 and 5 == 10) # True


'========================Boolean type=============================='
# Булевый тип данных имеет всего 2 значения True и False




bool(1) # True
bool(-12) # True
bool(0) # False

bool('hello') # True
bool(' ') # True
bool('_') # True
bool('') # False

bool(True) # True
bool(False) # False


'========================NoneType==========================='
# None - неизменяемый тип данных с одним значением None, который используется для обозначения отсутствия значения

# a = None
# bool(None) # False


# a = 5
# b = 5

# a == b # True
# print(a is b) 


# v = 'num'
# # n = 'num'
# # print(id(v), id(n))


# '=====================Условные операторы=============================='
# # Условные операторы - конструкция, которая используется для того, чтобы при разных данных код работал по разному (в зависимости от условия)



# # if условие1:
# #     действие1


# pogoda = input('Введите погоду: ') # солнечно

# if pogoda == 'солнечно':
#     print('Взять солнц-очки')
    

# if pogoda == 'шторм':
#     print('спать')

# if pogoda == 'снег':
#     print('Сидеть дома')
# elif pogoda == 'дождливо':
#     print('Взять зонтик')
# elif ...:
#     ...
# else:
#     print('Пока')


'===============================Тернарный оператор========================================'
# тернарный оператор - условие в одну строку

num = -23


if num > 0: # условие1
    chislo = 'положительное' # действие1
else:
    chislo = 'отрицательное' # действие2
print(chislo)

# chislo = действие1 if условие1 else действие2

chislo = 'положительное' if num > 0 else 'отрицательное'
print(chislo)