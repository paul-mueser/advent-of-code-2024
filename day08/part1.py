import itertools

content = ""
res = 0

with open("input.txt") as file:
    content = file.read()

content = content.split("\n")
nodes = [[c for c in line] for line in content]
antinodes = [['.' for _ in line] for line in content]


def update_antinodes(freq, pos, nodes, antinodes):
    for i in range(len(nodes)):
        line = nodes[i]
        for j in range(len(line)):
            char = line[j]
            if pos[0] == i and pos[1] == j:
                continue
            if not char == freq:
                continue
            x_off = pos[0]-i
            y_off = pos[1]-j
            if pos[0] + x_off < len(nodes) and pos[0] + x_off >= 0:
                if pos[1] + y_off < len(nodes[0]) and pos[1] + y_off >= 0:
                    antinodes[pos[0]+x_off][pos[1]+y_off] = '#'
            if i - x_off >= 0 and i - x_off < len(nodes):
                if j - y_off < len(nodes[0]) and j - y_off >= 0:
                    antinodes[i-x_off][j-y_off] = '#'



for i in range(len(nodes)):
    line = nodes[i]
    for j in range(len(line)):
        char = line[j]
        if char == '.':
            continue
        update_antinodes(char, (i,j), nodes, antinodes)


for line in antinodes:
    for char in line:
        if char == '#':
            res += 1


print(res)