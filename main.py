"""
Pokemon TCG Game - Main Entry Point
"""

import pygame
import sys
from src.ui.main_window import MainWindow

def main():
    pygame.init()
    app = MainWindow()
    app.run()
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()