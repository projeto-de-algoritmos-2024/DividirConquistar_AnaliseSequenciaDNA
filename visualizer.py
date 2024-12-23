import pygame
import sys


class Visualizer:
    def __init__(self):
        pygame.init()
        self.WIDTH = 800
        self.HEIGHT = 400
        self.WINDOW = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Análise de Sequência Biológica")

        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.YELLOW = (255, 255, 0)
        self.BLUE = (0, 0, 255)
        self.GREEN = (0, 255, 0)
        self.GRAY = (200, 200, 200)

        self.font = pygame.font.Font(None, 36)

    def get_sequence(self):
        """Obtém a sequência do usuário"""
        input_box = pygame.Rect(200, 150, 400, 40)
        button = pygame.Rect(350, 220, 100, 40)

        text = ""
        active = False

        instruction = self.font.render(
            "Digite a sequência (ex: AGCTGAC):", True, self.BLACK
        )
        button_text = self.font.render("Enviar", True, self.BLACK)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if input_box.collidepoint(event.pos):
                        active = True
                    elif button.collidepoint(event.pos) and text:
                        return text
                    else:
                        active = False

                if event.type == pygame.KEYDOWN and active:
                    if event.key == pygame.K_RETURN and text:
                        return text
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        if event.unicode.upper() in "ACGTU":
                            text += event.unicode.upper()

            self.WINDOW.fill(self.WHITE)
            pygame.draw.rect(
                self.WINDOW, self.GRAY if active else self.BLACK, input_box, 2
            )
            pygame.draw.rect(self.WINDOW, self.GRAY, button)

            text_surface = self.font.render(text, True, self.BLACK)
            self.WINDOW.blit(instruction, (200, 120))
            self.WINDOW.blit(text_surface, (input_box.x + 5, input_box.y + 5))
            self.WINDOW.blit(button_text, (button.x + 10, button.y + 10))

            pygame.display.flip()

    def show_sorting_steps(
        self, message, bases, numbers, left_idx=None, right_idx=None, merged=None
    ):
        """Mostra um passo da ordenação"""
        self.WINDOW.fill(self.WHITE)

        message_y = self.HEIGHT * 0.2
        bases_y = self.HEIGHT * 0.4
        numbers_y = self.HEIGHT * 0.6

        total_elements = len(bases)
        element_width = 40
        total_width = total_elements * element_width

        x_start = (self.WIDTH - total_width) // 2

        message_text = self.font.render(message, True, self.BLACK)
        bases_label = self.font.render("Bases:", True, self.BLACK)
        numbers_label = self.font.render("Números:", True, self.BLACK)

        label_x = x_start - 150

        self.WINDOW.blit(
            message_text, ((self.WIDTH - message_text.get_width()) // 2, message_y)
        )
        self.WINDOW.blit(bases_label, (label_x, bases_y))
        self.WINDOW.blit(numbers_label, (label_x, numbers_y))

        for i, (base, num) in enumerate(zip(bases, numbers)):
            x_pos = x_start + (i * element_width)

            color = self.BLACK
            if merged is not None and num in merged:
                color = self.GREEN
            elif left_idx is not None and i <= left_idx:
                color = self.YELLOW
            elif right_idx is not None and left_idx is not None and i > left_idx:
                color = self.BLUE

            base_text = self.font.render(str(base), True, color)
            num_text = self.font.render(str(num), True, color)

            self.WINDOW.blit(base_text, (x_pos, bases_y))
            self.WINDOW.blit(num_text, (x_pos, numbers_y))

        pygame.display.flip()
        pygame.time.wait(500)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def show_results(self, inversions, disorder_index):
        """Mostra os resultados finais"""
        inv_text = self.font.render(
            f"Número de inversões: {inversions}", True, self.BLACK
        )
        disorder_text = self.font.render(
            f"Índice de desordem: {disorder_index:.2%}", True, self.BLACK
        )

        button_color = (150, 150, 150)
        exit_button = pygame.Rect(300, 250, 200, 40)
        exit_text = self.font.render("Sair", True, self.BLACK)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if exit_button.collidepoint(event.pos):
                        pygame.quit()
                        return

                if exit_button.collidepoint(pygame.mouse.get_pos()):
                    button_color = self.GRAY
                else:
                    button_color = (150, 150, 150)

            self.WINDOW.fill(self.WHITE)
            self.WINDOW.blit(inv_text, (200, 150))
            self.WINDOW.blit(disorder_text, (200, 200))

            pygame.draw.rect(self.WINDOW, button_color, exit_button)
            pygame.draw.rect(self.WINDOW, self.BLACK, exit_button, 2)

            text_rect = exit_text.get_rect(center=exit_button.center)
            self.WINDOW.blit(exit_text, text_rect)

            pygame.display.flip()
