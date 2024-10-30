def calculet(*args):
        total = 0

        for i in args:
            if isinstance(i, (list, tuple, set)):
                total += calculet(*i)
            elif isinstance (i, dict):
                total +=calculet(*i.items())
            elif isinstance(i, str):
                total += len(i)
            elif isinstance(i, (int, float)):
                    total += i

        return total

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]
result = calculet(data_structure)
print(result)