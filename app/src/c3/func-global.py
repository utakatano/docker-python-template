value = 100

def changeValue():
    global value
    value = 20

changeValue()
print('value=', value)