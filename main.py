import pygame
import sys
from button import Button
import pygame_gui

play_game = True
show_splash_screen = True
pygame.init()

WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
CENTRE_X = WINDOW_WIDTH // 2
CENTRE_Y = WINDOW_HEIGHT // 2

WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("GPT World")

CLOCK = pygame.time.Clock()

UI_REFRESH_RATE = CLOCK.tick(60) / 1000

BACKGROUND = pygame.image.load("assets/img/background.png")

UI_MANAGER = pygame_gui.UIManager((WINDOW_WIDTH, WINDOW_HEIGHT))

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/fonts//press-start-2p.ttf", size)

def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        WINDOW.fill("black")

        PLAY_TEXT = get_font(45).render("This is the PLAY screen.", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(CENTRE_X, 260))
        WINDOW.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(CENTRE_X, 460),
                           text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(WINDOW)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        WINDOW.fill("white")

        OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(CENTRE_X, 260))
        WINDOW.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(CENTRE_X, 460),
                              text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(WINDOW)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def main_menu():
    while True:
        WINDOW.blit(BACKGROUND, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("GPT World", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(CENTRE_X, 65))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/img/button-rect.png"), pos=(CENTRE_X, 200),
                             text_input="PLAY", font=get_font(40), base_color="#d7fcd4", hovering_color="White")
        CREATE_PLAYER_BUTTON = Button(image=pygame.image.load("assets/img/button-rect.png"), pos=(CENTRE_X, 350),
                                text_input="CREATE PLAYER", font=get_font(40), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/img/button-rect.png"), pos=(CENTRE_X, 500),
                                text_input="OPTIONS", font=get_font(40), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/img/button-rect.png"), pos=(CENTRE_X, 650),
                             text_input="QUIT", font=get_font(40), base_color="#d7fcd4", hovering_color="White")

        WINDOW.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON, CREATE_PLAYER_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(WINDOW)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if CREATE_PLAYER_BUTTON.checkForInput(MENU_MOUSE_POS):
                    create_player()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
            
            UI_MANAGER.process_events(event)
        
        UI_MANAGER.update(UI_REFRESH_RATE)
        UI_MANAGER.draw_ui(WINDOW)

        pygame.display.update()

def create_player():
    
    name_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((100, 200), (100, 50)), text="Name:", manager=UI_MANAGER)
    name_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((200, 200), (900, 50)), manager=UI_MANAGER, object_id="#name-entry")

    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        WINDOW.fill("black")

        HEADER = get_font(45).render("CREATE PLAYER", True, "white")
        HEADER_RECT = HEADER.get_rect(center=(CENTRE_X, 50))
        WINDOW.blit(HEADER, HEADER_RECT)

        BACK_BUTTON = Button(image=None, pos=(CENTRE_X, 560), text_input="BACK", font=get_font(45), base_color="white", hovering_color="Green")

        BACK_BUTTON.changeColor(OPTIONS_MOUSE_POS)
        BACK_BUTTON.update(WINDOW)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BACK_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    name_label.visible = False
                    name_input.visible = False
                    main_menu()
                        
            UI_MANAGER.process_events(event)
        
        UI_MANAGER.update(UI_REFRESH_RATE)
        UI_MANAGER.draw_ui(WINDOW)

        pygame.display.update()


main_menu()

