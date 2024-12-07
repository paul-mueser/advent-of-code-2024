import itertools

content = ""
calculations = []
res = 0

with open("input.txt") as file:
    content = file.read()

for line in content.split("\n"):
    calc = line.split(": ")
    calculations.append((int(calc[0]), [int(x) for x in calc[1].split(" ")]))


def valid_calc(checksum, numbers):
    operations = list(itertools.product(["+", "*", "||"], repeat=len(numbers)-1))
    for op in operations:
        res = numbers[0]
        for i in range(1, len(numbers)):
            if op[i-1] == "+":
                res += numbers[i]
            elif op[i-1] == "*":
                res *= numbers[i]
            elif op[i-1] == "||":
                res = int(str(res) + str(numbers[i]))
            if res > checksum:
                break
        if res == checksum:
            return True
    return False
        


for calc in calculations:
    if valid_calc(calc[0], calc[1]):
        res += calc[0]

print(res)