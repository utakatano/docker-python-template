def mul_func(a, b): return a * b
def add_func(a, b): return a + b

def calc_5_3(func):
    return func(5, 3)

result = calc_5_3(mul_func)
print(result)

result = calc_5_3(add_func)
print(result)