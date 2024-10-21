calls = 0
def count_calls():
    global calls
    calls +=1

def string_info(string):
    count_calls()
    summer = tuple((len('summer'),'summer'.upper(), 'summer'.lower()))
    print(summer)
string_info('string')

def string_info(string):
    count_calls()
    saturday = tuple((len('saturday'),'saturday'.upper(), 'saturday'.lower()))
    print(saturday)
string_info('string')

def is_contains(string, list_to_search):
    count_calls()
    list_ = ['dog', 'hamster',]
    b = 'cat'
    if b in list_:
        print(True)
    else:
        print(False)
is_contains('string','list_to_search')

def is_contains(string, list_to_search):
    count_calls()
    list2 = ['green', 'black', 'red']
    a = 'black'
    if a in list2:
        print(True)
    else:
        print(False)
is_contains('string','list_to_search')
print(calls)