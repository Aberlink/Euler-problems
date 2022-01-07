def check_figures(game):
    figures = dict()
    for i in range(0, len(game), 2):
        figure = game[i]
        if figure == 'T':
            figure = 10
        elif figure == 'J':
            figure = 11
        elif figure == 'Q':
            figure = 12
        elif figure == 'K':
            figure = 13
        elif figure == 'A':
            figure = 14
        else:
            figure = int(figure)
        figures[figure] = figures.get(figure, 0) + 1
    sorted_figures = dict(sorted(figures.items()))
    x = sorted(sorted_figures.values())
    return sorted_figures


def royal_flush(game):
    if straight(game) and color(game) and max(check_figures(game)) == 14:
        return True
    else:
        return False


def r_f_w(p1, p2):
    if royal_flush(p1) or royal_flush(p2):
        if royal_flush(p1) and royal_flush(p2):
            return 0
        elif royal_flush(p1):
            return 1
        else:
            return 2


def straight_flush(game):
    if straight(game) and color(game):
        return True
    else:
        return False


def s_f_w(p1, p2):
    if straight_flush(p1) and straight_flush(p2):
        return s_c_w(p1, p2)
    elif royal_flush(p1):
        return 1
    else:
        return 2


def four_of_a_kind(game):
    if max(check_figures(game).values()) == 4:
        return True
    else:
        return False


def f_w(p1, p2):
    if four_of_a_kind(p1) and four_of_a_kind(p2):
        return s_c_w(p1, p2)
    elif four_of_a_kind(p1):
        return 1
    else:
        return 2


def color(game):
    colors = dict()
    for i in range(1, len(game), 2):
        flush = game[i]
        colors[flush] = colors.get(flush, 0) + 1
    got_it = max(colors.values())
    if got_it == 5:
        return True
    else:
        return False


def c_w(p1, p2):
    if color(p1) and color(p2):
        return s_c_w(p1, p2)
    elif color(p1):
        return 1
    else:
        return 2


def full_house(game):
    if sorted(check_figures(game).values())[0] == 2 and sorted(check_figures(game).values())[1] == 3:
        return True
    else:
        return False


def f_h_w(p1, p2):
    if full_house(p1) and full_house(p2):
        return s_c_w(p1, p2)
    elif full_house(p1):
        return 1
    else:
        return 2


def straight(game):
    figures = check_figures(game)
    order = list(figures)
    if len(order) == 5:
        for i in range(1, len(order)):
            if order[i - 1] == order[i] - 1:
                continue
            else:
                return False
        return True
    else:
        return False


def s_w(p1, p2):
    if straight(p1) and straight(p2):
        return s_c_w(p1, p2)
    elif straight(p1):
        return 1
    else:
        return 2


def three_of_kind(game):
    if sorted(check_figures(game).values())[2] == 3:
        return True
    else:
        return False


def t_w(p1, p2):
    if three_of_kind(p1) and three_of_kind(p2):
        return s_c_w(p1, p2)
    elif three_of_kind(p1):
        return 1
    else:
        return 2


def two_pairs(game):
    if sorted(check_figures(game).values())[1] == 2 and sorted(check_figures(game).values())[2] == 2:
        return True
    else:
        return False


def t_p_w(p1, p2):
    if two_pairs(p1) and two_pairs(p2):
        return s_c_w(p1, p2)
    elif two_pairs(p1):
        return 1
    else:
        return 2


def pair(game):
    if sorted(check_figures(game).values())[3] == 2:
        return True
    else:
        return False


def p_w(p1, p2):
    if pair(p1) and pair(p2):
        return s_c_w(p1, p2)
    elif pair(p1):
        return 1
    else:
        return 2


def one_card(game, position):
    x = sorted(check_figures(game).items(), key=lambda kv:(kv[1], kv[0]))
    return x[position][0]


def s_c_w(p1, p2):
    for i in range(-1, -5, -1):
        if one_card(p1, i) < one_card(p2, i):
            return 2
        elif one_card(p1, i) > one_card(p2, i):
            return 1
    return 0


def read_games_wins():
    results = dict()
    with open('p054_poker.txt', 'r') as file:
        while line := file.readline().replace(" ", "").replace("\n", ""):
            p1 = line[:10]
            p2 = line[10:]
            if royal_flush(p1) or royal_flush(p2):
                results[r_f_w(p1, p2)] = results.get(r_f_w(p1, p2), 0) + 1
            elif straight_flush(p1) or straight_flush(p2):
                results[s_f_w(p1, p2)] = results.get(s_f_w(p1, p2), 0) + 1
            elif four_of_a_kind(p1) or four_of_a_kind(p2):
                results[f_w(p1, p2)] = results.get(f_w(p1, p2), 0) + 1
            elif color(p1) or color(p2):
                results[c_w(p1, p2)] = results.get(c_w(p1, p2), 0) + 1
            elif full_house(p1) or full_house(p2):
                results[f_h_w(p1, p2)] = results.get(f_h_w(p1, p2), 0) + 1
            elif straight(p1) or straight(p2):
                results[s_w(p1, p2)] = results.get(s_w(p1, p2), 0) + 1
            elif three_of_kind(p1) or three_of_kind(p2):
                results[t_w(p1, p2)] = results.get(t_w(p1, p2), 0) + 1
            elif two_pairs(p1) or two_pairs(p2):
                results[t_p_w(p1, p2)] = results.get(t_p_w(p1, p2), 0) + 1
            elif pair(p1) or pair(p2):
                results[p_w(p1, p2)] = results.get(p_w(p1, p2), 0) + 1
            else:
                results[s_c_w(p1, p2)] = results.get(s_c_w(p1, p2), 0) + 1
    return results


print(read_games_wins())


