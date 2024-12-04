import numpy as np

content = ""
content_array = []
res = 0

with open("input2.txt") as file:
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
        char = content_array[y][x]
        if char == "X":
            char = "."
        cols[x] += char
        rows[y] += char
        fdiag[x+y] += char
        bdiag[x-y-min_bdiag] += char

for i in range(len(fdiag)):
    print(fdiag[i])
    if fdiag[i].count("MAS") == 0 or fdiag[i].count("SAM") == 0:
        continue
    #if bdiag[len(bdiag)-i].count("MAS") == 0 or bdiag[len(bdiag)-i].count("SAM") == 0:
    #    continue
    print(fdiag[i])
    print(bdiag[len(bdiag)-i])


print(res)