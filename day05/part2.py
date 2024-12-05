content = ""
# When key is in the manual, val has to be also in the manual before key if both are in the same manual
rules = dict()
res = 0

with open("input.txt") as file:
    content = file.read()

parts = content.split("\n\n")
for rule in parts[0].split("\n"):
    rule = rule.split("|")
    if int(rule[1]) in rules.keys():
        rules[int(rule[1])].append(int(rule[0]))
    else:
        rules[int(rule[1])] = [int(rule[0])]

violations = []

def check_violation(man):
    for i in range(len(man)):
        val = int(man[i])
        if val in rules.keys():
            for j in range(len(man)):
                if j == i:
                    continue
                val2 = int(man[j])
                if val2 in rules[val]:
                    if j > i:
                        return True
    return False

for man in parts[1].split("\n"):
    man = man.split(",")
    if check_violation(man):
        violations.append(man)

for violation in violations:
    while check_violation(violation):
        for i in range(len(violation)):
            val = int(violation[i])
            if val in rules.keys():
                for j in range(len(violation)):
                    if j == i:
                        continue
                    val2 = int(violation[j])
                    if val2 in rules[val]:
                        if j > i:
                            violation[i], violation[j] = violation[j], violation[i]
                            break
    res += int(violation[len(violation)//2])

print(res)