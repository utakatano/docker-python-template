animal_dict = {
    "Lion": 58,
    "Cheetah": 110,
    "Zebra": 60,
    "Reindeer": 80
}

li = sorted(
    animal_dict.items(),
    key = lambda x: x[1],
    reverse = True
)

for name, speed in li:
    print(name, speed)