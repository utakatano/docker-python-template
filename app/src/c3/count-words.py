text = """
Keep oon asking, and it will be given you;
keep on seeking, and you will find;
keep on knocking, and it will be opened to you;
for everyone asking receives. and everyone seeking finds,
and to everyone knocking, it will be opened.
"""

text = text.replace(";", "")
text = text.replace(",", "")
text = text.replace(".", "")
words = text.split()

counter = {}
for w in words:
    ws = w.lower()
    if ws in counter:
        counter[ws] += 1
    else:
        counter[ws] = 1

for k,v in sorted(counter.items()):
    if v >= 3:
        print(k, v)