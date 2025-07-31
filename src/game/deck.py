import random

class Deck:
    def __init__(self, cards=None):
        self.cards = cards or []
    
    def shuffle(self):
        random.shuffle(self.cards)
    
    def add_card(self, card):
        self.cards.append(card)
    
    def is_valid(self):
        # Regole base: 60 carte, max 4 copie per carta (eccetto energie base)
        if len(self.cards) != 60:
            return False
        
        card_counts = {}
        for card in self.cards:
            card_counts[card.name] = card_counts.get(card.name, 0) + 1
            if card.card_type != 'energy' and card_counts[card.name] > 4:
                return False
        
        return True