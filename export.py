import printing

data_file = "game_stat.txt"

file = open("results.txt", "w")
file.write(printing.print_count_games(data_file) + "\n")
file.write(printing.print_decide(data_file, 2004) + "\n")
file.write(printing.print_get_latest(data_file) + "\n")
file.write(printing.print_count_by_genre(data_file, "RPG") + "\n")
file.write(printing.print_get_line_number_by_title(data_file, "World of Warcraft") + "\n")
file.close()

# Export functions
