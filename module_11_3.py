
from inspect import getmodule


def introspection_info(obj):
    dict_introspection = dict()
    attributes = []
    methods = []
    for attr in dir(obj):
        if callable(getattr(obj, attr)):
            methods.append(attr)
        else:
            attributes.append(attr)
    dict_introspection['type'] = type(obj) # тип объекта
    dict_introspection['attribute'] = attributes # атрибуты объекта
    dict_introspection['method'] = methods # ищем методы объекта
    dict_introspection['module_obj'] = getmodule(obj) # проверяем к какому модулю относится
    dict_introspection['module_func'] = getmodule(introspection_info) # функция относится к модулю __main__
    return dict_introspection



number_info = introspection_info(42)
string_info = introspection_info('Логотип')

print(number_info)
print(string_info)
