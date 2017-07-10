import reports


def print_get_most_played(file_name):
    most_played = reports.get_most_played(file_name)
    print("The title of the most played game is " + most_played)
    return "The title of the most played game is " + most_played


def print_sum_sold(file_name):
    sum_sold = reports.sum_sold(file_name)
    print(str(sum_sold) + "M copies have been sold total")
    return str(sum_sold) + "M copies have been sold total"


def print_get_selling_avg(file_name):
    selling_avg = reports.get_selling_avg(file_name)
    print("The average selling is " + str(selling_avg))
    return "The average selling is " + str(selling_avg)


def print_count_longest_title(file_name):
    longest_title = reports.count_longest_title(file_name)
    print("The longest title is " + str(longest_title) + " characters long")
    return "The longest title is " + str(longest_title) + " characters long"


def print_get_date_avg(file_name):
    date_avg = reports.get_date_avg(file_name)
    print("The average of the release dates is " + str(date_avg))
    return "The average of the release dates is " + str(date_avg)


def print_get_game(file_name, title):
    get_game = reports.get_game(file_name, title)
    print(get_game)
    return get_game

print_get_most_played("game_stat.txt")
print_sum_sold("game_stat.txt")
print_get_selling_avg("game_stat.txt")
print_count_longest_title("game_stat.txt")
print_get_date_avg("game_stat.txt")
print_get_game("game_stat.txt", "World of Warcraft")
