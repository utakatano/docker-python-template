def for_func(iterable, callback):
    it = iter(iterable)

    while True:
        try:
            v = next(it)
            callback(v)
        except StopIteration:
            break

nums = [1, 2, 3]

for_func(
    nums,
    lambda i: print(i)
)

age = {'Taro': 20, 'Jiro': 15, 'Saburo': 18}

for_func(
    age.items(),
    lambda n: print(n)
)