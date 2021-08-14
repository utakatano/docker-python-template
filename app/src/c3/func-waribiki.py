def calcValue(who, hour, count, value):
    '''function to calc discounted price in a supermarket'''
    info = 'no discount'

    if (hour == 14) and (count >= 3):
        value *= 0.9
        info = '10% off'
    elif (hour == 15) and (count >= 5):
        value *= 0.8
        info = '20% off'
    
    value = int(value)
    print("{0} paied {1}={2} yen".format(who, info, value))

calcValue("A", 15, 3, 1200)
calcValue("B", 14, 5, 2000)
calcValue("C", 15, 8, 5400)