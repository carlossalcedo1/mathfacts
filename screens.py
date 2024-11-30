from main import screen_size
import pygame

#import user_class
pygame.init()
screen = pygame.display.set_mode(screen_size)

# variables
spacer = 50
# can use tuples because rectangles are never changing and can still loop through them lol, feel runtime acceleration
main_screen_rectangles = (
    (pygame.Rect((screen_size[0] - 350) // 2, 100 * 1 + spacer * 1, 350, 100)),
    (pygame.Rect((screen_size[0] - 350) // 2, 100 * 2 + spacer * 2, 350, 100)),
    (pygame.Rect((screen_size[0] - 350) // 2, 100 * 3 + spacer * 3, 350, 100)),
    (pygame.Rect((screen_size[0] - 350) // 2, 100 * 4 + spacer * 4, 350, 100))
)

main_screen_font = pygame.font.Font(None, 36)
main_screen_texts = (
    (main_screen_font.render("Math-Lingo, Select a Difficulty", True, "grey")),
    (main_screen_font.render("Easy", True, "black")),
    (main_screen_font.render("Medium", True, "black")),
    (main_screen_font.render("Hard", True, "black")),
    (main_screen_font.render("Settings", True, "black"))
)


# main2_screen_rectangles = (
#     (pygame.Rect((screen_size[0] - 350) // 2, 100 * 1 + spacer * 1, 350, 100)),
#     (pygame.Rect((screen_size[0] - 350) // 2, 100 * 2 + spacer * 2, 350, 100)),
#     (pygame.Rect((screen_size[0] - 350) // 2, 100 * 3 + spacer * 3, 350, 100)),
#     (pygame.Rect((screen_size[0] - 350) // 2, 100 * 4 + spacer * 4, 350, 100))
# )

main2_screen_font = pygame.font.Font(None, 72)
main2_screen_texts = (
    (main2_screen_font.render("+", True, "black")),
    (main2_screen_font.render("-", True, "black")),
    (main2_screen_font.render("X", True, "black")),
    (main2_screen_font.render("/", True, "black")),
    (main_screen_font.render("Select an Operation", True, "grey"))
)

run_button = pygame.Rect((screen_size[0] - 350) // 2, 100 * 4 + spacer * 4, 350, 100)
game_screen_font = pygame.font.Font(None, 84)



def main_screen(rectangles: tuple, texts: tuple):
    screen.fill("white")

    pygame.draw.rect(screen, "green", rectangles[0])
    pygame.draw.rect(screen, "yellow", rectangles[1])
    pygame.draw.rect(screen, "red", rectangles[2])
    pygame.draw.rect(screen, "grey", rectangles[3])
    # screen.blit(),
    screen.blit(texts[0], (100, 80))
    screen.blit(texts[1], texts[1].get_rect(center=rectangles[0].center))
    screen.blit(texts[2], texts[2].get_rect(center=rectangles[1].center))
    screen.blit(texts[3], texts[3].get_rect(center=rectangles[2].center))
    screen.blit(texts[4], texts[4].get_rect(center=rectangles[3].center))

def main2_screen(rectangles: tuple, texts: tuple):
    screen.fill("white")
    pygame.draw.rect(screen, "green", rectangles[0])
    pygame.draw.rect(screen, "yellow", rectangles[1])
    pygame.draw.rect(screen, "red", rectangles[2])
    pygame.draw.rect(screen, "grey", rectangles[3])

    screen.blit(texts[0], texts[0].get_rect(center=rectangles[0].center))
    screen.blit(texts[1], texts[1].get_rect(center=rectangles[1].center))
    screen.blit(texts[2], texts[2].get_rect(center=rectangles[2].center))
    screen.blit(texts[3], texts[3].get_rect(center=rectangles[3].center))
    screen.blit(texts[4], (100, 80))


def settings_screen(timer_sel: int):
    screen.fill("white")

    setting_screen_texts = (
        (game_screen_font.render(f"Settings Page (Click to Change)", True, "black")),
        (main_screen_font.render(f"Timer Selected: {timer_sel} seconds", True, "black")),
        (main_screen_font.render(f"---", True, "black")),
        (main_screen_font.render(f"View Stat Trends", True, "black")),
        (main_screen_font.render("Back", True, "black"))


    )
    pygame.draw.rect(screen, "green", main_screen_rectangles[0])
    pygame.draw.rect(screen, "yellow", main_screen_rectangles[1])
    pygame.draw.rect(screen, "red", main_screen_rectangles[2])
    pygame.draw.rect(screen, "grey", main_screen_rectangles[3])


    screen.blit(setting_screen_texts[0], (200, 60))
    screen.blit(setting_screen_texts[1], setting_screen_texts[1].get_rect(center=main_screen_rectangles[0].center))
    screen.blit(setting_screen_texts[2], setting_screen_texts[2].get_rect(center=main_screen_rectangles[1].center))
    screen.blit(setting_screen_texts[3], setting_screen_texts[3].get_rect(center=main_screen_rectangles[2].center))
    screen.blit(setting_screen_texts[4], setting_screen_texts[4].get_rect(center=main_screen_rectangles[3].center))

def game_screen(operands: tuple, operator: int, answer: str, streak: int, total_solved: int, temp_solved: int, timer: int, rank_by_name: str):
    screen.fill("white")
    operator_dict = {1: "+", 2: "-", 3: "X", 4: "/"}
    game_screen_texts = (
        (game_screen_font.render(str(operands[0]), True, "black")),
        (game_screen_font.render(str(operands[1]), True, "black")),
        (game_screen_font.render(operator_dict[operator], True, "black")),
        (game_screen_font.render("--------", True, "black")),
        (game_screen_font.render(answer, True, "black")),
        (game_screen_font.render(f"Total Solved: {total_solved}", True, "black")),
        (game_screen_font.render(f"Timer: {timer}", True, "black")),
        (game_screen_font.render(f"Streak: {streak}", True, "black")),
        (game_screen_font.render(f"Solved: {temp_solved}", True, "black")),
        (game_screen_font.render(f"Rank: {rank_by_name}", True, "black")),
        (game_screen_font.render("Exit", True, "black"))
    )
    pygame.draw.rect(screen, "grey", run_button)

    screen.blit(game_screen_texts[0], (screen_size[0]//2, (screen_size[1] -250)//2))
    #if easy mode or hard mode draw 50 pixels to the left so it's aligned with the left number
    if len(str(operands[1])) == 1:
        screen.blit(game_screen_texts[1], ((screen_size[0] + 75)//2, (screen_size[1] -100)//2))
    else:
        screen.blit(game_screen_texts[1], (screen_size[0] // 2, (screen_size[1] - 100) // 2))

    #operator symbol and line under
    screen.blit(game_screen_texts[2], ((screen_size[0] - 75)//2, (screen_size[1] -100)//2))
    screen.blit(game_screen_texts[3], ((screen_size[0] - 150)//2, (screen_size[1] - 25)//2))

    #answer, show "correct" if correct answer
    screen.blit(game_screen_texts[4], ((screen_size[0] - 100) // 2, (screen_size[1]) // 2 + 50))

    #display streak and time and solved and total puzzles_solved
    screen.blit(game_screen_texts[5], ((screen_size[0] - 500) // 6, (screen_size[1] - 400) // 2))
    screen.blit(game_screen_texts[6], ((screen_size[0] - 500) // 6, (screen_size[1] - 250) // 2))
    screen.blit(game_screen_texts[7], ((screen_size[0] - 500) // 6, (screen_size[1] - 100) // 2))
    screen.blit(game_screen_texts[8], ((screen_size[0] - 500) // 6, (screen_size[1] +50) // 2))
    screen.blit(game_screen_texts[9], ((screen_size[0] - 500) // 6, (screen_size[1] + 200) // 2))

    #exit button
    screen.blit(game_screen_texts[10], game_screen_texts[10].get_rect(center=run_button.center))


def game_over(streak: int, solved: int, total_time: int):
    screen.fill("white")
    end_screen_texts = (
        (game_screen_font.render("Game Over!", True, "black")),
        (main_screen_font.render(f"You solved {solved} with a streak of {streak} in {total_time} seconds.", True, "black")),
        (main_screen_font.render("Restart", True, "black"))
    )
    pygame.draw.rect(screen, "grey", run_button)

    screen.blit(end_screen_texts[0], ((screen_size[0] - 250) // 2, (screen_size[1] - 400) // 2))
    screen.blit(end_screen_texts[1], ((screen_size[0] - 250) // 2, (screen_size[1] - 250) // 2))
    screen.blit(end_screen_texts[2], end_screen_texts[2].get_rect(center=run_button.center))