import pygame
import sys
import random

# =========================
# INITIALIZE
# =========================
pygame.init()
pygame.mixer.init()

clock = pygame.time.Clock()

# =========================
# WINDOW
# =========================
WIDTH = 1280
HEIGHT = 720

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Finish The Lyrics!")

# =========================
# BACKGROUND
# =========================
background = pygame.image.load("background.jpg")
background = pygame.transform.smoothscale(background, (WIDTH, HEIGHT))

pop_bg = pygame.image.load("pop_bg.jpg")
pop_bg = pygame.transform.smoothscale(pop_bg, (WIDTH, HEIGHT))

bollywood_bg = pygame.image.load("bolly_bg.jpg")
bollywood_bg = pygame.transform.smoothscale(bollywood_bg, (WIDTH, HEIGHT))

rhymes_bg = pygame.image.load("rhyme_bg.jpg")
rhymes_bg = pygame.transform.smoothscale(rhymes_bg, (WIDTH, HEIGHT))

# =========================
# CATEGORY IMAGES
# =========================
pop_image = pygame.image.load("pop.jpg")
pop_image = pygame.transform.smoothscale(pop_image, (220, 220))

bollywood_image = pygame.image.load("bolly.jpg")
bollywood_image = pygame.transform.smoothscale(bollywood_image, (220, 220))

rhymes_image = pygame.image.load("rhyme.jpg")
rhymes_image = pygame.transform.smoothscale(rhymes_image, (220, 220))

# =========================
# ICONS
# =========================
hint_icon = pygame.image.load("bulb.png")
hint_icon = pygame.transform.smoothscale(hint_icon, (35, 35))

# SKULL IMAGE
skull_image = pygame.image.load("skull.png")
skull_image = pygame.transform.smoothscale(skull_image, (140, 140))

# WIN IMAGE
win_image = pygame.image.load("star.png")
win_image = pygame.transform.smoothscale(win_image, (180, 180))

# =========================
# BACKGROUND MUSIC
# =========================
pygame.mixer.music.load("sounds/bg_score.mp3")
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1)

# =========================
# BUTTON CLICK SOUND
# =========================
click_sound = pygame.mixer.Sound("sounds/button.mp3")
click_sound.set_volume(0.2)

# =========================
# CORRECT SOUND
# =========================
correct_sound = pygame.mixer.Sound("sounds/right.mp3")
correct_sound.set_volume(0.2)

# =========================
# WRONG SOUND
# =========================
wrong_sound = pygame.mixer.Sound("sounds/wrong.mp3")
wrong_sound.set_volume(0.2)

# =========================
# LEVEL UP SOUND
# =========================
levelup_sound = pygame.mixer.Sound("sounds/level_up.mp3")
levelup_sound.set_volume(0.2)

# =========================
# COLORS
# =========================
WHITE = (255, 255, 255)
LILAC = (224, 170, 255)
DARK_PURPLE = (16, 0, 43)
GREEN = (30, 215, 96)
RED = (255, 80, 80)

# =========================
# FONTS
# =========================
title_font = pygame.font.SysFont("Helvetica", 72)
subtitle_font = pygame.font.SysFont("Helvetica", 36)
button_font = pygame.font.SysFont("Helvetica", 40)
body_font = pygame.font.SysFont("Helvetica", 28)

# =========================
# GAME STATE
# =========================
game_state = "menu"

selected_category = ""

question = ""
correct_answer = ""

user_text = ""

message = ""
message_color = WHITE

score = 0
lives = 3

hint_used = False

question_count = 0
max_questions = 5

game_result = ""

# =========================
# LOAD QUESTIONS FROM TXT
# =========================
def load_questions(filename):

    questions = []

    file = open(filename, "r")

    for line in file:

        question, answer = line.strip().split("|")

        questions.append((question, answer))

    file.close()

    return questions

# =========================
# ORIGINAL QUESTIONS
# =========================
original_pop_questions = load_questions("pop.txt")
original_bollywood_questions = load_questions("bollywood.txt")
original_rhymes_questions = load_questions("rhymes.txt")

# =========================
# WORKING COPIES
# =========================
pop_questions = original_pop_questions.copy()
bollywood_questions = original_bollywood_questions.copy()
rhymes_questions = original_rhymes_questions.copy()

# =========================
# BUTTONS
# =========================
start_button = pygame.Rect(440, 420, 400, 85)

next_button = pygame.Rect(500, 560, 280, 70)

