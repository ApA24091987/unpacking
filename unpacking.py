def print_params(a=1, b='str', c=True):
    print(a, b, c)


# Вызов без аргументов
print_params()
# Вызов без аргументов
print_params(5)
# Вызов с двумя аргументами
print_params(1, 'str')
# Вызов с тремя аргументами
print_params(8, 'str', False)
## Вызов с именованными аргументами
print_params(b=25)
# Вызов с именованными аргументами
print_params(c=[1, 2, 3])

# используя распаковку параметров
values_list = [24, 'Я не уверен', False]
values_dict = {'a': 15, 'b': 'Я не уверен', 'c': False}
values_list_2 = [37, 'Я уверен']

print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 39)
