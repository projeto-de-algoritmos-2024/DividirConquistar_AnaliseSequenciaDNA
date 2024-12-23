import pygame
import sys


def get_sequence():
    pygame.init()

    WIDTH = 600
    HEIGHT = 200
    WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Entrada de Sequência")

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GRAY = (200, 200, 200)

    font = pygame.font.Font(None, 36)

    input_box = pygame.Rect(50, 50, 400, 40)
    button = pygame.Rect(WIDTH // 2 - 50, 120, 100, 40)

    text = ""
    active = False

    instruction = font.render("Digite a sequência (ex: AGCTGAC):", True, BLACK)
    button_text = font.render("Enviar", True, BLACK)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = True
                elif button.collidepoint(event.pos):
                    if text:
                        pygame.quit()
                        return text
                else:
                    active = False

            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        if text:
                            pygame.quit()
                            return text
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        if event.unicode.upper() in "ACGTU":
                            text += event.unicode.upper()

        WINDOW.fill(WHITE)

        pygame.draw.rect(WINDOW, GRAY if active else BLACK, input_box, 2)

        pygame.draw.rect(WINDOW, GRAY, button)

        text_surface = font.render(text, True, BLACK)
        WINDOW.blit(instruction, (50, 20))
        WINDOW.blit(text_surface, (input_box.x + 5, input_box.y + 5))
        WINDOW.blit(button_text, (button.x + 10, button.y + 10))

        pygame.display.flip()
