# TCG Pokémon Game
A virtual TCG Pokémon game where you can battle with other players and reach the top of the world


## Caratteristiche
- Meccaniche di gioco fedeli al TCG originale
- Interfaccia grafica con Pygame
- Sistema di mazzi personalizzabili
- Modalità giocatore vs giocatore

## Installazione
pip install -r requirements.txt
python main.py


## Struttura progetto
pokemon-tcg-game/
├── src/
│   ├── game/
│   │   ├── __init__.py
│   │   ├── card.py          # Classe per le carte
│   │   ├── deck.py          # Gestione mazzi
│   │   ├── player.py        # Logica giocatore
│   │   ├── battle.py        # Logica di battaglia
│   │   └── game_engine.py   # Motore principale
│   ├── ui/
│   │   ├── __init__.py
│   │   ├── main_window.py   # Interfaccia principale
│   │   ├── game_board.py    # Campo da gioco
│   │   └── card_display.py  # Visualizzazione carte
│   └── utils/
│       ├── __init__.py
│       ├── card_loader.py   # Caricamento dati carte
│       └── constants.py     # Costanti del gioco
├── assets/
│   ├── cards/              # Immagini delle carte
│   ├── backgrounds/        # Sfondi
│   └── sounds/            # Suoni (opzionale)
├── data/
│   ├── cards.json         # Database delle carte
│   └── sets.json          # Set di carte
├── tests/
├── requirements.txt
├── main.py
└── README.md

