# -*- coding: utf-8 -*-

import pygame, sys
from pygame.locals import *


def main():
    cores = {
        "backgroundColor": "#f6effd",
        "xColor": "#f36654",
        "oColor": "#4ac8c6",
        "mainColor": "#dd8fd5",
        "accentColor": "#7e1eb1",
    }

    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("Jogo da Velha")

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()


if __name__ == "__main__":
    main()
