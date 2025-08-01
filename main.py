#!/usr/bin/env python3
"""
Pokemon TCG Game - Main Entry Point
Avvia il gioco delle carte Pokemon
"""

import sys
import os

# Aggiungi la cartella src al path per gli import
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

try:
    import pygame
    from ui.main_window import MainWindow
except ImportError as e:
    print(f"Errore: Libreria mancante - {e}")
    print("Installa le dipendenze con: pip install pygame")
    sys.exit(1)

def main():
    """Funzione principale del gioco"""
    try:
        # Inizializza Pygame
        pygame.init()
        
        # Crea e avvia la finestra principale
        app = MainWindow()
        app.run()
        
    except Exception as e:
        print(f"Errore durante l'esecuzione: {e}")
        return 1
    
    finally:
        # Cleanup
        pygame.quit()
    
    return 0

if __name__ == "__main__":
    sys.exit(main())