fruits = {
    'banana': 300,
    'orange': 240,
    'strawberry': 350,
    'mango': 400 
}

# for name in fruits.keys():
#     price = fruits[name]
for name, price in fruits.items():
    s = "{0} is {1} yen".format(name, price)
    print(s)