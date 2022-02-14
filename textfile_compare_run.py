from textfile_compare import TextFileCompare
from textfile_compare_menu import TextFileCompareMenu

if __name__ == '__main__':
    file_a = "godfather_part1.txt"
    file_b = "godfather_part2.txt"
    menu_choice = TextFileCompareMenu.get_menu_choice(file_a, file_b)
    textfile_compare = TextFileCompare
