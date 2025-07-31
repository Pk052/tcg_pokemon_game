import pygame

class CardDisplay:
    def __init__(self, card, x, y):
        self.card = card
        self.x = x
        self.y = y
        self.image = self.load_card_image()
    
    def load_card_image(self):
        try:
            return pygame.image.load(self.card.image_path)
        except:
            # Crea un placeholder se l'immagine non esiste
            surface = pygame.Surface((80, 120))
            surface.fill((200, 200, 200))
            return surface