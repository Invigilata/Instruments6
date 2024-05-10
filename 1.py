# Фабрика функций
def create_operation(operation):
    if operation == "add":
        def add(x, y):
            return x + y
        return add
    elif operation == "substract":
        def substract(x, y):
            return x - y
        return substract

my_func_add = create_operation("add")
my_func_substract = create_operation("substract")
print(my_func_add(4, 2))
print(float(my_func_substract(4, 2)))

# Лямбда-функции
multiply = lambda x, y: x * y
print(multiply(4, 4))

def multyply_def(x, y):
    return x * y
print(multyply_def(4, 4))

# Вызываемые объекты
class Rect:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self, *args, **kwargs):
        return self.a * self.b


rectangle = Rect(2, 4)

print("Площадь: {}".format(rectangle.__call__()))