food = ['apple', 'coconat', 'banana']
print(food)
print(food[0]) #0- apple, 1- coconat, 2- banana
food[0] = 'peach' # замена переменной по порядковому номеру
print(food)
food.append(True) # добавление переменной в конец списка
print(food)
food.extend('string') # при добавлении, каждый символ добавляет отдельно
print(food)
food.extend(['string']) # [] - позволяют добавить элемент, как он написан
print(food)
food.extend(['string', 2])
print(food)
food.remove('coconat') # удаление элемента списка
print(food)
print('coconat' in food) # проверка наличия элемента в списке
print('coconat' not in food) # проверят отсутствие элемента в списке.
print(food[0:4:2]) # со списком можно работать как со строками.
print(food[::2])