import random
import string

class WordSearch:
    def __init__(self, size=15, num_words=10):
        self.size = size
        self.num_words = num_words
        self.grid = [[' ' for _ in range(size)] for _ in range(size)]
        self.words = []

    def generate(self, word_list):
        self.words = random.sample(word_list, self.num_words)
        self.place_words()

        self.fill_remaining()

    def place_words(self):
        directions = [(1, 0), (0, 1), (1, 1), (-1, 1)]  # Right, Down, Diagonal Right, Diagonal Left
        for word in self.words:
            placed = False
            while not placed:
                direction = random.choice(directions)
                start_row = random.randint(0, self.size - 1)
                start_col = random.randint(0, self.size - 1)

                end_row = start_row + len(word) * direction[0]
                end_col = start_col + len(word) * direction[1]

                if 0 <= end_row < self.size and 0 <= end_col < self.size:
                    valid_placement = True
                    for i in range(len(word)):
                        row = start_row + i * direction[0]
                        col = start_col + i * direction[1]
                        if self.grid[row][col] != ' ':
                            valid_placement = False
                            break
                    if valid_placement:
                        for i in range(len(word)):
                            row = start_row + i * direction[0]
                            col = start_col + i * direction[1]
                            self.grid[row][col] = word[i]
                        placed = True

    def fill_remaining(self):
        letters = string.ascii_uppercase
        for i in range(self.size):
            for j in range(self.size):
                if self.grid[i][j] == ' ':
                    self.grid[i][j] = random.choice(letters)

    def display(self):
        for row in self.grid:
            print(' '.join(row))