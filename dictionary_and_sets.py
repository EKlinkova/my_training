                            # Словари - dictionary
phone_book={'Denis': 88008000200, 'Max': 88002000600}
print(phone_book) # Ключ - имя, значение - номер телефона. Ключ - неизменяемый объект (не список)
print(phone_book ['Denis'])
phone_book['Denis']= 81523647892 # в словаре возможно изменить значение переменной
print(phone_book)
phone_book['Anton']=8123456789 # При обращении к не существующем ключу, словарь его добавляет.
print(phone_book)
del phone_book['Max'] # удаление ключа
print(phone_book)

phone_book.update({'Sasha': 88456123792,  #добавление в имеющийся словарь нескольких ключей
                   'Masha': 880023654789})
print(phone_book)

print(phone_book.get('Denis')) # выводит значение ключа из словаря
print(phone_book.get('Kamilla')) # при обращении к несуществующему ключу в ответ - None
print(phone_book.get('Kamilla', "Такого ключа нет")) # задает ответ, при обращении к несуществующему ключу


a= phone_book.pop('Anton') # pop - удаляет ключ и возвращает соответсвующее ему значение
print(phone_book)
print(a)

list_ = [1, 2, 3] # pop - работает аналогично со списками
list_.pop(0)
print(list_)

print(phone_book.keys()) # keys - метод выводит значения ключей в словаре
print(phone_book.values()) # values - метод выводит значения всех ключей
print(phone_book.items()) # items - метод выводит значения пар: ключ+значение

                                    # Множества -sets
set_= {1, 2, 3 , 4, 5, 4, 3, 2, 1} # множиства хранят уникальные значения любых типов данных
print(set_)
set_ = {1, 2, 3, 4, 5, 4, 3, 2, 1, 'String', True, (1, 2, 3)}
print(set_)

list_=[1, 1, 2, 2, 1, 3, 3, 2, 1, 2]
list_=set(list_)
print(list_) # set - преобразует список в множество
print(list_.discard(1)) # discard или remove - удаляют элемент из множества. discard - не выдает шибки при отсутствии элемента в множестве
print(list_)
print(list_.add(5)) # add - добавляет элемент в множество
print(list_)
