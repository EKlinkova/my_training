tuple_ = 1, 2, 3, 4 # кортеж - неизменяемы список. в выводе будет всегда в - ()
print(tuple_)
tuple_2=(1, 2, 3, 4)
print(tuple_2)
tuple_3=tuple([1, 2, 3, 4])
print(tuple_3)
print(type(tuple_2)) # класс переменно - кортеж (tuple).
tuple_ = 1, 2, 3, True, 'String'
print(tuple_[0]) # с кортежем можно работать как со строками
print(tuple_[::2])
#tuple_[0] = 200 кортеж является неизменяемым - скрип выдает ошибку.
#print(tuple_)
tuple_ = 1, 2, 3, True, 'String'
list_ = [1, 2, 3, True, 'String']
print(tuple_.__sizeof__()) # __sizeof__ - выводи объем занимаемой памяти.
print(list_.__sizeof__()) # кортеж занимает места меньше, чем списки

tuple_=([1, 2], 3) # кортеж может содержать в себе изменяемые элементы, прим.: - список
print(tuple_)
tuple_[0][0] = 2
print(tuple_)

tuple_=([1, 2], 3) + (2, 1) # Конкатенация кортежа - сложение, работает, как в строках
print(tuple_)

tuple_= (1, 2)*3 # кортежа доступно умножение
print(tuple_)