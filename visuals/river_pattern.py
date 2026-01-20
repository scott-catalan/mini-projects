import random, time

leftShore = "HlIiioo::."
rightShore = leftShore[::-1]

width = 40

riverSize = random.randint(1,9)
leftSize = random.randint(1,(width - riverSize - len(leftShore) - len(rightShore)) // 2)

while True:
    riverSize = random.randint(max(1, riverSize - 2), min(9, riverSize + 2))
    leftSize = random.randint(max(1, leftSize - 1), min(9, 20 - riverSize - 1))
    rightSize = 20 - riverSize - leftSize
    leftLand = ''
    rightLand = ''
    river = ''
    for a in range(leftSize):
        leftLand += "|/"
    for b in range(rightSize):
        rightLand += "\\|"
    if riverSize <= 0:
        pass
    else:
        for c in range(riverSize):
            river += "_"
        if riverSize % 2 == 1:
            add = "|"
        else:
            add = ''
    line = f"{leftLand}{leftShore}{river}{rightShore}{add}{rightLand}"
    while len(line) < 58:
        line += "\\|"
    while len(line) > 58:
        line = line[:-2]
    
    print(line)
    time.sleep(0.15)