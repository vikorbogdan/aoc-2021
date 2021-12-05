from os import closerange


f = open("day_4_in", "r")
input_data = [i for i in f.read().split()]
f.close()
del f
# Drawn numbers
number_pool = tuple(int(i) for i in input_data[0].split(","))

# Bingo Boards
del input_data[0]

b_boards = [input_data[i-5:i] for i in range(5, len(input_data)+1, 5)]
b_boards = [b_boards[i-5:i] for i in range(5, len(b_boards)+1, 5)]
del input_data


def column(matrix, i):
    return [row[i] for row in matrix]


def calculate_winner(board, drawn_numbers):
    unmarked = []
    for row in board:
        for element in row:
            if int(element) not in drawn_numbers:
                unmarked.append(int(element))
    print(sum(unmarked) * drawn_numbers[-1])


def check_for_bingos(bingo_board_matrix, drawn_numbers):
    for i in bingo_board_matrix:
        for j in range(len(i[0])):
            col = column(i, j)
            k = 0
            found_bingo = True
            while k < len(col) and found_bingo:
                if int(col[k]) not in drawn_numbers:
                    found_bingo = False
                k += 1
            if found_bingo:
                calculate_winner(i, drawn_numbers)
                return True
        for j in i:
            found_bingo = True
            for k in j:
                if int(k) not in drawn_numbers:
                    found_bingo = False
            if found_bingo:
                calculate_winner(i, drawn_numbers)
                return True
    return False


drawn_numbers = []
for i in number_pool:
    drawn_numbers.append(i)
    if(check_for_bingos(b_boards, drawn_numbers)):
        break
