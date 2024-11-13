class House:
    def __init__(self, name, number_of_flors):
        self.name = name
        self.number_of_flors = number_of_flors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_flors}"

    def __eq__(self, other):
        if isinstance(other.number_of_flors, int) and isinstance(other, House):
            return self.number_of_flors == other.number_of_flors

    def __lt__(self, other):
        if isinstance(other.number_of_flors, int) and isinstance(other, House):
            return self.number_of_flors < other.number_of_flors

    def __le__(self, other):
        if isinstance(other.number_of_flors, int) and isinstance(other, House):
            return self.number_of_flors <= other.number_of_flors

    def __gt__(self, other):
        if isinstance(other.number_of_flors, int) and isinstance(other, House):
            return self.number_of_flors > other.number_of_flors

    def __ge__(self, other):
        if isinstance(other.number_of_flors, int) and isinstance(other, House):
            return self.number_of_flors >= other.number_of_flors

    def __ne__(self, other):
        if isinstance(other.number_of_flors, int) and isinstance(other, House):
            return self.number_of_flors != other.number_of_flors

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_flors = self.number_of_flors + value
            return self

    def __radd__(self, value):
        self.number_of_flors += value
        return self

    def __iadd__(self, value):
        self.number_of_flors += value
        return self



h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)
print(h1 == h2)
print(h1 >= h2)
print(h1 < h2)
print(h1 <= h2)
print(h1 != h2)
h1 = h1 + 10
print(h1)
h1 += 10
print(h1)
h2 = 10 + h2
print(h2)