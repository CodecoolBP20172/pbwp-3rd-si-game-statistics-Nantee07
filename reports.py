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


def count_games(file_name):
    data = open_stats(file_name)
    titles = data[0]
    # count = 0
    #
    # for title in titles:
    #     count += 1

    return len(titles)


def decide(file_name, year):
    data = open_stats(file_name)
    release_years = data[2]

    for release_year in release_years:
        if year == release_year:
            return True

    return False


def get_latest(file_name):
    data = open_stats(file_name)
    titles = data[0]
    release_years = data[2]
    max_year = 0
    max_index = 0

    for i in range(len(release_years)):
        if release_years[i] > max_year:
            max_year = release_years[i]
            max_index = i

    return titles[max_index]


def count_by_genre(file_name, genre):
    data = open_stats(file_name)
    genres = data[3]
    count = 0

    for gen in genres:
        if gen == genre:
            count += 1

    return count


def get_line_number_by_title(file_name, title):
    data = open_stats(file_name)
    titles = data[0]

    for i in range(len(titles)):
        if titles[i] == title:
            return i+1

    raise ValueError
