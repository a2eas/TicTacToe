import pygame
import sys
 # Initialize pygame
pygame.init()

# Define constants for the game
WIDTH, HEIGHT = 600, 600
GRID_SIZE = 3
CELL_SIZE = WIDTH // GRID_SIZE
LINE_WIDTH = 15
LINE_COLOR = (255, 255, 255)
CIRCLE_COLOR = (238, 36, 0)
CROSS_COLOR = (0, 255, 0)
BACKGROUND_COLOR = (28, 170, 156)

# Game state representation
# Board layout: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

class TicTacToeGUI:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Tic Tac Toe")
        self.board = [[i + 1 for i in range(j * 3, (j + 1) * 3)] for j in range(3)]  # Initialize the board
        self.game_over = False


        # Draw the grid lines
        for row in range(1, GRID_SIZE):
            pygame.draw.line(self.screen, LINE_COLOR, (0, row * CELL_SIZE), (WIDTH, row * CELL_SIZE), LINE_WIDTH)
            pygame.draw.line(self.screen, LINE_COLOR, (row * CELL_SIZE, 0), (row * CELL_SIZE, HEIGHT), LINE_WIDTH)

        pygame.display.update()

    def draw_mark(self, row, col, mark):
        center = (col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2)
        if mark == 'X':
            pygame.draw.line(self.screen, CROSS_COLOR, (center[0] - CELL_SIZE // 3, center[1] - CELL_SIZE // 3),
                             (center[0] + CELL_SIZE // 3, center[1] + CELL_SIZE // 3), LINE_WIDTH)
            pygame.draw.line(self.screen, CROSS_COLOR, (center[0] + CELL_SIZE // 3, center[1] - CELL_SIZE // 3),
                             (center[0] - CELL_SIZE // 3, center[1] + CELL_SIZE // 3), LINE_WIDTH)
        elif mark == 'O':
            pygame.draw.circle(self.screen, CIRCLE_COLOR, center, CELL_SIZE // 3, LINE_WIDTH)

        pygame.display.update()

    def get_cell_from_mouse(self, pos):
        x, y = pos
        row = y // CELL_SIZE
        col = x // CELL_SIZE
        return row, col

    def get_user_input(self):
        """
        Get the user's input from the mouse click.
        If the cell is already taken (either by 'X' or 'O'), ignore the click.
        """
        if self.game_over:
            return None

        waiting_for_input = True
        while waiting_for_input:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    row, col = self.get_cell_from_mouse(mouse_pos)
                    cell_value = self.board[row][col]

                    # Check if the cell is already taken by either 'X' or 'O'
                    if isinstance(cell_value, int):  # Only allow input if the cell is still available
                        self.board[row][col] = 'X'  # Assume the user is 'X'
                        self.draw_mark(row, col, 'X')  # Draw 'X' in the clicked cell
                        waiting_for_input = False
                        return cell_value  # Return the number corresponding to the cell
                    else:
                        # If the cell is already occupied (by 'X' or 'O'), do nothing
                        print("Invalid move. Try again.")
                        # Do not draw the 'X' if the move is invalid
                        continue  # Ignore the click and keep waiting for valid input
        return None



    def agent_move(self, bourd):
        """
        Analyzes the board and updates the screen to show the agent's move ('O').
        Assumes 'O' positions are already in the board (which is passed as 'bourd').
        """
        for row in range(3):
            for col in range(3):
                if bourd[row][col] == 'O':  # Check for 'O' (agent's move)
                    self.draw_mark(row, col, 'O')

    def check_draw(self):
        """ Check if the game is a draw (board is full). """
        for row in self.board:
            for cell in row:
                if isinstance(cell, int):  # If there's still an empty spot, it's not a draw
                    return False
        return True
    def check_win(self):
        """ Check for a win condition. """
        # Check rows, columns, and diagonals
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2]:
                return self.board[i][0]
            if self.board[0][i] == self.board[1][i] == self.board[2][i]:
                return self.board[0][i]
        if self.board[0][0] == self.board[1][1] == self.board[2][2]:
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0]:
            return self.board[0][2]
        return None
    def check_lost(self):
        """
        Checks if the player (X) has lost the game.
        This happens when the AI (O) wins.
        Returns True if the player has lost, False otherwise.
        """
        # Check for a win for the AI ('O')
        winner = self.check_win()
        if winner == 'O':
            return True  # Player has lost if 'O' wins
        return False
    def show_message(self, message):
        """ Display the message on the screen and freeze the game. """
        self.screen.fill((0,0,0))
        font = pygame.font.Font(None, 74)
        text = font.render(message, True, (255, 255, 255))
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        self.screen.blit(text, text_rect)
        pygame.display.update()
    def mainloop(self):
        self.draw_board()

        while True:
            user_input = self.get_user_input()
            if user_input:
                print(f"User played at {user_input}")
                # After user input, you can have the agent play
                # Example: agent_move(5) if the agent plays at the center
                self.agent_move(4)

            pygame.display.update()
    def quit(self):
        pygame.quit()    
if __name__ == "__main__":
    gui = TicTacToeGUI()
    while play_again.lower() == "y":
        user = 'X'
        test = True
        while test == True:
            userplay = gui.get_user_input()
            play = user_play(userplay)
            if play:
                check = agent_play()
                gui.agent_move(bourd)
                if check == -1:
                    break
                if check == 0:
                    break
        bourd = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        method = True
        play_again = input("if you want to play again type y: ").strip().lower()
    else:
        print("Thank you.")

