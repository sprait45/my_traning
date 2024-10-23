def print_params(a = 1, b = 'string', c = True):
    print(a,b,c)
values_list = [6.5, "Red", 87]
values_dict = {'a':'Green', 'b':[25,26,27], 'c': False}
values_list_2 = ['white', 4]
print_params(b = 25)
print_params(c = [1,2,3])
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)