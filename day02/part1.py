content = ""
reports = []
res = 0

with open("input.txt") as file:
    content = file.read()

for line in content.split("\n"):
    reports.append([int(x) for x in line.split(" ")])

for report in reports:
    increasing = report[0] < report[1]
    safe = True
    for i in range(len(report)-1):
        if increasing:
            if report[i] > report[i+1]:
                safe = False
                break
            if not 0 < report[i+1] - report[i] <= 3:
                safe = False
                break
        else:
            if report[i] < report[i+1]:
                safe = False
                break
            if not 0 < report[i] - report[i+1] <= 3:
                safe = False
                break
    if safe:
        res += 1

print(res)