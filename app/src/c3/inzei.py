def calc_royalty(price, sales, per):
    rate = per / 100
    ro = int(price * sales * rate)
    return ro

i = input("how much is regular price? ")
price = int(i)

i = input("how much is the number of circulation? ")
sales = int(i)

i = input("what is royalties? ")
per = float(i)

v = calc_royalty(price, sales, per)

print("royalty is", v, "yen")