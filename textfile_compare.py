class TextFileCompare:
    def __init__(self, filename_A, filename_B):

        self.filename_A = filename_A
        self.filename_B = filename_B
        self.read_files_into_dicts()

    def read_files_into_dicts(self) -> None:
        # Read files to dictionary
        file_A = open(self.filename_A, "r")
        file_B = open(self.filename_B, "r")
        self.dict_A: dict = self.getWordCountsFromFile(file_A)
        file_A.close()
        self.dict_B: dict = self.getWordCountsFromFile(file_B)
        file_B.close()

    def getWordCountsFromFile(self, inputFile) -> dict:
        word_counts = {}
        line: str
        for line in inputFile:
            line = self.replacePunctuation(line)
            self.countWordsInLine(line.lower(), word_counts)  # pass wordCounts by reference
        return word_counts

    def countWordsInLine(self, line: str, word_counts: dict) -> None:
        """
        Processing word for word in a line
        If the word is not in word_counts it will be added as a key, with value 1
        If the word is already in word_count, the value will be increased by +1
        """

        words: list = line.split()  # Get words from each line
        for word in words:
            if word in word_counts:
                word_counts[word] += 1  # Increase count for word
            else:
                word_counts[word] = 1  # Add an item in the dictionary

    def replacePunctuation(self, line: str) -> str:
        for ch in line:
            if ch in "~@#$%^&*()_-+=~<>?/,.;:!{}[]|'\"":
                line = line.replace(ch, " ")
        return line

    def choose_dictionary(self, file_letter) -> dict:
        if file_letter == "A":
            return self.dict_A
        elif file_letter == "B":
            return self.dict_B

    def get_n_unique_words(self, file_letter) -> int:
        words_dict: dict = self.choose_dictionary(file_letter)
        n_unique_words: int = 0
        for i in words_dict:
            if words_dict[i] == 1:
                n_unique_words += 1
        return n_unique_words

    def get_unique_words(self, file_letter) -> list:
        words_dict: dict = self.choose_dictionary(file_letter)
        unique_words: list = []
        for i in words_dict:
            if words_dict[i] == 1:
                unique_words.append(i)
        return unique_words

    def get_unique_common_words(self) -> list:
        unique_common_list = []
        unique_list_A = self.get_unique_words("A")
        unique_list_B = self.get_unique_words("B")
        for word in unique_list_A:
            if word in unique_list_B:
                unique_common_list.append(word)
        return unique_common_list

    def get_unique_words_exclusive_to_file(self, file_letter) -> list:
        # er alle men hvis i unique common ikke ta med
        unique_exclusive_list = []
        unique_list_A = self.get_unique_words("A")
        unique_list_B = self.get_unique_words("B")
        if file_letter == "A":
            for word in unique_list_A:
                if word not in unique_list_B:
                    unique_exclusive_list.append(word)
        elif file_letter == "B":
            for word in unique_list_B:
                if word not in unique_list_A:
                    unique_exclusive_list.append(word)
        return unique_exclusive_list

    def get_unique_from_files_combined(self) -> list:
        unique_list_A = self.get_unique_words("A")
        unique_list_B = self.get_unique_words("B")
        unique_including_both = []

        for word in unique_list_A:
            if word not in unique_list_B:
                unique_including_both.append(word)

        for word in unique_list_B:
            if word not in unique_list_A and word not in unique_including_both:
                unique_including_both.append(word)

        return unique_including_both
