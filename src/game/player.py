class Player:
    def __init__(self, name, deck):
        self.name = name
        self.deck = deck
        self.hand = []
        self.active_pokemon = None
        self.bench = []  # Fino a 5 Pokémon
        self.prize_cards = []
        self.discard_pile = []
        
    def draw_card(self, num=1):
        for _ in range(num):
            if self.deck.cards:
                self.hand.append(self.deck.cards.pop())
    
    def play_card(self, card_index):
        if 0 <= card_index < len(self.hand):
            return self.hand.pop(card_index)
        return None