i = 8
while i < 5:
    print("while(in)=", i)
    i = i + 1
else:
    print("while(else)=", i)


k = 3
while k < 5:
    print("while(in)=", k)
    if k == 2: break
    k = k + 1
else:
    print("while(else)=", k)