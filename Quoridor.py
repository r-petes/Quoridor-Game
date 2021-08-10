# Author: Rachel Peterson
# Date: 8/10/21
# Description: A Quoridor game implementation with data members and methods for tracking and validating fence placement
#     and player movement and determining whether or not a game has been won.


class QuoridorGame:
    """
    A class that runs a game of Quoridor with data members and methods for tracking and validating fence placement
    and player movement and determining whether or not a game has been won. Communicates with no other classes
    to accomplish game simulation.
    """

    def __init__(self):
        """
        Initializes the vertical and horizontal fence positions as well as the player positions
        and the total number of positions that each player has placed already (initialized to 0).
        Also initializes the player turn to player 1, as player 1 is to begin the game.
        """
        # Vertical and Horizontal fence positions already occupied/not possible to add fences to
        self._vertical_fence_positions = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8)]
        self._horizontal_fence_positions = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0)]

        # Starting player positions
        self._player_1_position = (4, 0)
        self._player_2_position = (4, 8)

        # Number of fences placed
        self._player_1_fences = 0
        self._player_2_fences = 0

        # Current player's turn, initialized to player 1
        self._players_turn = 1

    def move_pawn(self, player, player_destination):
        """
        Takes as parameters the current player's number (integer) making a move and the player's desired destination
        coordinates (tuple) and checks whether or not this will be a valid pawn move. Returns True and update
        the pawn's position if the move is determined to be valid, otherwise returns False.
        """
        # Set the current_player_position and the opponent_position depending on who is the current player
        if player == 1:
            current_player_position = self._player_1_position
            opponent_position = self._player_2_position

        if player == 2:
            current_player_position = self._player_2_position
            opponent_position = self._player_1_position

        # Check if the game has already been won
        if self.is_game_won() is True:
            return False

        # Check if it is the current player's turn
        if self.is_players_turn(player) is False:
            return False

        # Check if a player is already in that spot
        if self.is_taken(player, player_destination) is True:
            return False

        # Check if a player is trying to move out of bounds
        if self.is_out_of_bounds(player_destination) is False:
            return False

        # Check if the move is a successful orthogonal move
        if self.is_valid_orthogonal(current_player_position, player_destination, opponent_position) is True:
            self.update_coordinates(player, player_destination)
            # Switch turn tracker to the next player's turn
            self.update_turn(player)
            return True

        # Check if the move is a successful diagonal move
        if self.is_valid_diagonal(current_player_position, opponent_position, player_destination) is True:
            self.update_coordinates(player, player_destination)
            # Switch turn tracker to the next player's turn
            self.update_turn(player)
            return True

        return False

    def is_players_turn(self, player):
        """
        Takes as a parameter the current player's number and checks if the correct player is taking a turn.
        Returns True if it is the current player's turn, False otherwise.
        """
        if player == self._players_turn:
            return True
        return False

    def is_game_won(self):
        """
        Takes no parameters and checks both players' positions to see if the game has already been won.
        Returns True if a player has already won, False otherwise.
        """
        for number in range(9):
            # if player_1_position = (0,8) -> (8,8), player 1 has already won
            if self._player_1_position == (number, 8):
                return True
            # or if player_2_position = (0,0) -> (8,0), player 2 has already won
            if self._player_2_position == (number, 0):
                return True
        return False

    def is_taken(self, player, player_destination):
        """
        Takes the current player's number and the player destination coordinates as parameters
        and checks if the player destination is already occupied.
        Returns True if the player's desired destination is already taken,
        False otherwise.
        """
        # If the current player is #2, check if player 1 is already occupying the destination coordinates
        if player == 2:
            if player_destination == self._player_1_position:
                return True
        # If the current player is #1, check if player 2 is already occupying the destination coordinates
        if player == 1:
            if player_destination == self._player_2_position:
                return True
        return False

    def is_out_of_bounds(self, player_destination):
        """
        Takes the player's destination coordinates as a parameter.
        If the move is out of bounds, return False, but otherwise return True.
        """
        # Check x coordinate for out of bounds
        if player_destination[0] < 0 or player_destination[0] > 8:
            return False
        # Check y coordinate for out of bounds
        if player_destination[1] < 0 or player_destination[1] > 8:
            return False

        return True

    def is_valid_orthogonal(self, current_player_position, player_destination, opponent_position):
        """
        Takes the current player's position and destination coordinates as
        well as the opponent's current position and checks if they are making an
        orthogonal movement. Returns True if the orthogonal movement is successful,
        returns False otherwise.
        """

        # if move is 1 right and not blocked by fence, return true
        if player_destination[0] == current_player_position[0] + 1 and player_destination[1] == current_player_position[1]:
            fence_type = "vertical"
            if self.is_fence_blocking(player_destination, fence_type) is False:
                return True

        # if move is 1 left and not blocked by fence, return true
        if player_destination[0] == current_player_position[0] - 1 and player_destination[1] == current_player_position[1]:
            fence_type = "vertical"
            if self.is_fence_blocking(current_player_position, fence_type) is False:
                return True

        # if move is 1 down and not blocked by fence, return true
        if player_destination[0] == current_player_position[0] and player_destination[1] == current_player_position[1] + 1:
            fence_type = "horizontal"
            if self.is_fence_blocking(player_destination, fence_type) is False:
                return True

        # if move is 1 up and not blocked by fence, return true
        if player_destination[0] == current_player_position[0] and player_destination[1] == current_player_position[1] - 1:
            fence_type = "horizontal"
            if self.is_fence_blocking(current_player_position, fence_type) is False:
                return True

        # Check if the move is two spaces because it is skipping another player with no fence blocking the movement
        if self.is_valid_skip(current_player_position, opponent_position, player_destination) is True:
            return True

    def is_valid_skip(self, current_player_position, opponent_position, player_destination):
        """
        Takes the current player's position and destination coordinates as
        well as the opponent's current position and checks whether the current player is skipping over
        the opponent piece. Returns True if the skip movement is valid, returns False otherwise.
        """

        # Check if movement is two up
        if player_destination[0] == current_player_position[0] and player_destination[1] == current_player_position[1] - 2:
            # Check if there is a player at the space between
            if opponent_position[0] == current_player_position[0] and opponent_position[1] == current_player_position[1] - 1:
                fence_type = "horizontal"
                # Ensure that there is no fence blocking
                if self.is_fence_blocking(opponent_position, fence_type) is False:
                    return True

        # Check if movement is two down
        if player_destination[0] == current_player_position[0] and player_destination[1] == current_player_position[1] + 2:
            # Check if there is a player at the space between
            if opponent_position[0] == current_player_position[0] and opponent_position[1] == current_player_position[1] + 1:
                # Ensure that there is no fence blocking
                fence_type = "horizontal"
                if self.is_fence_blocking(player_destination, fence_type) is False:
                    return True

    def is_valid_diagonal(self, current_player_position, opponent_position, player_destination):
        """
        Takes the current player's position and destination coordinates as
        well as the opponent's current position and checks for a valid diagonal movement. If the movement
        is determined to be valid, return True and update the player's position.
        """

        # Check if upward diagonal
        if player_destination[0] == current_player_position[0] + 1 and player_destination[1] == current_player_position[1] - 1 or player_destination[0] == current_player_position[0] - 1 and player_destination[1] == current_player_position[1] - 1:
            # Check if there is another player blocking forward movement
            if opponent_position[0] == current_player_position[0] and opponent_position[1] == current_player_position[1] - 1:
                # check if there is a fence behind the opponent player
                fence_type = "horizontal"
                if self.is_fence_blocking(opponent_position, fence_type) is True:
                    return True

        # Check if backward diagonal
        if player_destination[0] == current_player_position[0] + 1 and player_destination[1] == current_player_position[1] + 1 or player_destination[0] == current_player_position[0] - 1 and player_destination[1] == current_player_position[1] + 1:
            # Check if there is another player blocking backward movement
            if opponent_position[0] == current_player_position[0] and opponent_position[1] == current_player_position[1] + 1:
                # Check if there is a fence at behind that player
                fence_type = "horizontal"
                fence_location = (current_player_position[0], current_player_position[1] + 2)
                if self.is_fence_blocking(fence_location, fence_type) is True:
                    return True

        return False

    def is_fence_blocking(self, fence_coordinates, fence_type):
        """
        Takes as parameters the fence coordinates that would necessitate blocking a predetermined movement
        as well as the fence type and checks if the fence is blocking a movement. Returns True if the fence is
        blocking the movement, False otherwise.
        """

        # Checks for horizontal fence-blocking
        if fence_type == "horizontal":
            if fence_coordinates in self._horizontal_fence_positions:
                return True
        # Checks for vertical fence-blocking
        if fence_type == "vertical":
            if fence_coordinates in self._vertical_fence_positions:
                return True
        return False

    def update_coordinates(self, player, destination_coordinates):
        """
        Takes as parameters the player's number whose turn it is and their destination coordinates and
        updates the player's coordinates to their desired move on a successful turn.
        """
        # If the player is #1, update their coordinates
        if player == 1:
            self._player_1_position = destination_coordinates
            return
        # If the player is #2, update their coordinates
        elif player == 2:
            self._player_2_position = destination_coordinates
            return

    def place_fence(self, player, type_of_fence, fence_destination):
        """
        Takes as parameters the player's number whose turn it is, the type of fence being placed,
        and the desired fence destination. This method determines whether the fence destination
        is valid, and returns True and places a fence if so. It returns False otherwise.
        """

        # Check if the game has already been won
        if self.is_game_won() is True:
            return False

        # Check if it is the current player's turn
        if self.is_players_turn(player) is False:
            return False

        # Checks if the player has fences left to place
        if self.has_fences_left(player) is False:
            return False

        # Check if fence placement is out of bounds
        if self.fence_in_bounds(fence_destination) is False:
            return False

        # Check if fence is already in that destination
        if self.fence_already_there(type_of_fence, fence_destination) is True:
            return False

        # Check if the fence can be placed and update the fence type to include this fence
        self.add_fence(type_of_fence, fence_destination)

        # Increment # of fences placed by that player
        if player == 1:
            self._player_1_fences += 1
        elif player == 2:
            self._player_2_fences += 1

        # Switch turn tracker to the next player's turn
        self.update_turn(player)

        return True

    def has_fences_left(self, player):
        """
        Takes as a parameter the player's number whose turn it is and
        checks if that player has any fences left to place. Returns
        False if the player has no fences left, True otherwise.
        """
        # If the player is #1, check if they have used all 10 fences
        if player == 1:
            if self._player_1_fences == 10:
                return False
        # If the player is #2, check if they have used all 10 fences
        elif player == 2:
            if self._player_2_fences == 10:
                return False
        return True

    def fence_in_bounds(self, fence_destination):
        """
        Takes as a parameter the desired destination of the fence and
        determines if the fence placement is within the board's boundaries
        (coordinates are between 0 and 8 inclusive). Returns True if the fence is
        in bounds, False otherwise.
        """
        # Check if the fence placement position is out of range
        if fence_destination[0] < 0 or fence_destination[0] > 8:
            return False
        if fence_destination[1] < 0 or fence_destination[1] > 8:
            return False

        return True

    def fence_already_there(self, type_of_fence, fence_destination):
        """
        Takes as parameters the type of fence and the coordinates of its desired destination and
        checks if a fence is already in that desired destination. Returns True if a fence is
        already placed in that location, false otherwise.
        """
        # If the fence being placed is horizontal, check the horizontal fence positions
        if type_of_fence == "h":
            if fence_destination in self._horizontal_fence_positions:
                return True
        # If the fence being placed is vertical, check the horizontal fence positions
        if type_of_fence == "v":
            if fence_destination in self._vertical_fence_positions:
                return True
        return False

    def add_fence(self, type_of_fence, fence_destination):
        """
        Takes as parameters the type of fence being placed and that fence's destination coordinates
        and adds the fence to the fence type's list of placed fences.
        """
        # Add a horizontal fence
        if type_of_fence == "h":
            self._horizontal_fence_positions.append(fence_destination)
        # Or add a vertical fence
        if type_of_fence == "v":
            self._vertical_fence_positions.append(fence_destination)
        return

    def update_turn(self, player):
        """
        Takes as a parameter the current player's number and updates the turn tracker
        to indicate the next player's turn.
        """
        if player == 1:
            self._players_turn = 2          # Update the turn tracker to player 2's turn
        if player == 2:
            self._players_turn = 1          # Update the turn tracker to player 1's turn
        return

    def is_winner(self, player):
        """ Takes as a parameter the number of a player and returns True if the player has won and False if not. """

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