home_button = pygame.Rect(1080, 40, 150, 55)

# CATEGORY BOXES
pop_rect = pygame.Rect(120, 220, 220, 220)
bollywood_rect = pygame.Rect(530, 220, 220, 220)
rhymes_rect = pygame.Rect(940, 220, 220, 220)

# =========================
# LOAD QUESTION
# =========================
def load_question():

    global question
    global correct_answer
    global hint_used

    hint_used = False

    random_question = None

    if selected_category == "POP":

        if len(pop_questions) > 0:

            random_question = random.choice(pop_questions)

            pop_questions.remove(random_question)

    elif selected_category == "BOLLYWOOD":

        if len(bollywood_questions) > 0:

            random_question = random.choice(bollywood_questions)

            bollywood_questions.remove(random_question)

    elif selected_category == "RHYMES":

        if len(rhymes_questions) > 0:

            random_question = random.choice(rhymes_questions)

            rhymes_questions.remove(random_question)

    if random_question:

        question = random_question[0]
        correct_answer = random_question[1]

# =========================
# RESET QUESTIONS
# =========================
def reset_questions():

    global pop_questions
    global bollywood_questions
    global rhymes_questions

    pop_questions = original_pop_questions.copy()
    bollywood_questions = original_bollywood_questions.copy()
    rhymes_questions = original_rhymes_questions.copy()

# =========================
# GAME LOOP
# =========================
running = True

