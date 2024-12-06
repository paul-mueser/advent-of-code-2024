content = ""
room = []
guard_pos = [0, 0, 'N']
done = False
res = 0

with open("input.txt") as file:
    content = file.read()

content = content.split("\n")
for i in range(len(content)):
    line = content[i]
    room.append([])
    for j in range(len(line)):
        if line[j] == "^":
            guard_pos = [i, j, 'N']
        room[i].append(line[j])


def move_guard_till_block(guard_pos, room):
    while True:
        if guard_pos[2] == 'N':
            if guard_pos[0] - 1 < 0:
                return
            if room[guard_pos[0] - 1][guard_pos[1]] == '#':
                guard_pos[2] = 'E'
                return
            else:
                room[guard_pos[0]][guard_pos[1]] = 'X'
                guard_pos[0] -= 1
        elif guard_pos[2] == 'E':
            if guard_pos[1] + 1 >= len(room[0]):
                return
            if room[guard_pos[0]][guard_pos[1] + 1] == '#':
                guard_pos[2] = 'S'
                return
            else:
                room[guard_pos[0]][guard_pos[1]] = 'X'
                guard_pos[1] += 1
        elif guard_pos[2] == 'S':
            if guard_pos[0] + 1 >= len(room):
                return
            if room[guard_pos[0] + 1][guard_pos[1]] == '#':
                guard_pos[2] = 'W'
                return
            else:
                room[guard_pos[0]][guard_pos[1]] = 'X'
                guard_pos[0] += 1
        elif guard_pos[2] == 'W':
            if guard_pos[1] - 1 < 0:
                return
            if room[guard_pos[0]][guard_pos[1] - 1] == '#':
                guard_pos[2] = 'N'
                return
            else:
                room[guard_pos[0]][guard_pos[1]] = 'X'
                guard_pos[1] -= 1


while True:
    move_guard_till_block(guard_pos, room)
    if guard_pos[2] == 'N' and guard_pos[0] == 0:
        break
    elif guard_pos[2] == 'E' and guard_pos[1] == len(room[0]):
        break
    elif guard_pos[2] == 'S' and guard_pos[0] == len(room):
        break
    elif guard_pos[2] == 'W' and guard_pos[1] == 0:
        break

room[guard_pos[0]][guard_pos[1]] = 'X'

for line in room:
    res += line.count('X')


print(res)