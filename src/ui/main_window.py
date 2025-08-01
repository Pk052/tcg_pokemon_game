import pygame
from enum import Enum

class GameState(Enum):
    MENU = "menu"
    DECK_SELECTION = "deck_selection"
    GAME = "game"
    SETTINGS = "settings"

class MainWindow():
    def __init__(self):
        # Pygame initialization
        pygame.init()

        # Window constants
        self.WINDOW_WIDTH = 1200
        self.WINDOW_HEIGHT = 800
        self.fps = 60

        # Colors
        self.COLORS = {
            'background': (20, 30, 50),
            'card_bg': (240, 240, 240),
            'button': (70, 130, 180),
            'button_hover': (100, 149, 237),
            'text': (255, 255, 255),
            'text_dark': (50, 50, 50),
            'accent': (255, 215, 0)
        }

        # Setup display
        self.screen = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        pygame.display.set_caption("Pokemon TCG Game")
        self.clock = pygame.time.Clock()

        # Fonts
        self.fonts = {
            'title': pygame.font.Font(None, 72),
            'button': pygame.font.Font(None, 36),
            'text': pygame.font.Font(None, 24)
        }

        self.current_state = GameState.MENU
        self.running = True

        # Menu buttons
        # self.buttons = []
        self.create_menu_buttons()

        # Mouse state
        self.mouse_pos = (0, 0)
        self.mouse_clicked = False

    def create_menu_buttons(self):
        """Crea i bottoni del menu principale"""
        button_width = 200
        button_height = 50
        button_spacing = 20
        start_y = 350

        button_data = [
            ("New Game", self.start_new_game),
            ("Deck Builder", self.open_deck_builder),
            ("Settings", self.open_settings),
            ("Exit", self.exit_game)
        ]

        self.buttons = []
        for i, (text, callback) in enumerate(button_data):
            x = (self.WINDOW_WIDTH - button_width) // 2
            y = start_y + i * (button_height + button_spacing)
            
            button = {
                'rect': pygame.Rect(x, y, button_width, button_height),
                'text': text,
                'callback': callback,
                'hovered': False
            }
            self.buttons.append(button)

    def handle_events(self):
        """Gestisce tutti gli eventi"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                
            elif event.type == pygame.MOUSEMOTION:
                self.mouse_pos = event.pos
                self.update_button_hover()
                
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left click
                    self.mouse_clicked = True
                    self.handle_button_clicks()
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if self.current_state != GameState.MENU:
                        self.current_state = GameState.MENU
                    else:
                        self.running = False

    def update_button_hover(self):
        """Aggiorna lo stato hover dei bottoni"""
        for button in self.buttons:
            button['hovered'] = button['rect'].collidepoint(self.mouse_pos)

    def handle_button_clicks(self):
        """Gestisce i click sui bottoni"""
        for button in self.buttons:
            if button['rect'].collidepoint(self.mouse_pos):
                button['callback']()
                break

    def draw_menu(self):
        """Disegna il menu principale"""
        # Sfondo
        self.screen.fill(self.COLORS['background'])
        
        # Titolo
        title_text = self.fonts['title'].render("Pokemon TCG", True, self.COLORS['accent'])
        title_rect = title_text.get_rect(center=(self.WINDOW_WIDTH // 2, 150))
        self.screen.blit(title_text, title_rect)
        
        subtitle_text = self.fonts['button'].render("Card Game", True, self.COLORS['text'])
        subtitle_rect = subtitle_text.get_rect(center=(self.WINDOW_WIDTH // 2, 200))
        self.screen.blit(subtitle_text, subtitle_rect)
        
        # Bottoni
        for button in self.buttons:
            # Colore del bottone
            color = self.COLORS['button_hover'] if button['hovered'] else self.COLORS['button']
            
            # Disegna il bottone
            pygame.draw.rect(self.screen, color, button['rect'])
            pygame.draw.rect(self.screen, self.COLORS['text'], button['rect'], 2)
            
            # Testo del bottone
            text_surface = self.fonts['button'].render(button['text'], True, self.COLORS['text'])
            text_rect = text_surface.get_rect(center=button['rect'].center)
            self.screen.blit(text_surface, text_rect)
        
        # Versione in basso
        version_text = self.fonts['text'].render("v0.1.0 - Alpha", True, self.COLORS['text'])
        version_rect = version_text.get_rect(bottomright=(self.WINDOW_WIDTH - 10, self.WINDOW_HEIGHT - 10))
        self.screen.blit(version_text, version_rect)
    
    # Placeholder

    def draw_game_placeholder(self):
        """Placeholder per la schermata di gioco"""
        self.screen.fill((40, 60, 80))
        
        # Titolo
        title_text = self.fonts['title'].render("Game Board", True, self.COLORS['text'])
        title_rect = title_text.get_rect(center=(self.WINDOW_WIDTH // 2, 100))
        self.screen.blit(title_text, title_rect)
        
        # Placeholder per il campo da gioco
        board_rect = pygame.Rect(100, 200, self.WINDOW_WIDTH - 200, 400)
        pygame.draw.rect(self.screen, (60, 80, 100), board_rect)
        pygame.draw.rect(self.screen, self.COLORS['text'], board_rect, 2)
        
        # Testo placeholder
        placeholder_text = self.fonts['button'].render("Game will be implemented here", True, self.COLORS['text'])
        placeholder_rect = placeholder_text.get_rect(center=board_rect.center)
        self.screen.blit(placeholder_text, placeholder_rect)
        
        # Istruzioni
        back_text = self.fonts['text'].render("Press ESC to return to menu", True, self.COLORS['text'])
        back_rect = back_text.get_rect(center=(self.WINDOW_WIDTH // 2, 650))
        self.screen.blit(back_text, back_rect)
    
    def draw_deck_builder_placeholder(self):
        """Placeholder per il deck builder"""
        self.screen.fill((50, 40, 70))
        
        title_text = self.fonts['title'].render("Deck Builder", True, self.COLORS['text'])
        title_rect = title_text.get_rect(center=(self.WINDOW_WIDTH // 2, 100))
        self.screen.blit(title_text, title_rect)
        
        placeholder_text = self.fonts['button'].render("Deck Builder coming soon!", True, self.COLORS['text'])
        placeholder_rect = placeholder_text.get_rect(center=(self.WINDOW_WIDTH // 2, 400))
        self.screen.blit(placeholder_text, placeholder_rect)
        
        back_text = self.fonts['text'].render("Press ESC to return to menu", True, self.COLORS['text'])
        back_rect = back_text.get_rect(center=(self.WINDOW_WIDTH // 2, 650))
        self.screen.blit(back_text, back_rect)
    
    def draw_settings_placeholder(self):
        """Placeholder per le impostazioni"""
        self.screen.fill((70, 50, 40))
        
        title_text = self.fonts['title'].render("Settings", True, self.COLORS['text'])
        title_rect = title_text.get_rect(center=(self.WINDOW_WIDTH // 2, 100))
        self.screen.blit(title_text, title_rect)
        
        placeholder_text = self.fonts['button'].render("Settings panel coming soon!", True, self.COLORS['text'])
        placeholder_rect = placeholder_text.get_rect(center=(self.WINDOW_WIDTH // 2, 400))
        self.screen.blit(placeholder_text, placeholder_rect)
        
        back_text = self.fonts['text'].render("Press ESC to return to menu", True, self.COLORS['text'])
        back_rect = back_text.get_rect(center=(self.WINDOW_WIDTH // 2, 650))
        self.screen.blit(back_text, back_rect)

    def draw(self):
        """Disegna la schermata corrente"""
        if self.current_state == GameState.MENU:
            self.draw_menu()
        elif self.current_state == GameState.GAME:
            self.draw_game_placeholder()
        elif self.current_state == GameState.DECK_SELECTION:
            self.draw_deck_builder_placeholder()
        elif self.current_state == GameState.SETTINGS:
            self.draw_settings_placeholder()
    
    def update(self):
        """Aggiorna la logica del gioco"""
        # Reset mouse click
        self.mouse_clicked = False
        
        # Qui andrà la logica di aggiornamento specifica per ogni stato
        pass

    # Callback functions per i bottoni
    def start_new_game(self):
        """Inizia una nuova partita"""
        print("Starting new game...")
        self.current_state = GameState.GAME
    
    def open_deck_builder(self):
        """Apre il deck builder"""
        print("Opening deck builder...")
        self.current_state = GameState.DECK_SELECTION
    
    def open_settings(self):
        """Apre le impostazioni"""
        print("Opening settings...")
        self.current_state = GameState.SETTINGS
    
    def exit_game(self):
        """Esce dal gioco"""
        print("Exiting game...")
        self.running = False
    
    def run(self):
        """Loop principale del gioco"""
        print("Pokemon TCG Game starting...")
        
        while self.running:
            # Gestisci eventi
            self.handle_events()
            
            # Aggiorna logica
            self.update()
            
            # Disegna tutto
            self.draw()
            
            # Aggiorna display
            pygame.display.flip()
            self.clock.tick(self.fps)
        
        print("Game shutting down...")
        pygame.quit()