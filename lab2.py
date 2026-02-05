import math

x = float(input("Введіть число: "))

numerator = math.log(math.e**(-x)) + math.cos(x - 1)
sqRoot = math.sin(3 * x) + math.cos(2 * x)
if sqRoot < 0:
    print(f"Помилка: підкореневий вираз від’ємний: {sqRoot}")
else:
    denominator = (math.log(x))**3 + math.sqrt(sqRoot)
    if denominator == 0:
        print(f"Помилка: ділення на нуль")
    else:
        result = numerator / denominator
        print(f"Результат обчислення дорівнює {result}")