while running:

    # DYNAMIC BACKGROUND
    if game_state == "game":
        if selected_category == "POP":
            screen.blit(pop_bg, (0, 0))

        elif selected_category == "BOLLYWOOD":
            screen.blit(bollywood_bg, (0, 0))

        elif selected_category == "RHYMES":
            screen.blit(rhymes_bg, (0, 0))

        else:
            screen.blit(background, (0, 0))

    else:
        screen.blit(background, (0, 0))

    # ==================================================
    # MENU SCREEN
    # ==================================================
    if game_state == "menu":

        title = title_font.render(
            "FINISH THE LYRICS",
            True,
            WHITE
        )

        title_rect = title.get_rect(
            center=(WIDTH // 2, 170)
        )

        screen.blit(title, title_rect)

        subtitle = subtitle_font.render(
            "Complete the lyrics!",
            True,
            LILAC
        )

        subtitle_rect = subtitle.get_rect(
            center=(WIDTH // 2, 280)
        )

        screen.blit(subtitle, subtitle_rect)

        pygame.draw.rect(
            screen,
            DARK_PURPLE,
            start_button,
            border_radius=50
        )

        start_text = button_font.render(
            "START GAME",
            True,
            WHITE
        )

        start_rect = start_text.get_rect(
            center=start_button.center
        )

        screen.blit(start_text, start_rect)

    # ==================================================
    # CATEGORY SCREEN
    # ==================================================
    elif game_state == "category":

        category_title = title_font.render(
            "SELECT CATEGORY",
            True,
            WHITE
        )

        category_title_rect = category_title.get_rect(
            center=(WIDTH // 2, 120)
        )

        screen.blit(category_title, category_title_rect)

        # POP
        pygame.draw.rect(
            screen,
            WHITE,
            pop_rect,
            width=2,
            border_radius=20
        )

        screen.blit(pop_image, pop_rect)

        pop_text = subtitle_font.render(
            "POP",
            True,
            WHITE
        )

        pop_text_rect = pop_text.get_rect(
            center=(230, 480)
        )

        screen.blit(pop_text, pop_text_rect)

        # BOLLYWOOD
        pygame.draw.rect(
            screen,
            WHITE,
            bollywood_rect,
            width=2,
            border_radius=20
        )

        screen.blit(bollywood_image, bollywood_rect)

        bollywood_text = subtitle_font.render(
            "BOLLYWOOD",
            True,
            WHITE
        )

        bollywood_text_rect = bollywood_text.get_rect(
            center=(640, 480)
        )

        screen.blit(bollywood_text, bollywood_text_rect)

        # RHYMES
        pygame.draw.rect(
            screen,
            WHITE,
            rhymes_rect,
            width=2,
            border_radius=20
        )

        screen.blit(rhymes_image, rhymes_rect)

        rhymes_text = subtitle_font.render(
            "RHYMES",
            True,
            WHITE
        )

        rhymes_text_rect = rhymes_text.get_rect(
            center=(1050, 480)
        )

        screen.blit(rhymes_text, rhymes_text_rect)

    # ==================================================
    # GAME SCREEN
    # ==================================================
    elif game_state == "game":

        # SCORE
        score_text = body_font.render(
            f"Score: {score}",
            True,
            WHITE
        )

        screen.blit(score_text, (50, 35))

        # LIVES
        lives_text = body_font.render(
            f"Lives: {lives}",
            True,
            WHITE
        )

        screen.blit(lives_text, (50, 70))

        # QUESTION COUNT
        count_text = body_font.render(
            f"Question: {question_count}/{max_questions}",
            True,
            WHITE
        )

        screen.blit(count_text, (50, 105))

        # HINT ICON
        screen.blit(hint_icon, (490, 669))

        # HINT TEXT
        hint_text = body_font.render(
            "Press SHIFT for Hint",
            True,
            WHITE
        )

        screen.blit(hint_text, (540, 673))

        # HOME BUTTON
        pygame.draw.rect(
            screen,
            DARK_PURPLE,
            home_button,
            border_radius=30
        )

        pygame.draw.rect(
            screen,
            WHITE,
            home_button,
            width=2,
            border_radius=30
        )

        home_text = body_font.render(
            "HOME",
            True,
            WHITE
        )

        home_rect = home_text.get_rect(
            center=home_button.center
        )

        screen.blit(home_text, home_rect)

        # CATEGORY NAME
        category_name = subtitle_font.render(
            selected_category,
            True,
            LILAC
        )

        category_rect = category_name.get_rect(
            center=(WIDTH // 2, 120)
        )

        screen.blit(category_name, category_rect)

        # QUESTION
        question_text = subtitle_font.render(
            question,
            True,
            WHITE
        )

        question_rect = question_text.get_rect(
            center=(WIDTH // 2, 260)
        )

        screen.blit(question_text, question_rect)

        # INPUT BOX
        input_rect = pygame.Rect(
            WIDTH // 2 - 250,
            340,
            500,
            90
        )

        pygame.draw.rect(
            screen,
            DARK_PURPLE,
            input_rect,
            border_radius=50
        )

        pygame.draw.rect(
            screen,
            WHITE,
            input_rect,
            width=3,
            border_radius=50
        )

        answer_surface = subtitle_font.render(
            user_text,
            True,
            WHITE
        )

        answer_rect = answer_surface.get_rect(
            center=input_rect.center
        )

        screen.blit(answer_surface, answer_rect)

        # RESULT MESSAGE
        if message != "":

            result_text = subtitle_font.render(
                message,
                True,
                message_color
            )

            result_rect = result_text.get_rect(
                center=(WIDTH // 2, 490)
            )

            screen.blit(result_text, result_rect)

        # HINT DISPLAY
        if hint_used and message == "":

            hint_display = body_font.render(
                f"Hint: Starts with '{correct_answer[0]}'",
                True,
                LILAC
            )

            hint_display_rect = hint_display.get_rect(
                center=(WIDTH // 2, 530)
            )

            screen.blit(hint_display, hint_display_rect)

        # NEXT BUTTON
        if message != "":

            pygame.draw.rect(
                screen,
                DARK_PURPLE,
                next_button,
                border_radius=40
            )

            pygame.draw.rect(
                screen,
                WHITE,
                next_button,
                width=2,
                border_radius=40
            )

            next_text = button_font.render(
                "NEXT",
                True,
                WHITE
            )

            next_rect = next_text.get_rect(
                center=next_button.center
            )

            screen.blit(next_text, next_rect)

    # ==================================================
    # RESULT SCREEN
    # ==================================================
    elif game_state == "result":

        result_title = title_font.render(
            "GAME OVER",
            True,
            WHITE
        )

        result_title_rect = result_title.get_rect(
            center=(WIDTH // 2, 170)
        )

        # RESULT IMAGE
        if game_result == "lose":
            screen.blit(skull_image, (WIDTH // 2 - 70, 150))
        else:
            screen.blit(win_image, (WIDTH // 2 - 90, 140))

        final_score = subtitle_font.render(
            f"Final Score: {score}",
            True,
            LILAC
        )

        final_score_rect = final_score.get_rect(
            center=(WIDTH // 2, 360)
        )

        screen.blit(final_score, final_score_rect)

        # PERFORMANCE RATING
        if score >= 40:

            rating = "Lyric Legend!"

        elif score >= 20:

            rating = "Music Master!"

        elif score >= 10:

            rating = "Casual Singer!"

        else:

            rating = "Karaoke Beginner!"

        rating_text = subtitle_font.render(
            rating,
            True,
            WHITE
        )

        rating_rect = rating_text.get_rect(
            center=(WIDTH // 2, 440)
        )

        screen.blit(rating_text, rating_rect)

        # PLAY AGAIN BUTTON
        play_again_button = pygame.Rect(
            WIDTH // 2 - 170,
            520,
            340,
            80
        )

        pygame.draw.rect(
            screen,
            DARK_PURPLE,
            play_again_button,
            border_radius=40
        )

        pygame.draw.rect(
            screen,
            WHITE,
            play_again_button,
            width=2,
            border_radius=40
        )

        play_again_text = button_font.render(
            "PLAY AGAIN",
            True,
            WHITE
        )

        play_again_rect = play_again_text.get_rect(
            center=play_again_button.center
        )

        screen.blit(play_again_text, play_again_rect)

    # ==================================================
    # EVENTS
    # ==================================================
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        # MOUSE CLICK
        if event.type == pygame.MOUSEBUTTONDOWN:

            # MENU
            if game_state == "menu":

                if start_button.collidepoint(event.pos):

                    click_sound.stop()
                    click_sound.play()

                    game_state = "category"

            # CATEGORY
            elif game_state == "category":

                reset_questions()

                # POP
                if pop_rect.collidepoint(event.pos):

                    click_sound.stop()
                    click_sound.play()

                    selected_category = "POP"

                    score = 0
                    lives = 3
                    question_count = 0

                    load_question()

                    user_text = ""
                    message = ""

                    game_state = "game"

                # BOLLYWOOD
                elif bollywood_rect.collidepoint(event.pos):

                    click_sound.stop()
                    click_sound.play()

                    selected_category = "BOLLYWOOD"

                    score = 0
                    lives = 3
                    question_count = 0

                    load_question()

                    user_text = ""
                    message = ""

                    game_state = "game"

                # RHYMES
                elif rhymes_rect.collidepoint(event.pos):

                    click_sound.stop()
                    click_sound.play()

                    selected_category = "RHYMES"

                    score = 0
                    lives = 3
                    question_count = 0

                    load_question()

                    user_text = ""
                    message = ""

                    game_state = "game"

            # GAME
            elif game_state == "game":

                # HOME BUTTON
                if home_button.collidepoint(event.pos):

                    click_sound.stop()
                    click_sound.play()

                    game_state = "category"

                    user_text = ""
                    message = ""
                    hint_used = False

                # NEXT BUTTON
                elif message != "":

                    if next_button.collidepoint(event.pos):

                        click_sound.stop()
                        click_sound.play()

                        if question_count >= max_questions:

                            game_result = "win"

                            levelup_sound.stop()
                            levelup_sound.play()

                            game_state = "result"

                        else:

                            load_question()

                            user_text = ""
                            message = ""

            # RESULT SCREEN
            elif game_state == "result":

                if play_again_button.collidepoint(event.pos):

                    click_sound.stop()
                    click_sound.play()

                    score = 0
                    lives = 3
                    question_count = 0

                    user_text = ""
                    message = ""

                    reset_questions()

                    game_state = "category"

        # KEYBOARD
        if game_state == "game":

            if event.type == pygame.KEYDOWN:

                # HINT
                if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                    if message == "":
                        hint_used = True

                # TYPING
                elif message == "":

                    # BACKSPACE
                    if event.key == pygame.K_BACKSPACE:
                        user_text = user_text[:-1]

                    # ENTER
                    elif event.key == pygame.K_RETURN:

                        if user_text.lower() == correct_answer.lower():

                            correct_sound.stop()
                            correct_sound.play()

                            message = "Correct!"
                            message_color = GREEN

                            score += 10

                        else:

                            wrong_sound.stop()
                            wrong_sound.play()

                            lives -= 1

                            message = "Wrong!"
                            message_color = RED

                        question_count += 1

                        # GAME OVER IF NO LIVES
                        if lives <= 0:

                            game_result = "lose"

                            levelup_sound.stop()
                            levelup_sound.play()

                            game_state = "result"

                        user_text = ""
                        hint_used = False

                    # NORMAL KEYS
                    else:
                        user_text += event.unicode

    pygame.display.update()
    clock.tick(60)

# =========================
# QUIT
# =========================
pygame.quit()
sys.exit()