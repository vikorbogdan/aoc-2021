# Read input file

f = open("day_1_in", "r")
input_data = tuple(int(i) for i in f.read().split())
f.close()
del f

def count_increase(values):
    c = 0
    for i in range(1, len(values)):
        if (values[i] > values[i - 1]):
            c += 1
    return c

# Part 1 - the number of times a depth measurement increases from the previous measurement


part_one_ans = count_increase(input_data)

# Part 2 - the number of times the sum of measurements in this sliding window increases
sum_list = [sum(input_data[i:i+3]) for i in range(0,len(input_data)-2) ]
part_two_ans = count_increase(sum_list)

print(f"Part one answer: {part_one_ans}\nPart two answer: {part_two_ans}")
