from collections import Counter
f = open("day_3_in", "r")
input_data = tuple(i for i in f.read().split())
f.close()
del f


def column(matrix, i):
    return [row[i] for row in matrix]


def most_in_column(matrix, column_index):
    c = Counter(column(matrix, column_index)).most_common()
    if c[0][1] == c[-1][1]:
        return 1
    return c[0][0]


def least_in_column(matrix, column_index):
    c = Counter(column(matrix, column_index)).most_common()
    if c[0][1] == c[-1][1]:
        return 0
    return c[-1][0]


gamma_rate = "".join([
    most_in_column(input_data, i) for i in range(len(input_data[0]))])
epsilon_rate = "".join([
    least_in_column(input_data, i) for i in range(len(input_data[0]))])

part_one_ans = int(gamma_rate, 2) * int(epsilon_rate, 2)
print(part_one_ans)

oxygen_generator_rating_list = list(input_data)
co2_scrubber_rating_list = list(input_data)
for i in range(len(oxygen_generator_rating_list[0])):
    oxygen_generator_rating_list = [j for j in oxygen_generator_rating_list if most_in_column(
        oxygen_generator_rating_list, i) == j[i]]
for i in range(len(co2_scrubber_rating_list[0])):
    co2_scrubber_rating_list = [j for j in co2_scrubber_rating_list if least_in_column(
        co2_scrubber_rating_list, i) == j[i]]
ogr = int(oxygen_generator_rating_list[0], 2)
co2 = int(co2_scrubber_rating_list[0], 2)
del oxygen_generator_rating_list
del co2_scrubber_rating_list
part_two_ans = ogr*co2
print(f"Solution of the first part: {part_one_ans}")
print(f"Solution of the second part: {part_two_ans,ogr,co2}")
