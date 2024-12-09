immutable_var= 1, 2, 3, 4, True, 'Projects'
print(immutable_var)

#Пример кода за изменение кортежа закомментировала, чтоб Python ошибку не выдавал в скрипте.
#immutable_var[5]= 'Project_1'
#print(immutable_var) # Значение элементов кортежа является неизменным, постоянным.

mutable_list=(1, 2, [3, 4], 'Modul')
print(mutable_list)
mutable_list[2][0]=8
print(mutable_list)