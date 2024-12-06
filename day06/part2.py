import copy
content = ""
room_arr = []
guard_position = [0, 0, 'N']
done = False
res = 0

with open("input.txt") as file:
    content = file.read()

content = content.split("\n")
for i in range(len(content)):
    line = content[i]
    room_arr.append([])
    for j in range(len(line)):
        if line[j] == "^":
            guard_position = [i, j, 'N']
        room_arr[i].append(line[j])


def move_guard_till_block(guard_pos, room, visited):
    while True:
        if guard_pos[2] == 'N':
            if guard_pos[0] - 1 < 0:
                return
            if room[guard_pos[0] - 1][guard_pos[1]] == '#':
                visited[guard_pos[0]][guard_pos[1]][guard_pos[2]] += 1
                guard_pos[2] = 'E'
                visited[guard_pos[0]][guard_pos[1]][guard_pos[2]] += 1
                return
            else:
                guard_pos[0] -= 1
        elif guard_pos[2] == 'E':
            if guard_pos[1] + 1 >= len(room[0]):
                return
            if room[guard_pos[0]][guard_pos[1] + 1] == '#':
                visited[guard_pos[0]][guard_pos[1]][guard_pos[2]] += 1
                guard_pos[2] = 'S'
                visited[guard_pos[0]][guard_pos[1]][guard_pos[2]] += 1
                return
            else:
                guard_pos[1] += 1
        elif guard_pos[2] == 'S':
            if guard_pos[0] + 1 >= len(room):
                return
            if room[guard_pos[0] + 1][guard_pos[1]] == '#':
                visited[guard_pos[0]][guard_pos[1]][guard_pos[2]] += 1
                guard_pos[2] = 'W'
                visited[guard_pos[0]][guard_pos[1]][guard_pos[2]] += 1
                return
            else:
                guard_pos[0] += 1
        elif guard_pos[2] == 'W':
            if guard_pos[1] - 1 < 0:
                return
            if room[guard_pos[0]][guard_pos[1] - 1] == '#':
                visited[guard_pos[0]][guard_pos[1]][guard_pos[2]] += 1
                guard_pos[2] = 'N'
                visited[guard_pos[0]][guard_pos[1]][guard_pos[2]] += 1
                return
            else:
                guard_pos[1] -= 1


def check_loop(guard_pos, room):
    visited = [[{'N': 0, 'E': 0, 'S': 0, 'W': 0} for _ in range(len(room[0]))] for _ in range(len(room))]
    while True:
        move_guard_till_block(guard_pos, room, visited)
        if guard_pos[2] == 'N' and guard_pos[0] == 0:
            return False
        elif guard_pos[2] == 'E' and guard_pos[1] == len(room[0]) - 1:
            return False
        elif guard_pos[2] == 'S' and guard_pos[0] == len(room) - 1:
            return False
        elif guard_pos[2] == 'W' and guard_pos[1] == 0:
            return False
        if visited[guard_pos[0]][guard_pos[1]][guard_pos[2]] > 5:
            return True


for i in range(len(room_arr)):
    for j in range(len(room_arr[0])):
        print(i, j)
        if room_arr[i][j] == '.':
            room = copy.deepcopy(room_arr)
            room[i][j] = '#'
            if check_loop(copy.deepcopy(guard_position), room):
                res += 1


print(res)