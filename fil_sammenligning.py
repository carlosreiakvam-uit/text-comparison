import logging

logging.basicConfig(level=logging.DEBUG)


class TextFileCompare:
    def __init__(self):
        self.filename_A = "godfather_part1.txt"
        filename_B = "godfather_part2.txt"
        file_a = open(self.filename_A, "r")  # Open the file
        file_b = open(filename_B, "r")  # Open the file
        dict_a: dict = self.getWordCountsFromFile(file_a)
        dict_b: dict = self.getWordCountsFromFile(file_b)
        file_a.close()
        file_b.close()

        UNIQUE_WORDS_IN_FILE_A = 1
        UNIQUE_WORDS_IN_FILE_B = 2
        N_UNIQUE_WORDS_IN_FILE_A = 3
        N_UNIQUE_WORDS_IN_FILE_B = 4
        UNIQUE_COMMON_WORDS = 5
        UNIQUE_WORDS_EXCLUSIVE_TO_A = 6
        UNIQUE_WORDS_EXCLUSIVE_TO_B = 7
        UNIQUE_WORDS_IN_EITHER_FILE_EXCEPT_COMMON_WORDS = 8
        QUIT_CHOICE = 9
        menu_choices_list = [UNIQUE_WORDS_IN_FILE_A, UNIQUE_WORDS_IN_FILE_B, N_UNIQUE_WORDS_IN_FILE_A,
                             N_UNIQUE_WORDS_IN_FILE_B, UNIQUE_COMMON_WORDS,
                             UNIQUE_WORDS_EXCLUSIVE_TO_A, UNIQUE_WORDS_EXCLUSIVE_TO_B,
                             UNIQUE_WORDS_IN_EITHER_FILE_EXCEPT_COMMON_WORDS, QUIT_CHOICE]

        choice: int = 0

        # PERFOMR MENU CHOICE
        while choice != QUIT_CHOICE:
            while True:
                self.print_menu()
                try:
                    choice = int(input('Enter your choice: '))
                    if choice in menu_choices_list:
                        break
                    else:
                        print(f"{choice} is not a choice in menu")
                        print("Try again!")
                        continue
                except ValueError:
                    print("You did not entered an integerer.")
                    print("Try again!")
                    continue

            if choice == UNIQUE_WORDS_IN_FILE_A:
                print(f"Number of unique words in {filename_A}: {self.get_n_unique_words(dict_a)}")
            elif choice == UNIQUE_WORDS_IN_FILE_B:
                print(f"Number of unique words in {filename_B}: {self.get_n_unique_words(dict_b)}")
            elif choice == N_UNIQUE_WORDS_IN_FILE_A:
                print(f"Unique words in {filename_A}: {self.get_unique_words(dict_a)}")
            elif choice == N_UNIQUE_WORDS_IN_FILE_B:
                print(f"Unique words in {filename_B}: {self.get_unique_words(dict_b)}")
            elif choice == UNIQUE_COMMON_WORDS:
                print(f"Unique common words: {self.get_unique_common_words(dict_a, dict_b)}")
            elif choice == UNIQUE_WORDS_EXCLUSIVE_TO_A:
                print(f"Unique words exclusive to A: {self.get_unique_words_exclusive_to_A(dict_a, dict_b)}")
            elif choice == UNIQUE_WORDS_EXCLUSIVE_TO_B:
                print(f"Unique words exclusive to B: {self.get_unique_words_exclusive_to_B(dict_a, dict_b)}")
            elif choice == UNIQUE_WORDS_IN_EITHER_FILE_EXCEPT_COMMON_WORDS:
                print(
                    f"Unique words in either file except common words: {self.get_unique_words_exclusive_to_B(dict_a, dict_b)}")

    def print_menu(self):
        print('        MENU')
        print('1) Number of unique words in file A')
        print('2) Number of unique words in file B')
        print('3) Display unique words in file A')
        print('4) Display unique words in file B')
        print('5) Unique common words')
        print('6) Unique words exclusive to A')
        print('7) Unique words exclusive to B')
        print('8) Unique words in either file except common words')
        print('9) Quit')

    def getWordCountsFromFile(self, inputFile):
        wordCounts = {}  # Create an empty dictionary to count words
        for line in inputFile:
            countWordsInLine(line.lower(), wordCounts)  # pass wordCounts by reference
        return wordCounts

    def print_first_x_from_list(self, items, x: int):
        for count, word in items[: x]:  # Slice the first 10 items
            print(word, count, sep='\t')

    def getListOfPairsFromDict(self, wordCounts):
        listFromDict: list = list(wordCounts.items())  # Get pairs from dictionary as a list
        return listFromDict

    def readFile(self):
        pass

    def get_n_unique_words(self, dictionary: dict) -> int:
        n_unique_words: int = 0
        for i in dictionary:
            if dictionary[i] == 1:
                n_unique_words += 1
        return n_unique_words

    def get_unique_words(self, dictionary: dict) -> list:
        n_unique_words: list = []
        for i in dictionary:
            if dictionary[i] == 1:
                n_unique_words.append(i)
        return n_unique_words

    def get_unique_common_words(self, dict_a, dict_b):
        pass

    def get_unique_words_exclusive_to_A(self, dict_a, dict_b):
        pass

    def get_unique_words_exclusive_to_B(self, dict_a, dict_b):
        pass

    def get_unique_words_from_either_except_ommon_words(self, dict_a, dict_b):
        pass


def countWordsInLine(line, wordCounts: dict):
    """
    Metoden prosseserer ord for ord i en linje
    Hvis ordet ikke eksisterer som key i dictionary wordCounts fra før, legges det til med verdien 1.
    Hvis ordet derimot eksisterer som key fra før, adderes 1 til verdien som tidligere var assiosert med gitt key
    """
    words = line.split()  # Get words from each line
    for word in words:
        if word in wordCounts:
            wordCounts[word] += 1  # Increase count for word
        else:
            wordCounts[word] = 1  # Add an item in the dictionary


def replacePunctuation(line):
    """Metoden erstatter eventuelle tegn i en linje med space"""
    for ch in line:
        if ch in "~@#$%^&*()_-+=~<>?/,.;:!{}[]|'\"":
            line = line.replace(ch, " ")

    return line


if __name__ == '__main__':
    TextFileCompare()
