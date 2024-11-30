import json

class User:
    def __init__(self, name: str, puzzles_solved: int, rank: int, settings_time: int):

        self.name = name
        self.rank = rank
        self.difficulty = 0  # 1easy,2medium,3hard
        self._puzzles_solved = puzzles_solved
        self._easy_solved = 0
        self._medium_solved = 0
        self._hard_solved = 0
        self.settings_time = settings_time
        self.rank_names = {
            0: "Noob",
            1: "Noob+",
            2: "Experienced"
        }

    def __str__(self):
        return f"Name: {self.name}, Puzzles_solved: {self._puzzles_solved}, Rank: {self.rank}, Rank as name: {self.rank_names[self.rank]}"

    @property
    def get_puzzles_solved(self):
        return self._puzzles_solved

    @property
    def get_easy_solved(self):
        return self._easy_solved

    @property
    def get_medium_solved(self):
        return self._medium_solved

    @property
    def get_hard_solved(self):
        return self._hard_solved


    def increment_solved(self):
        if self.difficulty == 0:
            return "Not set"
        elif self.difficulty == 1:
            self._puzzles_solved += 1
            self._easy_solved += 1

        elif self.difficulty == 2:
            self._puzzles_solved += 1
            self._medium_solved += 1

        elif self.difficulty == 3:
            self._puzzles_solved += 1
            self._hard_solved += 1

        return self._puzzles_solved

    def rank_upgrade(self) -> bool:
        if self._puzzles_solved % 100 == 0:
            self.rank += 1
            return True
        return False

    def rank_name(self):
        return self.rank_names[self.rank]

    def time_set(self):
        if self.settings_time > 5:
            self.settings_time = 1
        else:
            self.settings_time += 1



def save_data(person) -> bool:
    #person is an object, of class Profile [person.name, person.id, person.level, person.get_cookie_clicks]
    with open('data.json', 'r') as file:
        data = json.load(file)
    for profile in data:
        if profile.get("name") == person.name:
            index = data.index(profile)
            profile["attributes"]["rank"] += person.rank
            profile["attributes"]["time_select"] = person.settings_time
            profile["attributes"]["puzzles_solved"] = person.get_puzzles_solved
            profile["attributes"]["easy_solved"] += person.get_easy_solved
            profile["attributes"]["medium_solved"] += person.get_medium_solved
            profile["attributes"]["hard_solved"] += person.get_hard_solved
            data[index] = profile
            with open('data.json', 'w') as file:
                json.dump(data, file, indent=4)
            print(f"Saved user profile {person.name}")
            return True
    return False