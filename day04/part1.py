import numpy as np

content = ""
content_array = []
res = 0

with open("input.txt") as file:
    content = file.read()

for line in content.split("\n"):
    content_array.append(line)


max_col = len(content_array[0])
max_row = len(content_array)
cols = ["" for _ in range(max_col)]
rows = ["" for _ in range(max_row)]
fdiag = ["" for _ in range(max_row + max_col - 1)]
bdiag = ["" for _ in range(len(fdiag))]
min_bdiag = -max_row + 1

for x in range(max_col):
    for y in range(max_row):
        cols[x] += content_array[y][x]
        rows[y] += content_array[y][x]
        fdiag[x+y] += content_array[y][x]
        bdiag[x-y-min_bdiag] += content_array[y][x]

for col in cols:
    res += col.count("XMAS")
    res += col.count("SAMX")

for row in rows:
    res += row.count("XMAS")
    res += row.count("SAMX")

for diag in fdiag:
    res += diag.count("XMAS")
    res += diag.count("SAMX")

for diag in bdiag:
    res += diag.count("XMAS")
    res += diag.count("SAMX")


print(res)