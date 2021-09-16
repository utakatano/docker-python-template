import re

words = [
    "orange", "october", "octopus",
    "order", "banana", "baby", "busy"
]

pattern = r"oc.*"

print("pattern with 'oc' as begining", pattern)

for word in words:
    if re.match(pattern, word):
        print("-", word)

pattern = r"b.*y"

print("pattern with 'b' as begining and 'y' as end", pattern)

for word in words:
    if re.match(pattern, word):
        print("-", word)
