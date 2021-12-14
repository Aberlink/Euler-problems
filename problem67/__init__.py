import linecache


def load_line(line_number):
    string_list = linecache.getline('p067_triangle.txt', line_number).split()
    int_map = map(int, string_list)
    return list(int_map)


def generate_empty_row():
    empty = []
    for i in range(0, 101):
        empty.append(0)
    return empty


def sum_two_lines(bot_line, top_line):
    sum_line = []
    for i in range(0, len(top_line)):
        temporary1 = top_line[i] + bot_line[i]
        temporary2 = top_line[i] + bot_line[i + 1]
        if temporary1 >= temporary2:
            sum_line.append(temporary1)
        else:
            sum_line.append(temporary2)
    return sum_line


max_value = sum_two_lines(generate_empty_row(), load_line(100))
for i in range(99, 0, -1):
    max_value = sum_two_lines(max_value, load_line(i))
print(max_value)

