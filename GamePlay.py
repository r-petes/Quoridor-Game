import pygame
import Quoridor
from pygame.locals import *


pygame.init()


# Images, etc.  :
# class for each object in game:

class Player1Pawn(pygame.sprite.Sprite):
    """A pawn will start in starting position and move when destination is determined."""

class Player2Pawn(pygame.sprite.Sprite):
    """A pawn will start in starting position and move when destination is determined."""

class Fence(pygame.sprite.Sprite):
    """A fence to be placed."""

class Board(pygame.sprite.Sprite):
    """The board background."""



def main():
    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode((1000, 1000))
    pygame.display.set_caption('Quoridor Game')

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))

    # Display some text
    font = pygame.font.Font(None, 36)
    text = font.render("Welcome to Quoridor!", 1, (10, 10, 10))
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    background.blit(text, textpos)

    # Blit everything to the screen
    screen.blit(background, (0, 0))
    pygame.display.flip()

    # Event loop
    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                return

        screen.blit(background, (0, 0))
        pygame.display.flip()

        # GAME PLAY:

        # Initialize game object
        quoridor = Quoridor.QuoridorGame()

        # Print whose turn it is
        if quoridor.is_players_turn(1) is True:
            text = font.render("Player 1's turn.", 1, (10, 10, 10))
            textpos = text.get_rect()
            textpos.centerx = background.get_rect().centerx
            background.blit(text, textpos)

            # Blit everything to the screen
            screen.blit(background, (0, 0))
            pygame.display.flip()

        if quoridor.is_players_turn(2) is True:
            text = font.render("Player 2's turn.", 1, (10, 10, 10))
            textpos = text.get_rect()
            textpos.centerx = background.get_rect().centerx
            background.blit(text, textpos)

            # Blit everything to the screen
            screen.blit(background, (0, 0))
            pygame.display.flip()


        # Allows player to choose either move pawn or place fence
        # if the move is valid, (returns True) then:
            # Clicks space or enters coordinates for moving pawn/placing fence
            # Update placement on board
            # Check if the game has been won
                # Print the return statement

        # Print the return statement if the move/placement is not possible.



if __name__ == '__main__': main()