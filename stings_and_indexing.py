name = 'Denis' # "" или ''- выбирается в зависимости от используемых кавычек внутри строки
print(name)

print('Hello'+name) # сложение строк
print('Hello, '+name)
print('Hello, ',name)
print('Hello,', name)

print('Hello'*5)

#динамическая типизация данных - позволят работать с символми
#индексация - позволяет работать с данными внутри строки

name = 'Denis' # 0- D, 1- e, 2-n, 3- i, 5-s. Счет в строке начинается с нуля.
print(name[0])
print(name[3])
print(name[-1])

print(name[1:3])
print(name[0:4:2]) # 0:4 - интервал выборки, 2- шаг выборки
print(name[:3])
print(name[2:])
print(name[::2]) # :: - интервал от начала до конца строки, 2- шаг
print(name[::-1]) # -1 - отрицательный шаг


                            # Операции со строками

# 1. Как проверить два объекта на идентичность?
# Оператор is возвращает True в том случае, если в две переменные записана ссылка на одну и ту же область памяти.
# Не стоит путать is и ==. Оператор == проверяет лишь равенство объектов.

animals = ['python','gopher']
more_animals = animals
print(animals == more_animals) #=> True
print(animals is more_animals) #=> True
even_more_animals = ['python','gopher']
print(animals == even_more_animals) #=> True
print(animals is even_more_animals) #=> False

# Cуществует функция id, которая возвращает идентификатор адреса памяти, связанного с именем переменной.
# При вызове этой функции для двух идентичных объектов будет выдан один и тот же идентификатор.

name = 'object'
id(name) #=> 4408718312

# 2. Как проверить то, что каждое слово в строке начинается с заглавной буквы?
# Существует строковый метод istitle().

print( 'The Hilton'.istitle() ) #=> True
print( 'The dog'.istitle() ) #=> False
print( 'sticky rice'.istitle() ) #=> False

