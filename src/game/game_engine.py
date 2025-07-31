class GameEngine:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.current_player = player1
        self.turn_count = 0
        self.game_state = "setup"  # setup, playing, ended
        
    def setup_game(self):
        # Mescola mazzi
        self.player1.deck.shuffle()
        self.player2.deck.shuffle()
        
        # Pesca 7 carte iniziali
        self.player1.draw_card(7)
        self.player2.draw_card(7)
        
        # Metti 6 carte premio
        for _ in range(6):
            if self.player1.deck.cards:
                self.player1.prize_cards.append(self.player1.deck.cards.pop())
            if self.player2.deck.cards:
                self.player2.prize_cards.append(self.player2.deck.cards.pop())
        
        self.game_state = "playing"
    
    def switch_turn(self):
        self.current_player = self.player2 if self.current_player == self.player1 else self.player1
        self.turn_count += 1
    
    def check_win_condition(self):
        # Vince se:
        # 1. L'avversario non ha più carte premio
        # 2. L'avversario non può pescare
        # 3. L'avversario non ha Pokémon attivi
        for player in [self.player1, self.player2]:
            if len(player.prize_cards) == 0:
                return player
            if not player.deck.cards and not player.hand:
                opponent = self.player2 if player == self.player1 else self.player1
                return opponent
            if not player.active_pokemon and not player.bench:
                opponent = self.player2 if player == self.player1 else self.player1
                return opponent
        return None
