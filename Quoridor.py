# Author: Rachel Peterson
# Date: 8/3/21
# Description: 

# Don't forget commenting
# Don't forget docstrings on all functions and classes
# No one-letter variables
# NO METHOD HAS MORE THAN 20-25 LINES OF CODE

class QuoridorGame:
    """ TO DO """

    def __init__(self):
        """
        Initialized the board with the fences (four edges) and
        pawns (P1 and P2) in the correct positions."""
        # all data members are private
        self._vertical_fence_positions = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8)]
        self._horizontal_fence_positions = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0)]
        self._player_1_position = (4, 0)
        self._player_2_position = (4, 8)
        # need to enforce turns?

    def move_pawn(self, player, player_destination):
        """ TO DO: Move the pawn."""
        # takes two params: the player making the move and the coordinates of the destination (tuple)
        if player == 1:
            current_player_position = self._player_1_position
            opponent_position = self._player_2_position

        if player == 2:
            current_player_position = self._player_2_position
            opponent_position = self._player_1_position

        # do the numbers have to be 1 or 2?

        # check if the game has already been won
        if self.check_if_game_won(self) is False:
            return False

        # check if the move is forbidden by the rules
        if self.check_if_forbidden(self, player, player_destination) is False:
            return False

        # if move successful return True
        if self.check_successful_orthogonal(self, current_player_position, player_destination) is True:
            return True

        if self.check_successful_diagonal(self, current_player_position, opponent_position, player_destination)

        return False

    # make sure they haven't already placed a fence/moved a pawn? only one at a time.
    def check_if_game_won(self):
        """ If the game has already been won, return False """
        for number in range(9):
            # if player_1_position = (0,8) - (8,8), player 1 has already won
            if self._player_1_position == (number, 8):
                return False
            # or if player_2_position = (0,0) - (8,0)
            if self._player_2_position == (number, 0):
                return False

    def check_if_forbidden(self, player, player_destination):
        """ If move forbidden by the rule: return False. """

        # if player already in that spot:
        if player == 2:
            if player_destination == self._player_1_position:
                return False
        if player == 1:
            if player_destination == self._player_2_position:
                return False

        # if position out of range:
        if player_destination[0] < 0 or player_destination[0] > 8:
            return False
        if player_destination[1] < 0 or player_destination[1] > 8:
            return False

        return True

    def check_successful_diagonal(self, current_player_position, opponent_position, player_destination):
        """ Check if diagonal move is successful. """

        # if upward diagonal: if player in front with fence behind them,
        # if coordinate == current position (x-1,y-1) OR == (x+1, y-1)
        # if there is another player at (x, y-1)
        # if there is a fence at (x, y-1)
        # move is valid, update position and return True
        # if backward diagonal: if player in front with fence behind them,
        # if coordinate == current position (x-1,y-1) OR == (x+1, y-1)
        # if there is another player at (x, y-1)
        # if there is a fence at (x, y-1)
        # move is valid, update position and return True

        # if left diagonal: if player in front with fence behind them,
        # if coordinate == current position (x-1,y-1) OR == (x+1, y-1)
        # if there is another player at (x, y-1)
        # if there is a fence at (x, y-1)
        # move is valid, update position and return True

        # if right diagonal: if player in front with fence behind them,
        # if coordinate == current position (x-1,y-1) OR == (x+1, y-1)
        # if there is another player at (x, y-1)
        # if there is a fence at (x, y-1)
        # move is valid, update position and return True


    def check_successful_orthogonal(self, current_player_position, player_destination):
        """ Check if orthogonal move is successful. """

        # if move is 1 right and not blocked by fence, return true
        if player_destination[0] == current_player_position[0] + 1 and player_destination[1] == current_player_position[1]:
            fence_type = "horizontal"
            if self.is_fence_blocking(self, player_destination, fence_type) is False:
                return True

        # if move is 1 left and not blocked by fence, return true
        if player_destination[0] == current_player_position[0] - 1 and player_destination[1] == current_player_position[1]:
            fence_type = "horizontal"
            if self.is_fence_blocking(self, current_player_position, fence_type) is False:
                return True

        # if move is 1 down and not blocked by fence, return true
        if player_destination[0] == current_player_position[0] and player_destination[1] == current_player_position[1] + 1:
            fence_type = "vertical"
            if self.is_fence_blocking(self, player_destination, fence_type) is False:
                return True

        # if move is 1 up and not blocked by fence, return true
        if player_destination[0] == current_player_position[0] and player_destination[1] == current_player_position[1] - 1:
            fence_type = "vertical"
            if self.is_fence_blocking(self, current_player_position, fence_type) is False:
                return True

        # if move is left or up, if no fence at current position return True
        # if move is down:
        # if no fence at (x, y+1), return True
        # if move is right, if no fence at (x+1, y), return True
        # if not, return True

        # if player is in front, can jump over (but only if no fence)
        # if move == current position x - or  + 2 or y - or + 2,
        # if there is a player in the space at current +- 1
        # if there is no fence at the space
        # move is valid

    def is_space_taken(self, player_destination):
        """ Checks if the destination space is taken. """
        # Takes a destination space and checks if another player is already in that space

    def is_fence_blocking(self, fence_coordinates, fence_type):
        """ Checks if the fence is blocking the movement. """
        # checks for horizontal moves
        if fence_type == "horizontal":
            if fence_coordinates in self._horizontal_fence_positions:
                return True
        # checks for vertical moves
        if fence_type == "vertical":
            if fence_coordinates in self._vertical_fence_positions:
                return True
        return False


    def place_fence(self, player, type_of_fence, fence_destination):
        """ Place a fence. """
        # params: the player moving the fence, the type of fence (letter) and the fence dest. coords. (tuple)
        # if game already won, return False
        # if no fence left return False
        # if fence out of bounds, return False
        # if fence already there
            # if new fence will overlap, return False
            # if new fence will intersect, return False--- same for one square fence?
        # if the fence can be placed, return True
        # if it breaks the fair play rule, return string "breaks the fair play rule"

    def is_winner(self, player):
        """ Returns True if the player has won and false if not. """
        # Return True if the player won
        for number in range(9):
            # if player_1_position = (0,8) - (8,8), player 1 has won
            if player == 1:
                if self._player_1_position == (number, 8):
                    return True
            # or if player_2_position = (0,0) - (8,0)
            if player == 2:
                if self._player_2_position == (number, 0):
                    return True
        return False

    def print_board(self):
        """ Print the current state of the board."""


q.move_pawn(2, (4,7)) #moves the Player2 pawn -- invalid move because only Player1 can start, returns False
q.move_pawn(1, (4,1)) #moves the Player1 pawn -- valid move, returns True
q.place_fence(1, 'h',(6,5)) #places Player1's fence -- out of turn move, returns False
q.move_pawn(2, (4,7)) #moves the Player2 pawn -- valid move, returns True
q.place_fence(1, 'h',(6,5)) #places Player1's fence -- returns True
q.place_fence(2, 'v',(3,3)) #places Player2's fence -- returns True
q.is_winner(1) #returns False because Player 1 has not won
q.is_winner(2) #returns False because Player 2 has not won