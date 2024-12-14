
from inspect import getmodule


def introspection_info(obj):
    dict_introspection = dict()
    dict_introspection['type'] = type(obj) # тип объекта
    dict_introspection['attribute'] = dir(obj) # атрибуты объекта
    dict_introspection['method'] = hasattr(obj, 'upper') # ищем методы объекта
    dict_introspection['module_obj'] = getmodule(obj) # проверяем к какому модулю относится
    dict_introspection['module_func'] = getmodule(introspection_info) # функция относится к модулю __main__
    return dict_introspection



number_info = introspection_info(42)
string_info = introspection_info('Логотип')

print(number_info)
print(string_info)
