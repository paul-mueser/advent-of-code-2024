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
        char = content_array[y][x]
        if char == "X":
            char = "."
        cols[x] += char
        rows[y] += char
        fdiag[x+y] += char
        bdiag[x-y-min_bdiag] += char

for y in range(max_row-2):
    row1,row2,row3 = rows[y],rows[y+1],rows[y+2]
    for x in range(max_col-2):
        range1,range2,range3 = row1[x:x+3],row2[x:x+3],row3[x:x+3]
        w1 = range1[0] + range2[1] + range3[2]
        w2 = range1[2] + range2[1] + range3[0]
        if (w1 == "MAS" or w1 == "SAM") and (w2 == "MAS" or w2 == "SAM"):
            res += 1


print(res)