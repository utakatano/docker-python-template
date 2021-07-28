foodstuff = [
    "Banana",
    "Mango",
    "Fish",
    "Carrot",
    "cabbage"
]

# flag_found = False

for food in foodstuff:
    if food == "Mango":
        # flag_found = True
        print("There is Mango")
        break

# if flag_found:
#     print("There is Mango")
else:
    print("Not exist")