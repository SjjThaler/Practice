# Define a chess board class.

class ChessBoard:
    def __init__(self):
        self.board = [
            ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['_', '_', '_', '_', '_', '_', '_', '_'],
            ['_', '_', '_', '_', '_', '_', '_', '_'],
            ['_', '_', '_', '_', '_', '_', '_', '_'],
            ['_', '_', '_', '_', '_', '_', '_', '_'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']
        ]
	

    def display(self):
    	for row in self.board:
    		print(''.join(row))

    def move_piece(self, from_pos, to_pos):

    	# Unpacking tulples
    	from_row, from_col = from_pos
    	to_row, to_col = to_pos

    	# Assigning the new position of the piece
    	self.board[to_row][to_col] = self.board[from_row][from_col]

    	# Clearing old position of the piece
    	self.board[from_row][from_col] = '_'

# Initialize chess board

chess_board = ChessBoard()

# Call chess_board

chess_board.display()

chess_board.move_piece((1,0),(3,0))
chess_board.move_piece((7,1),(5,2))

chess_board.display()
