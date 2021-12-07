f = open("day_5_in", "r")
input_data = [i for i in f.read().split("\n")]
f.close()
del f
input_data = [i.split("->") for i in input_data]
input_data = [[j.strip() for j in i] for i in input_data]
input_data = tuple([tuple([tuple(j.split(",")) for j in i])
                   for i in input_data])

board_width = max(max([[int(j[0]) for j in i] for i in input_data]))+1
board_height = max(max([[int(j[1]) for j in i] for i in input_data]))+1

board = [[0 for j in range(board_width)] for i in range(board_height)]

for i in input_data:
    y1 = int(i[0][0])
    y2 = int(i[1][0])
    x1 = int(i[0][1])
    x2 = int(i[1][1])
    print(x1, y1, x2, y2)
    if(x1 == x2):
        if y1 < y2:
            y = y1
            while y <= y2:
                board[x1][y] += 1
                y += 1
        elif y2 < y1:
            y = y2
            while y <= y1:
                board[x1][y] += 1
                y += 1
        else:
            board[x1][y1] += 1
    elif(y1 == y2):
        if x1 < x2:
            x = x1
            while x <= x2:
                board[x][y1] += 1
                x += 1
        elif x2 < x1:
            x = x2
            while x <= x1:
                board[x][y1] += 1
                x += 1

c = 0
for i in board:
    for j in i:
        if j > 1:
            c += 1
part_one_ans = c
print(f"Solution of the first part: {part_one_ans}")
