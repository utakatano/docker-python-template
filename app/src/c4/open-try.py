a_file = open("test.txt", mode="w")
try:
    a_file.write("I have not failed.\n")
    a_file.write("I've just found 10,000 ways that won't work.\n")
finally:
    a_file.close()