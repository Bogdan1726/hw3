int_a = 55
str_b = 'cursor'
set_c = {1, 2, 3}
lst_d = [1, 2, 3]
dict_e = {'a': 1, 'b': 2, 'c': 3}
print(id(int_a))
print(id(str_b))
print(id(set_c))
print(id(lst_d))
print(id(dict_e))
lst_d.append(4)
lst_d.append(5)
print(id(lst_d))
print(type(int_a), type(str_b), type(set_c), type(lst_d), type(dict_e))

print(isinstance(int_a, int), isinstance(str_b, str), isinstance(set_c,set), isinstance(lst_d, list), isinstance(dict_e, dict))

