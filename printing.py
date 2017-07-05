import reports


def print_count_games(file_name):
    count = reports.count_games(file_name)
    print("There are " + str(count) + " games")
    return "There are " + str(count) + " games"


def print_decide(file_name, year):
    is_there_a_game = reports.decide(file_name, year)
    if is_there_a_game:
        print("There is a game released in " + str(year))
        return "There is a game released in " + str(year)
    else:
        print("There is no game released in " + str(year))
        return "There is no game released in " + str(year)


def print_get_latest(file_name):
    latest = reports.get_latest(file_name)
    print("The latest game was " + latest)
    return "The latest game was " + latest


def print_count_by_genre(file_name, genre):
    count = reports.count_by_genre(file_name, genre)
    print("We have " + str(count) + " games in " + genre + " genre")
    return "We have " + str(count) + " games in " + genre + " genre"


def print_get_line_number_by_title(file_name, title):
    line_number = reports.get_line_number_by_title(file_name, title)
    print("The line number for " + title + " is " + str(line_number))
    return "The line number for " + title + " is " + str(line_number)

print_count_games("game_stat.txt")
print_decide("game_stat.txt", 2004)
print_get_latest("game_stat.txt")
print_count_by_genre("game_stat.txt", "RPG")
print_get_line_number_by_title("game_stat.txt", "World of Warcraft")