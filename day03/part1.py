import re

content = ""
res = 0

with open("input.txt") as file:
    content = file.read()

for line in content.split("\n"):
    erg = re.findall("mul\([0-9]+\,[0-9]+\)", line)
    print(erg)
    for i in erg:
        a, b = i[4:-1].split(",")
        res += int(a) * int(b)

print(res)