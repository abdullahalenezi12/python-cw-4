def my_name(name):
    print(f'My name is {name}')

my_name('Abdullah')

def my_food(food, drink):
    print(f'My favorite food is {food}, and i love to drink {drink} with it')

my_food('pasta', "cola")

number = int(input('pick a number '))

def cube(number):
    return number * number * number

def by_three(number):
    if number % 3 == 0:
        print(cube(number))
    else:
        print('false')
by_three(number)

