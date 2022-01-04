def read_games():
    with open('p054_poker.txt', 'r') as file:
        while line := file.readline().replace(" ", "").replace("\n", ""):
            game = [line[:10], line[10:]]
    return game


cards = list()
cards.append(read_games())


def check_color(game):
    colors = dict()
    for i in range(1, len(game), 2):
        color = game[i]
        colors[color] = colors.get(color, 0) + 1
    got_it = max(colors.values())
    if got_it == 5:
        return 2
    elif got_it == 4:
        return 1
    else:
        return 0


def check_figures(game):
    figures = dict()
    for i in range(0, len(game), 2):
        figure = game[i]
        if figure == 'J':
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
    return sorted_figures


def check_straight(game):
    figures = check_figures(game)
    order = list(figures)
    for i in range(1, len(order)):
        if order[i - 1] == order[i] - 1:
            continue
        else:
            return False
    return True


print(check_color(cards[0][0]))
print(check_figures(cards[0][0]))
print(check_straight(cards[0][0]))
