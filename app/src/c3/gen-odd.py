def genOdd():
    i = 1
    while i <= 30:
        yield i
        i += 2

it = genOdd()
for v in it:
    print(v, end=',')