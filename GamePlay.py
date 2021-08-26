import pygame
import Quoridor
import os
from pygame.locals import *

pygame.init()

# Initialise screen
WIDTH, HEIGHT = 540, 540
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Quoridor Game')

WHITE = (255, 255, 255)
FPS = 60
PAWN_WIDTH = 55
PAWN_HEIGHT = 75

FENCE_IMAGE = pygame.image.load(os.path.join("images", "fence.png"))
FENCE = pygame.transform.scale(FENCE_IMAGE, (60, 12))

PLAYER_1_IMAGE = pygame.image.load(os.path.join("images", "player_1_pawn.png"))
PLAYER_1 = pygame.transform.scale(PLAYER_1_IMAGE, (PAWN_WIDTH, PAWN_HEIGHT))
PLAYER_2_IMAGE = pygame.image.load(os.path.join("images", "player_2_pawn.png"))
PLAYER_2 = pygame.transform.scale(PLAYER_2_IMAGE, (PAWN_WIDTH, PAWN_HEIGHT))


# Images, etc.  :
# class for each object in game:

class Player1Pawn(pygame.sprite.Sprite):
    """A pawn will start in starting position and move when destination is determined."""

    # returns the pawn's new position based on the player's selection (and its validity)
    def __init__(self):
        """ Initialize the pawn placement."""
        pygame.sprite.Sprite.__init__(self)
        self._player_1_placement = pygame.Rect(273, 0, PAWN_WIDTH, PAWN_HEIGHT)

    def get_player_1_placement(self):
        """ Returns the player's placement on the board. """
        return self._player_1_placement

# return pygame.Rect(x, y, PAWN_WIDTH, PAWN_HEIGHT)


class Player2Pawn(pygame.sprite.Sprite):
    """A pawn will start in starting position and move when destination is determined."""

    # returns the pawn's new position based on the player's selection (and its validity)
    def __init__(self):
        """ Initialize the pawn placement."""
        pygame.sprite.Sprite.__init__(self)
        self._player_2_placement = pygame.Rect(273, 525, PAWN_WIDTH, PAWN_HEIGHT)

    def get_player_2_placement(self):
        """ Returns the player's placement on the board. """
        return self._player_2_placement


    # returns the pawn's new position based on the player's selection (and its validity)
    # return pygame.Rect(x, y, PAWN_WIDTH, PAWN_HEIGHT)


class Fence(pygame.sprite.Sprite):
    """A fence to be placed."""


class Square(pygame.sprite.Sprite):
    """ Create 81 squares to make up the board. """

    def __init__(self, x_coordinate, y_coordinate):
        pygame.sprite.Sprite.__init__(self)
        self._square_coordinates = (x_coordinate, y_coordinate)
        self._square_image = pygame.image.load(os.path.join("images", "square.png"))
        self._square = pygame.transform.scale(self._square_image, (50, 50))

    def blitSquare(self, destination_x, destination_y):
        """ Creates a square on the screen in the determined destination so as to create a 9x9 board."""
        WIN.blit(self._square, ((destination_x * 60), (destination_y * 60)))

    def getSquareCoordinates(self):
        """ Returns the coordinates of the square. """
        return self._square_coordinates


def draw_window(player_1, player_2):
    """ Fill the window. """
    squares = []
    WIN.fill(WHITE)

    # Create a board of squares
    for x_values in range(0, 9):
        for y_values in range(0, 9):
            new_square = Square(x_values, y_values)
            new_square.blitSquare(x_values, y_values)
            squares.append(new_square)

    WIN.blit(FENCE, (300, 300))
    WIN.blit(PLAYER_1, (player_1.x, player_1.y))
    WIN.blit(PLAYER_2, (player_2.x, player_2.y))

    pygame.display.update()


def main():
    player_1 = Player1Pawn()
    player_2 = Player2Pawn()


    squares = []

    clock = pygame.time.Clock()
    run = True

    # Events loop
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == QUIT:
                run = False

        draw_window(player_1.get_player_1_placement(), player_2.get_player_2_placement())



        # GAME PLAY:

        # Initialize game object
        # quoridor = Quoridor.QuoridorGame()

        # # Print whose turn it is
        # if quoridor.is_players_turn(1) is True:
        #     text = font.render("Player 1's turn.", 1, (10, 10, 10))
        #     textpos = text.get_rect()
        #     textpos.centerx = background.get_rect().centerx
        #     background.blit(text, textpos)
        #
        #     # Blit everything to the screen
        #     screen.blit(background, (0, 0))
        #     pygame.display.flip()
        #
        # if quoridor.is_players_turn(2) is True:
        #     text = font.render("Player 2's turn.", 1, (10, 10, 10))
        #     textpos = text.get_rect()
        #     textpos.centerx = background.get_rect().centerx
        #     background.blit(text, textpos)
        #
        #     # Blit everything to the screen
        #     screen.blit(background, (0, 0))
        #     pygame.display.flip()

        # Allows player to choose either move pawn or place fence
        # if the move is valid, (returns True) then:
        # Clicks space or enters coordinates for moving pawn/placing fence
        #    # handle MOUSEBUTTONUP
        #     if event.type == pygame.MOUSEBUTTONUP:
        #       pos = pygame.mouse.get_pos()
        #
        #       # get a list of all sprites that are under the mouse cursor
        #       clicked_sprites = [s for s in sprites if s.rect.collidepoint(pos)]
        #       # do something with the clicked sprites...
        # Update placement on board
        # Check if the game has been won
        # Print the return statement

        # Print the return statement if the move/placement is not possible.

    pygame.quit()


if __name__ == '__main__':
    main()
