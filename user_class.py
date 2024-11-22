class User:
    def __init__(self, name: str, puzzles_solved: int, rank: str, streak: int):

        self.name = name
        self.puzzles_solved = puzzles_solved
        self.rank = rank
        self.streak = streak
        difficulty = 0
        easy_solved = 0
        medium_solved = 0
        hard_solved = 0

    def __str__(self):
        return f"Name: {self.name}, Puzzles_solved: {self.puzzles_solved}, Rank: {self.rank}, Streak: {self.streak}"