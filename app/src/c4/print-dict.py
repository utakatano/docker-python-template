import re

zipre = re.compile(r"^[0-9]{3}\-[0-9]{4}$")

print(zipre.search("440-0012"))

print(zipre.search("1111-2222"))