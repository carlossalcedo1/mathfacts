import random

class Event:
    def __init__(self, state:str):
        self.state: str = state
        self.temp_solved: int = 0
        self.streak: int = 0

        self.input_answer = ""
        self.operator = 0
        self.difficulty = 0  # 1easy,2medium,3hard
        self.operands = ()
        self.current_time = 0

    #the user input methods


    def set_input(self, value):
        self.input_answer = value
        return self.input_answer

    def append_input(self, value:str):
        self.input_answer += value
        return self.input_answer

    def delete_input_character(self):
        self.input_answer = self.input_answer[0:len(self.input_answer)-1]

    def reset_input(self):
        self.input_answer = ""

    #operator 1 for adding, 2 for subtracting, 3 for multiplication, 4 for division
    def set_operator(self, value):
        self.operator = value
        return self.operator

    def set_operands(self, value1: int, value2: int):
        self.operands = (value1, value2)
        return self.operands

    def decrement_time(self):
        self.current_time -= 1/60

    def set_state(self, value):
        self.state = value

    def increment_streak(self) -> int:
        self.streak += 1
        return self.streak

    def reset_streak(self) -> int:
        self.streak = 0
        return self.streak

    def reset(self, set_time: int):
        self.state = "menu"
        self.input_answer = ""
        self.operands = ()
        self.current_time = set_time
        self.difficulty = 0
        self.temp_solved = 0
        self.streak = 0


    def operand_randomizer(self):
        if self.difficulty == 1:
            self.operands = (random.randint(10,99), random.randint(1,9))
        elif self.difficulty == 2:
            self.operands = (random.randint(10,99), random.randint(10,99))
            if self.operands[0] < self.operands[1]:
                self.operands = (self.operands[0] + self.operands[1] - random.randint(0, 15), self.operands[1])
        elif self.difficulty == 3:
            self.operands = (random.randint(100,999), random.randint(100,999))