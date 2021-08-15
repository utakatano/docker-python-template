# for i in range(10):
#     print("Hello", i)

def say_hello(i):
    if i <= 0:
        return
    print("Hello", i)
    say_hello(i - 1)

say_hello(10)