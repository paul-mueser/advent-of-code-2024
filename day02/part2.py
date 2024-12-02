import numpy as np

content = ""
reports = []
res = 0

with open("input.txt") as file:
    content = file.read()

for line in content.split("\n"):
    reports.append([int(x) for x in line.split(" ")])

for report in reports:
    arr = np.array(report)
    diff = np.diff(arr)
    if np.all(diff > 0) and np.all(diff <= 3):
        res += 1
        continue

    if np.all(diff < 0) and np.all(diff >= -3):
        res += 1
        continue

    if sum(diff) == 0:
        continue

    if sum(diff) > 0:
        errors = 0
        error_pos = []
        for i in range(len(diff)):
            if diff[i] < 1 or diff[i] > 3:
                error_pos.append(i)
                errors += 1
        if errors > 2:
            continue
        if errors == 2:
            if error_pos[1] - error_pos[0] > 1:
                continue
            rep_copy = report.copy()
            rep_copy.pop(error_pos[1])
            arr2 = np.array(rep_copy)
            diff2 = np.diff(arr2)
            if np.all(diff2 > 0) and np.all(diff2 <= 3):
                res += 1
                continue
        else:
            rep_copy = report.copy()
            rep_copy.pop(error_pos[0] + 1)
            arr2 = np.array(rep_copy)
            diff2 = np.diff(arr2)
            if np.all(diff2 > 0) and np.all(diff2 <= 3):
                res += 1
                continue

            rep_copy = report.copy()
            rep_copy.pop(error_pos[0])
            arr2 = np.array(rep_copy)
            diff2 = np.diff(arr2)
            if np.all(diff2 > 0) and np.all(diff2 <= 3):
                res += 1
                continue
    
    if sum(diff) < 0:
        errors = 0
        error_pos = []
        for i in range(len(diff)):
            if diff[i] > -1 or diff[i] < -3:
                error_pos.append(i)
                errors += 1
        if errors > 2:
            continue
        if errors == 2:
            if error_pos[1] - error_pos[0] > 1:
                continue
            rep_copy = report.copy()
            rep_copy.pop(error_pos[1])
            arr2 = np.array(rep_copy)
            diff2 = np.diff(arr2)
            if np.all(diff2 < 0) and np.all(diff2 >= -3):
                res += 1
                continue
        else:
            rep_copy = report.copy()
            rep_copy.pop(error_pos[0] + 1)
            arr2 = np.array(rep_copy)
            diff2 = np.diff(arr2)
            if np.all(diff2 < 0) and np.all(diff2 >= -3):
                res += 1
                continue

            rep_copy = report.copy()
            rep_copy.pop(error_pos[0])
            arr2 = np.array(rep_copy)
            diff2 = np.diff(arr2)
            if np.all(diff2 < 0) and np.all(diff2 >= -3):
                res += 1
                continue

print(res)
