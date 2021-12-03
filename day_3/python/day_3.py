from collections import Counter
f = open("day_3_in", "r")
input_data = tuple(i for i in f.read().split())
f.close()
del f


def column(matrix, i):
    return [row[i] for row in matrix]


gamma_rate = "".join([
    Counter(column(input_data, i)).most_common(1)[0][0] for i in range(len(input_data[0]))])
epsilon_rate = "".join([
    Counter(column(input_data, i)).most_common()[-1][0][0] for i in range(len(input_data[0]))])

part_one_ans = int(gamma_rate, 2) * int(epsilon_rate, 2)
print(part_one_ans)


s
