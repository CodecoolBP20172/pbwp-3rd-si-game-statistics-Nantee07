import printing


file = open("results.txt", "w")
file.write(printing.print_get_most_played("game_stat.txt") + "\n")
file.write(printing.print_sum_sold("game_stat.txt") + "\n")
file.write(printing.print_get_selling_avg("game_stat.txt") + "\n")
file.write(printing.print_count_longest_title("game_stat.txt") + "\n")
file.write(printing.print_get_date_avg("game_stat.txt") + "\n")
file.write(printing.print_get_game("game_stat.txt", "World of Warcraft") + "\n")
file.close()
