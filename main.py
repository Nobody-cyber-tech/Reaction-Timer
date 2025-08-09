import pygame
import random
import time



# Init
pygame.init()
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Reaction Timer")
font = pygame.font.SysFont("Arial", 36)
clock = pygame.time.Clock()

# color
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)


def reset():
    global red_screen, clicked, start_time, delay, reaction_start, message, show_result
    red_screen = True
    clicked = False
    start_time = time.time()
    delay = random.uniform(2, 5)
    reaction_start = 0
    message = ""
    show_result = False

reset()
    

# main loop
running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN and not clicked:
            clicked = True
            if red_screen:
                message = "Too Early!"
                reset()
            else:
                reaction_time = int((time.time() - reaction_start)*1000)
                message = f"Your time: {reaction_time} ms"

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and clicked:
            reset()

    if red_screen and time.time() - start_time >= delay:
        red_screen = False
        reaction_start = time.time()

    if not clicked:
        if red_screen:
            screen.fill(red)
            text = font.render("Get Ready!", True, black)
        else:
            screen.fill(green)
            text = font.render("Click!", True, black)
        screen.blit(text, (width//2 - text.get_width()//2, height//2))
    
    else:
        screen.fill(white)
        result = font.render(message, True, black)
        screen.blit(result, (width//2 - result.get_width()//2, height//2))
        hint = font.render("Press SPACE to play again", True, (200, 200, 200))
        screen.blit(hint, (300 - hint.get_width() // 2, 250))



    pygame.display.flip()

pygame.quit()
