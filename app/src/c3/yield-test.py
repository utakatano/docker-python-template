def gen1to3():
    yield 1;
    yield 2;
    yield 3;

it = gen1to3();

for i  in it:
    print(i)