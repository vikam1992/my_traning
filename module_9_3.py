first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']
first_result = (len(elem) - len(elem_2) for (elem, elem_2) in zip(first,second) if len(elem) != len(elem_2))
print(list(first_result))
second_result = (len(first[i]) == len(second[i]) for i in range(len(first)))
print(list(second_result))
