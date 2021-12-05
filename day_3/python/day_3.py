from collections import Counter
with open("day_3_in")as f:
    input_data = [i for i in f.read().split()]
del f


def get_column(matrix, i):
    return [row[i] for row in matrix]


def get_gamma(column):
    c = Counter(column).most_common()
    if (c[0][0] == c[-1][0]):
        return 1
    return c[0][0]


def get_epsilon(column):
    c = Counter(column).most_common()
    if (c[0][0] == c[-1][0]):
        return 0
    return c[-1][0]


gamma, epsilon = "", ""
for i in range(len(input_data[0])):
    gamma += get_gamma(get_column(input_data, i))
    epsilon += get_epsilon(get_column(input_data, i))

first_part_ans = int(gamma, 2) * int(epsilon, 2)

gamma_list = input_data.copy()
epsilon_list = input_data.copy()


def filter_binary(matrix, generator):
    digit_list = []
    for i in range(len(matrix[0])):
        if generator == "o2":
            digit_list.append(get_gamma(get_column(matrix, i)))
        elif generator == "co2":
            digit_list.append(get_epsilon(get_column(matrix, i)))
        else:
            print("Wrong parameter when calling function 'filter_binary'")
    print(digit_list)
    # filtering out the rows
    for i in range(len(matrix[0])):
        matrix = [row for row in matrix if row[i] == digit_list[i]]
    return matrix


second_part_ans = (filter_binary(input_data, "o2"),
                   filter_binary(input_data, "co2"))

print(
    f"Solution for the first part: {first_part_ans}\nSolution for the second part: {second_part_ans}")
