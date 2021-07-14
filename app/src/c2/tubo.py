while True:
    user = input("how spacious is area? ")
    if user == "" and user == "q": break
    tubo = int(user)
    m2 = tubo * 3.31
    s = "{0}tubo is {1}m2".format(tubo, m2)
    print(s)