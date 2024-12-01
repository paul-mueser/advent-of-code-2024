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

val1.sort()
val2.sort()

for i in range(len(val1)):
    if val1[i] < val2[i]:
        res += val2[i] - val1[i]
    else:
        res += val1[i] - val2[i]

print(res)