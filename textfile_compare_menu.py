import logging
from textfile_compare import TextFileCompare

logging.basicConfig(level=logging.DEBUG)


class TextFileCompareMenu:
    def __init__(self, filename_a, filename_b):
        self.filename_a = filename_a
        self.filename_b = filename_b

    def print_pretty_list(self, list):
        i = 0
        list.sort()
        for word in list:
            print(word, "", end="")
            i += 1
            if i % 10 == 0:
                print("\n")
        print("\n")

    def print_menu(self):
        print()
        print('        MENU')
        print('1) Number of unique words in file A')
        print('2) Number of unique words in file B')
        print('3) Display unique words in file A')
        print('4) Display unique words in file B')
        print('5) Unique words from each file that appear in BOTH files')
        print('6) Unique words exclusive to A')
        print('7) Unique words exclusive to B')
        print('8) Unique words of files combined')
        print('9) Quit')

    def get_menu_choice(self, filename_a, filename_b, textfile_compare):
        self.textfile_compare = textfile_compare
        N_UNIQUE_WORDS_IN_FILE_A = 1
        N_UNIQUE_WORDS_IN_FILE_B = 2
        UNIQUE_WORDS_IN_FILE_A = 3
        UNIQUE_WORDS_IN_FILE_B = 4
        UNIQUE_WORDS_FROM_EACH_FILE_THAT_APPEAR_IN_BOTH_FILES = 5
        UNIQUE_WORDS_EXCLUSIVE_TO_A = 6
        UNIQUE_WORDS_EXCLUSIVE_TO_B = 7
        UNIQUE_WORDS_IN_EITHER_FILE_EXCEPT_COMMON_WORDS = 8
        QUIT_CHOICE = 9
        self.menu_choices_list = [UNIQUE_WORDS_IN_FILE_A, UNIQUE_WORDS_IN_FILE_B, N_UNIQUE_WORDS_IN_FILE_A,
                                  N_UNIQUE_WORDS_IN_FILE_B, UNIQUE_WORDS_FROM_EACH_FILE_THAT_APPEAR_IN_BOTH_FILES,
                                  UNIQUE_WORDS_EXCLUSIVE_TO_A, UNIQUE_WORDS_EXCLUSIVE_TO_B,
                                  UNIQUE_WORDS_IN_EITHER_FILE_EXCEPT_COMMON_WORDS, QUIT_CHOICE]

        choice: int = 0
        while choice != QUIT_CHOICE:
            while True:
                self.print_menu()
                try:
                    choice = int(input('Enter your choice: '))
                    if choice in self.menu_choices_list:
                        print()  # adds line for separation
                        break
                    else:
                        print(f"{choice} is not a choice in menu")
                        print("Try again!")
                        continue
                except ValueError:
                    print("You did not entered an integerer.")
                    print("Try again!")
                    continue

            if choice == N_UNIQUE_WORDS_IN_FILE_A:
                print(f"""Number of unique words in {filename_a}: {textfile_compare.get_n_unique_words("A")}""")
            elif choice == N_UNIQUE_WORDS_IN_FILE_B:
                print(f"""Number of unique words in {filename_b}: {textfile_compare.get_n_unique_words("B")}""")
            elif choice == UNIQUE_WORDS_IN_FILE_A:
                self.print_pretty_list(textfile_compare.get_unique_words("A"))
            elif choice == UNIQUE_WORDS_IN_FILE_B:
                self.print_pretty_list(textfile_compare.get_unique_words("B"))
            elif choice == UNIQUE_WORDS_FROM_EACH_FILE_THAT_APPEAR_IN_BOTH_FILES:
                self.print_pretty_list(textfile_compare.get_unique_common_words())
            elif choice == UNIQUE_WORDS_EXCLUSIVE_TO_A:
                self.print_pretty_list(textfile_compare.get_unique_words_exclusive_to_file("A"))
            elif choice == UNIQUE_WORDS_EXCLUSIVE_TO_B:
                self.print_pretty_list(textfile_compare.get_unique_words_exclusive_to_file("B"))
            elif choice == UNIQUE_WORDS_IN_EITHER_FILE_EXCEPT_COMMON_WORDS:
                self.print_pretty_list(textfile_compare.get_unique_from_files_combined())
