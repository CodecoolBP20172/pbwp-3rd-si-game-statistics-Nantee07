def open_stats(file_name):
    titles = list()
    copies = list()
    releaseDates = list()
    genres = list()
    publishers = list()

    with open(file_name, "r") as stats:
        for line in stats:
            splitted = line.strip().split("\t")
            titles.append(splitted[0])
            copies.append(float(splitted[1]))
            releaseDates.append(int(splitted[2]))
            genres.append(splitted[3])
            publishers.append(splitted[4])

    return titles, copies, releaseDates, genres, publishers


def get_most_played(file_name):
    data = open_stats(file_name)
    titles = data[0]
    copies = data[1]
    max_copies = 0
    max_index = 0

    for i in range(len(copies)):
        if copies[i] > max_copies:
            max_copies = copies[i]
            max_index = i

    return titles[max_index]


def sum_sold(file_name):
    data = open_stats(file_name)
    copies = data[1]
    sum_sold = sum(copies)

    return sum_sold


def get_selling_avg(file_name):
    data = open_stats(file_name)
    copies = data[1]
    selling_avg = sum(copies) / len(copies)

    return selling_avg


def count_longest_title(file_name):
    data = open_stats(file_name)
    titles = data[0]
    max_len = 0
    max_index = 0
    longest_title = 0

    for i in range(len(titles)):
        if len(titles[i]) > max_len:
            max_len = len(titles[i])
            max_index = i
            longest_title = len(titles[max_index])

    return longest_title


def get_date_avg(file_name):
    data = open_stats(file_name)
    releaseDates = data[2]
    date_avg = sum(releaseDates) / len(releaseDates)

    return round(date_avg)


def get_game(file_name, title):
    data = open_stats(file_name)
    titles = data[0]
    copies = data[1]
    releaseDates = data[2]
    genres = data[3]
    publishers = data[4]

    game_prop = []

    for i in range(len(titles)):
        if titles[i] == title:
            game_prop.append(titles[i])
            game_prop.append(copies[i])
            game_prop.append(releaseDates[i])
            game_prop.append(genres[i])
            game_prop.append(publishers[i])

    return game_prop
