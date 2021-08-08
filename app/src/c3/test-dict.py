records = {
    'Tanaka': 72,
    'Yamada': 65,
    'Hirata': 100,
    'Akai': 56,
    'Fukuda': 66,
    'Sakai': 80
}

sum_v = 0
for v in records.values():
    sum_v += v

ave_v = sum_v / len(records)

print("Total point:", sum_v)
print("Average point:", ave_v)

fmt = "| {0:<7} | {1:>4} | {2:>5}"
print("| name    | point| diff")

for name, v in sorted(records.items()):
    diff_v = v - ave_v
    diff_v = round(diff_v, 1)
    print(fmt.format(name, v, diff_v))