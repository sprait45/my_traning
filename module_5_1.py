class House:
    def __init__(self, name, number_of_flors):
        self.name = name
        self.number_of_flors = number_of_flors

    def go_to(self, new_floor):
        if 1 <= new_floor <= self.number_of_flors:
            for i in range(1, new_floor +1 ):
                print(i)
        else:
            print('Такого этажа не существует')

h1 = House('ЖК Эльбрус', 30)
h1.go_to(25)
h1.go_to(87)