import linecache


def load_line(line_number):
    string_list = linecache.getline('p067_triangle.txt', line_number).split()
    int_map = map(int, string_list)
    return list(int_map)


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


def count_max():
    max_value = load_line(100)
    for i in range(99, 0, -1):
        max_value = sum_two_lines(max_value, load_line(i))
    return max_value


print(count_max())
