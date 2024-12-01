content = ""
val1 = []
val2 = []
res = 0

with open("input.txt") as file:
    content = file.read()

for line in content.split("\n"):
    vals = line.split("   ")
    val1.append(int(vals[0]))
    val2.append(int(vals[1]))

for elm in val1:
    res += elm * val2.count(elm)

print(res)