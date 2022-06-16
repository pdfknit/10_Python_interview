# Создать два списка с различным количеством элементов.
# В первом должны быть записаны ключи, во втором — значения.
# Необходимо написать функцию, создающую из данных ключей и значений словарь.
# Если ключу не хватает значения, в словаре для него должно сохраняться значение None.
# Если есть  значения, которым не хватило ключей, их необходимо отбросить.


def list_to_dict(key_list, value_list):
    result = {}

    for key, value in zip(key_list, value_list):
        result[key] = value

    for key in key_list[len(value_list):len(key_list)]:
        result[key] = None

    return result


key_list = [1, 2, 4, 7, 9, 12]
value_list = [1, 2, 3]
print(list_to_dict(key_list, value_list))
