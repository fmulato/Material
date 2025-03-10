def greet_decorador(func):
    def inner(name):
        print('Hi')
        func(name)
        print('Goodbye')
    return inner

def say_name(name):
    print(name)

greet = greet_decorador(say_name)
greet('Fabricio')