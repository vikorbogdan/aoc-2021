
# https://adventofcode.com/2021/day/2

# Read input file

f = open("day_2_in", "r")
input_data = tuple(tuple(i.split()) for i in f.read().split("\n"))[:-1]
f.close()
del f
input_data = tuple([tuple((i[0], int(i[1]))) for i in input_data])
print(input_data)
# Task 1 - Calculate the horizontal position and depth you would have after following the planned course.
# What do you get if you multiply your final horizontal position by your final depth?

horizontal_position = 0
depth = 0

for i in input_data:
    if i[0] == "forward":
        horizontal_position += i[1]
    elif i[0] == "up":
        depth -= i[1]
    else:
        depth += i[1]

part_one_ans = depth * horizontal_position

# Task 2 - Using new interpretation of the commands, calculate the horizontal position and depth
# you would have after following the planned course.
# What do you get if you multiply your final horizontal position by your final depth?

horizontal_position = 0
depth = 0
aim = 0

for i in input_data:
    if i[0] == "down":
        aim += i[1]
    elif i[0] == "up":
        aim -= i[1]
    elif i[0] == "forward":
        horizontal_position += i[1]
        depth += aim * i[1]

part_two_ans = horizontal_position * depth

print(
    f"Solution of the first part: {part_one_ans}\nSolution of the second part: {part_two_ans}")
