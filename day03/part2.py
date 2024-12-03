import re

content = ""
res = 0

with open("input.txt") as file:
    content = file.read()

enable = True
for line in content.split("\n"):
    erg = re.findall("mul\([0-9]+\,[0-9]+\)|do\(\)|don\'t\(\)", line)
    print(erg)
    for i in erg:
        if i == "do()":
            enable = True
        elif i == "don't()":
            enable = False
        elif enable:
            a, b = i[4:-1].split(",")
            res += int(a) * int(b)

print(res)