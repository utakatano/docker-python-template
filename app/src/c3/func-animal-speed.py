animal_speed_dict = {
    "Cheetah": 110,
    "Reindeer": 80,
    "Zebra": 60,
    "Lion": 58,
    "Giraffe": 50,
    "Camel": 30
}

distance_dict = {
    "Shizuoka": 183.7,
    "Nagoya": 350.6,
    "Osaka": 507.5
}

def calc_time(dist, speed):
    t = dist / speed
    t = round(t, 1)
    return t

def calc_animal(animal, speed):
    res = "|" + animal
    for city in sorted(distance_dict.keys()):
        dist = distance_dict[city]
        t = calc_time(dist, speed)
        res += "|{0:>6}".format(t)
    return res + "|"

print("+--------+--------+--------+--------+")
print("|animal name", end="")

for city in sorted(distance_dict.keys()):
    print("|" + city, end="")
print("|")
print("+--------+--------+--------+--------+")

for animal, speed in animal_speed_dict.items():
    s = calc_animal(animal, speed)
    print(s)
print("+--------+--------+--------+--------+")
