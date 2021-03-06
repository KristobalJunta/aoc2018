import re


class Rect:
    def __init__(self, params):
        self.id = int(params[0])
        self.x = int(params[1])
        self.y = int(params[2])
        self.w = int(params[3])
        self.h = int(params[4])


with open('input.txt') as infile:
    rects = []
    field = [[0] * 1000 for _ in range(1000)]
    for line in infile.readlines():
        rects.append(Rect(re.search('#(\d+)\s@\s(\d+),(\d+):\s(\d+)x(\d+)', line).groups()))

    for rect in rects:
        for row in field[rect.x:rect.x+rect.w]:
            row[rect.y:rect.y+rect.h] = [cell+1 for cell in row[rect.y:rect.y+rect.h]]

    count = 0
    for row in field:
        for cell in row:
            count = count + 1 if cell > 1 else count

    print(count)
