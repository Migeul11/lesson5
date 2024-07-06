# 2. Задайте переменные разных типов данных:
#   - Создайте переменную immutable_var и присвойте ей кортеж из нескольких элементов разных типов данных.
immutable_var = (3, True, "text")

#   - Выполните операции вывода кортежа immutable_var на экран.
print(immutable_var)

# 3. Изменение значений переменных:
#   - Попытайтесь изменить элементы кортежа immutable_var. Объясните, почему нельзя изменить значения элементов кортежа.
# immutable_var[0] = 1
# вызывает ошибку, так как элементы кортежа в отличие от элементов списка менять нельзя:
# Traceback (most recent call last):
#   File "C:\Users\Miguel\PycharmProjects\pythonProject1\'homework5.py", line 10, in <module>
#     immutable_var[0] = 1
#     ~~~~~~~~~~~~~^^^
# TypeError: 'tuple' object does not support item assignment

# 4. Создание изменяемых структур данных:
#   - Создайте переменную mutable_list и присвойте ей список из нескольких элементов.
mutable_list = [2, False, "string"]

#   - Измените элементы списка mutable_list.
mutable_list[2] = "text"

#   - Выведите на экран измененный список mutable_list.
print(mutable_list)
