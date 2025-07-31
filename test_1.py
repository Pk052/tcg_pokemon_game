from src.game.card import PokemonCard
from src.game.card import EnergyCard
from src.game.deck import Deck
from src.game.player import Player
from src.game.game_engine import GameEngine

if __name__ == "__main__":
    # Crea alcune carte di esempio
    pikachu = PokemonCard("Pikachu", 70, "electric", [
        {"name": "Thunder Shock", "damage": 20, "cost": ["electric"]}
    ])
    
    energy = EnergyCard("Electric Energy", "electric")
    
    # Crea mazzi (questo è solo un esempio, servono 60 carte)
    deck1_cards = [pikachu] * 4 + [energy] * 20  # Esempio semplificato
    deck2_cards = [pikachu] * 4 + [energy] * 20
    
    deck1 = Deck(deck1_cards)
    deck2 = Deck(deck2_cards)
    
    # Crea giocatori
    player1 = Player("Ash", deck1)
    player2 = Player("Gary", deck2)
    
    # Inizia il gioco
    game = GameEngine(player1, player2)
    game.setup_game()
    
    print(f"Gioco iniziato! {player1.name} vs {player2.name}")
    print(f"Carte in mano {player1.name}: {len(player1.hand)}")
    print(f"Carte in mano {player2.name}: {len(player2.hand)}")