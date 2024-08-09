
import sprites
import os
os.system('cls||clear')


import math

move_color = 'white'
darks = ['a1','a3','a5','a7','b2','b4','b6','b8','c1','c3','c5','c7','d2','d4','d6','d8','e1','e3','e5','e7','f2','f4','f6','f8','g1','g3','g5','g7','h2','h4','h6','h8']
lights = ['a2','a4','a6','a8','b1','b3','b5','b7','c2','c4','c6','c8','d1','d3','d5','d7','e2','e4','e6','e8','f1','f3','f5','f7','g2','g4','g6','g8','h1','h3','h5','h7']
files = ['a','b','c','d','e','f','g','h']
ranks = [1,2,3,4,5,6,7,8]
str_ranks = ['1','2','3','4','5','6','7','8']
piece_names = ['Q','B','N','R']


class Square: # The square class is used to represent a square on the board.
    def __init__(self, file, rank, piece=None):
        self.file = file
        self.rank = rank
        self.position = file + str(rank) # It is convenient in some places to list this information in two different places.
        self.piece = piece # The piece attribute is an object which will be defined next.
        if self.piece == None:
            self.image = sprites.get_image(None,None,self.file,self.rank) # The image attribute is a list of lines that will represent the square in the terminal.
        else:
            self.image = self.piece.get_image() # This calls a method from the Piece class, which calls a function from the sprites module.
    def update_image(self): # This method will be used to change the image of the square after a move.
        if self.piece == None:
            self.image = sprites.get_image(None,None,self.file,self.rank)
        else:
            self.image = self.piece.get_image()





class Piece: # This is the class used to represent each piece.
    def __init__(self, file, rank, color, type):
        self.rank = rank
        self.file = file
        self.color = color
        self.square = file + str(rank)
        self.type = type
        if self.type == 'king': # If the king moves, it loses castling rights. The same is true if one of the rooks moves; the king can no longer castle on that side. These attributes will be used to keep track of castling rights.
            self.short_castle_rights = True
            self.long_castle_rights = True
        elif self.type == 'pawn': # When a pawn moves forward two squares, for one move, it can be captured sideways via en passant. This attribute keeps track of this.
            self.en_passant_possible = False
    def get_image(self):
        return sprites.get_image(self.type,self.color,self.file,self.rank) # This calls the function from the sprites module which determines what a square looks like based on the piece type on the square and the color of the square.
    def update_square(self,new_square):
        self.square = new_square
        self.file = self.square[0]
        self.rank = self.square[1]

a2_pawn = Piece('a',2,'white','pawn') # These are all of the pieces in a chess game.
b2_pawn = Piece('b',2,'white','pawn')
c2_pawn = Piece('c',2,'white','pawn')
d2_pawn = Piece('d',2,'white','pawn')
e2_pawn = Piece('e',2,'white','pawn')
f2_pawn = Piece('f',2,'white','pawn')
g2_pawn = Piece('g',2,'white','pawn')
h2_pawn = Piece('h',2,'white','pawn')
a1_rook = Piece('a',1,'white','rook')
b1_knight = Piece('b',1,'white','knight')
c1_bishop = Piece('c',1,'white','bishop')
d1_queen = Piece('d',1,'white','queen')
e1_king = Piece('e',1,'white','king')
f1_bishop = Piece('f',1,'white','bishop')
g1_knight = Piece('g',1,'white','knight')
h1_rook = Piece('h',1,'white','rook')
a7_pawn = Piece('a',7,'black','pawn')
b7_pawn = Piece('b',7,'black','pawn')
c7_pawn = Piece('c',7,'black','pawn')
d7_pawn = Piece('d',7,'black','pawn')
e7_pawn = Piece('e',7,'black','pawn')
f7_pawn = Piece('f',7,'black','pawn')
g7_pawn = Piece('g',7,'black','pawn')
h7_pawn = Piece('h',7,'black','pawn')
a8_rook = Piece('a',8,'black','rook')
b8_knight = Piece('b',8,'black','knight')
c8_bishop = Piece('c',8,'black','bishop')
d8_queen = Piece('d',8,'black','queen')
e8_king = Piece('e',8,'black','king')
f8_bishop = Piece('f',8,'black','bishop')
g8_knight = Piece('g',8,'black','knight')
h8_rook = Piece('h',8,'black','rook')

pawns = [a2_pawn,b2_pawn,c2_pawn,d2_pawn,e2_pawn,f2_pawn,g2_pawn,h2_pawn,a7_pawn,b7_pawn,c7_pawn,d7_pawn,e7_pawn,f7_pawn,g7_pawn,h7_pawn]


a1 = Square('a',1,a1_rook) # These are all of the squares. The pieces that start on each of the squares are set as attributes of the square objects.
a2 = Square('a',2,a2_pawn)
a3 = Square('a',3)
a4 = Square('a',4)
a5 = Square('a',5)
a6 = Square('a',6)
a7 = Square('a',7,a7_pawn)
a8 = Square('a',8,a8_rook)
b1 = Square('b',1,b1_knight)
b2 = Square('b',2,b2_pawn)
b3 = Square('b',3)
b4 = Square('b',4)
b5 = Square('b',5)
b6 = Square('b',6)
b7 = Square('b',7,b7_pawn)
b8 = Square('b',8,b8_knight)
c1 = Square('c',1,c1_bishop)
c2 = Square('c',2,c2_pawn)
c3 = Square('c',3)
c4 = Square('c',4)
c5 = Square('c',5)
c6 = Square('c',6)
c7 = Square('c',7,c7_pawn)
c8 = Square('c',8,c8_bishop)
d1 = Square('d',1,d1_queen)
d2 = Square('d',2,d2_pawn)
d3 = Square('d',3)
d4 = Square('d',4)
d5 = Square('d',5)
d6 = Square('d',6)
d7 = Square('d',7,d7_pawn)
d8 = Square('d',8,d8_queen)
e1 = Square('e',1,e1_king)
e2 = Square('e',2,e2_pawn)
e3 = Square('e',3)
e4 = Square('e',4)
e5 = Square('e',5)
e6 = Square('e',6)
e7 = Square('e',7,e7_pawn)
e8 = Square('e',8,e8_king)
f1 = Square('f',1,f1_bishop)
f2 = Square('f',2,f2_pawn)
f3 = Square('f',3)
f4 = Square('f',4)
f5 = Square('f',5)
f6 = Square('f',6)
f7 = Square('f',7,f7_pawn)
f8 = Square('f',8,f8_bishop)
g1 = Square('g',1,g1_knight)
g2 = Square('g',2,g2_pawn)
g3 = Square('g',3)
g4 = Square('g',4)
g5 = Square('g',5)
g6 = Square('g',6)
g7 = Square('g',7,g7_pawn)
g8 = Square('g',8,g8_knight)
h1 = Square('h',1,h1_rook)
h2 = Square('h',2,h2_pawn)
h3 = Square('h',3)
h4 = Square('h',4)
h5 = Square('h',5)
h6 = Square('h',6)
h7 = Square('h',7,h7_pawn)
h8 = Square('h',8,h8_rook)

board = [[a8,b8,c8,d8,e8,f8,g8,h8], # This array will be used to display the board and to process moves.
         [a7,b7,c7,d7,e7,f7,g7,h7],
         [a6,b6,c6,d6,e6,f6,g6,h6],
         [a5,b5,c5,d5,e5,f5,g5,h5],
         [a4,b4,c4,d4,e4,f4,g4,h4],
         [a3,b3,c3,d3,e3,f3,g3,h3],
         [a2,b2,c2,d2,e2,f2,g2,h2],
         [a1,b1,c1,d1,e1,f1,g1,h1]]

# This list of diagonals will be useful for testing the legality of bishop and queen moves.
diagonals = [[a1,b2,c3,d4,e5,f6,g7,h8],[b1,c2,d3,e4,f5,g6,h7],[c1,d2,e3,f4,g5,h6],[d1,e2,f3,g4,h5],[e1,f2,g3,h4],[f1,g2,h3],[g1,h2],[a2,b3,c4,d5,e6,f7,g8],[a3,b4,c5,d6,e7,f8],[a4,b5,c6,d7,e8],[a5,b6,c7,d8],[a6,b7,c8],[a7,b8],
[a2,b1],[a3,b2,c1],[a4,b3,c2,d1],[a5,b4,c3,d2,e1],[a6,b5,c4,d3,e2,f1],[a7,b6,c5,d4,e3,f2,g1],[a8,b7,c6,d5,e4,f3,g2,h1],[b8,c7,d6,e5,f4,g3,h2],[c8,d7,e6,f5,g4,h3],[d8,e7,f6,g5,h4],[e8,f7,g6,h5],[f8,g7,h6],[g8,h7]]

def print_board(board):
    os.system('clear') # Clears the terminal screen.
    for row in board: # These nested loops print each line of the top 8 squares, then each line of the next 8, until the bottom of the board.
        for line in range(0,len(row[0].image)):
            for square in row:
                print(square.image[line], end='')
            print('')

print_board(board) # Prints the starting position.

def find_pawn_move(file,rank,move_color=move_color): # This function tests if a pawn move input is legal.
    if globals()[file + str(rank)].piece != None: # This statement returns None if a pawn is attempting to move onto an occupied square.
        return None
    if move_color == 'white': # White and black pawns move in opposite directions, so the code must be distinguished.
                if rank == 1 or rank == 2:
                    return None # White pawns start on the 2nd rank, so it is illegal to move a white pawn onto the 1st or 2nd rank.
                if globals()[file + str(int(rank) - 1)].piece != None: # Testing to see if the previous square had a white pawn.
                    if globals()[file + str(int(rank) - 1)].piece.type == 'pawn':
                        if globals()[file + str(int(rank) - 1)].piece.color == 'white':
                            return file + str(int(rank) - 1) # If there was a pawn on the previous square, this square's name is returned.
                elif globals()[file + str(int(rank) - 2)].piece != None: # Testing if the pawn was jumping 2 squares from the starting square.
                    if globals()[file + str(int(rank) - 2)].piece.type == 'pawn' and globals()[file + str(int(rank) - 2)].piece.color == 'white' and globals()[file + str(int(rank) - 1)].piece == None and int(rank) - 2 == 2:
                        globals()[file + str(int(rank) - 2)].piece.en_passant_possible = True # A pawn is jumping two squares, so it can be taken en passant.
                        return file + str(int(rank) - 2) # Returns the pawn's square's name.
                else:
                    return None # No legal pawn move was found
    if move_color == 'black': # Same as for white, but with pawns moving in the opposite direction.
            if rank == 7 or rank == 8:
                return None
            if globals()[file + str(int(rank) + 1)].piece != None:
                if globals()[file + str(int(rank) + 1)].piece.type == 'pawn' and globals()[file + str(int(rank) + 1)].piece.color == 'black':
                    return file + str(int(rank) + 1)
            elif globals()[file + str(int(rank) + 2)].piece != None:
                if globals()[file + str(int(rank) + 2)].piece.type == 'pawn' and globals()[file + str(int(rank) + 2)].piece.color == 'black' and globals()[file + str(int(rank) + 1)].piece == None and int(rank) + 2 == 7:
                    globals()[file + str(int(rank) + 2)].piece.en_passant_possible = True
                    return file + str(int(rank) + 2)
            else:
                return None
            
def process_specification(squares,specification): # This function receives a list of potential moves and a specifier of either the rank or the file.
    if specification in files: 
        for square in squares: # If the specifier is a file, it loops over each move and checks if the move's file matches the specifier file.
            if square[0] == specification: # square[0] is the first point in a square's name, e.g. for 'e4' it is 'e', which is the file.
                return square
    if str(specification) in str_ranks:
        for square in squares: # Here, it does the same for the moves' ranks.
            if square[1] == specification:
                return square

def find_bishop_move(final_square_object,piece_type,move_color,specification):
    solution = [] # This function receives a final destination as an input and locates the square a bishop could legally move there from.
    for diagonal in diagonals: # This loops over every diagonal and adds the diagonals that the destination square is on to solution
        if final_square_object in diagonal:
            solution.append(diagonal)
    bishop_squares = []
    for s in solution: # This loops over each diagonal the final square is on.
        index = s.index(final_square_object)
        for square in s[index+1:]: # This loops over every square to the right of the square the piece is attempting to move onto on the diagonal.
            if square.piece != None:
                if square.piece.type == piece_type and square.piece.color == move_color:
                    bishop_squares.append(square.file + str(square.rank)) # If the correct piece is on the square, a solution has been found and is added to the list.
                else: # If the square has another piece on it, the diagonal is blocked, and the loop must end.
                    break
        if index != 0:
            for square in s[index-1::-1]: # This loop is the same but moves in the opposite direction.
                if square.piece != None:
                    if square.piece.type == piece_type and square.piece.color == move_color:
                        bishop_squares.append(square.file + str(square.rank))
                    else:
                        break
    if bishop_squares != [] and specification == 'checking for check': # This specification is used to indicate that the function is being used only to check if a square is attacked, so the specification function can be skipped.
            return bishop_squares
    if piece_type == 'queen': # The bishop move function is used as a part of the queen move function, and the list of squares is returned to that function here.
        return bishop_squares
    if len(bishop_squares) == 1 and specification == None:
        return bishop_squares[0] # If there is only one possible square, no more work is needed.
    if len(bishop_squares) > 1 and specification != None:
        return process_specification(bishop_squares,specification) # If there are two solutions, it must be determined which is correct with the specifier function.
        
def find_rook_move(final_square_object,piece_type,move_color,specification): # The rook move function works similarly to the bishop move function, but instead of iterating over diagonals, it iterates over files and ranks.
    rank_index = abs(final_square_object.rank - 8) # These two variables are the index of the destination square vertically and horizontally on the board.
    vert_index = board[rank_index].index(final_square_object)
    rook_squares = []
    for square in board[rank_index][vert_index+1:]: # This loop iterates over the squares to the right of the destination square on its rank.
        if square.piece != None:
            if square.piece.type == piece_type and square.piece.color == move_color:
                rook_squares.append(square.file + str(square.rank)) # This is the same logic as the bishop move.
            break
    if vert_index != 0:
        for square in board[rank_index][vert_index-1::-1]: # This iterates over the squares to the left of the destination square.
            if square.piece != None:
                if square.piece.type == piece_type and square.piece.color == move_color:
                    rook_squares.append(square.file + str(square.rank))
                break
    for rank in board[rank_index+1:]: # This loop iterates down the board.
        square = rank[vert_index]
        if square.piece != None:
            if square.piece.type == piece_type and square.piece.color == move_color:
                rook_squares.append(square.file + str(square.rank))
            break
    if rank_index != 0: # This loop iterates up the board.
        for rank in board[rank_index-1::-1]:
            square = rank[vert_index]
            if square.piece != None:
                if square.piece.type == piece_type and square.piece.color == move_color:
                    rook_squares.append(square.file + str(square.rank))
                break
    if rook_squares != [] and specification == 'checking for check':
            return rook_squares
    if piece_type == 'queen': # This function is also used in the queen move function.
        return rook_squares
    if len(rook_squares) == 1 and specification == None:
        return rook_squares[0]
    if len(rook_squares) > 1 and specification != None:
        return process_specification(rook_squares,specification)

def find_knight_move(final_square_object,move_color,specification): # This function is similar to the previous two, but for knight moves.
    rank_index = abs(final_square_object.rank - 8)
    vert_index = board[rank_index].index(final_square_object)
    move_index_init = [[rank_index-2,vert_index-1],[rank_index-2,vert_index+1],[rank_index-1,vert_index-2],[rank_index-1,vert_index+2],[rank_index+1,vert_index+2],[rank_index+1,vert_index-2],[rank_index+2,vert_index+1],[rank_index+2,vert_index-1]]
    move_index_final = [] # The move_index_init generates a list of all possible squares a knight could be moving to the destination square from.
    for move in move_index_init:
        if ((0 <= move[0] <= 7) == True) and ((0 <= move[1] <= 7) == True):
            move_index_final.append(board[move[0]][move[1]]) # This loop ensures that the move index list contains only squares that are actually on the chess board.
    knight_squares = []
    for square in move_index_final:
        if square.piece != None: # Similar to the bishop and knight move functions, this loop checks for a knight of the correct color in the list of possible starting squares.
            if square.piece.type == 'knight' and square.piece.color == move_color:
                knight_squares.append(square.position)
    if knight_squares != [] and specification == 'checking for check':
        return knight_squares
    if len(knight_squares) == 1 and specification == None: # If there is only one legal knight move, and there is no specifier, the starting square is returned.
        return knight_squares[0]
    if len(knight_squares) > 1 and specification != None:
        return process_specification(knight_squares,specification)

def find_king_move(final_square_object,move_color,find_list=False): # This function works very similarly to the knight move function, with a list manually created of all legal king moves.
    rank_index = abs(final_square_object.rank - 8)
    vert_index = board[rank_index].index(final_square_object)
    move_index_init = [[rank_index-1,vert_index-1],[rank_index-1,vert_index+1],[rank_index+1,vert_index-1],[rank_index+1,vert_index+1],[rank_index+1,vert_index],[rank_index-1,vert_index],[rank_index,vert_index+1],[rank_index,vert_index-1]]
    move_index_final = [] # move_index_init is the list of all 8 squares a king can move onto based on its current position.
    for move in move_index_init: # This loop removes moves that would put the king off the board.
        if ((0 <= move[0] <= 7) == True) and ((0 <= move[1] <= 7) == True):
            move_index_final.append(board[move[0]][move[1]])
    if find_list == True: # This statement is used in tests for stalemate and checkmate in order to generate a list of possible squares a king can move onto
        non_friendly_squares = []
        for square in move_index_final:
            if square.piece != None:
                if square.piece.color != move_color:
                    non_friendly_squares.append(square)
            else:
                non_friendly_squares.append(square)
        return non_friendly_squares
    for square in move_index_final:
        if square.piece != None:
            if square.piece.type == 'king' and square.piece.color == move_color:
                square.piece.short_castle_rights = False
                square.piece.long_castle_rights = False
                return square.position

def find_queen_move(final_square_object, piece_type, move_color, specification):
    queen_squares = [] # This function combines rook and bishop moves to find possible queen moves.
    if find_rook_move(final_square_object, piece_type, move_color, specification) != None:
        queen_squares.append(find_rook_move(final_square_object, piece_type, move_color, specification))
    if find_bishop_move(final_square_object,piece_type, move_color, specification) != None:
        queen_squares.append(find_bishop_move(final_square_object,piece_type, move_color, specification))
    unnested_squares = []
    for list in queen_squares:
        for move in list: # Because the bishop and rook moves return lists, it is necessary to unnest the lists into one list as is done here.
            unnested_squares.append(move)
    if unnested_squares != [] and specification == 'checking for check':
            if len(unnested_squares) > 1:
                return unnested_squares[0] + unnested_squares[1]
            else:
                return unnested_squares[0]
    if len(unnested_squares) == 1 and specification == None:
        return unnested_squares[0]
    if len(unnested_squares) > 1 and specification != None:
        return process_specification(unnested_squares, specification)


def find_init_square(piece_type,final_square_object,specification):
    file = final_square_object.file # This is the master function which determines which of the piece functions should be called.
    assert type(piece_type) == str, 'The piece type was not input correctly'
    rank = final_square_object.rank
    if piece_type == 'pawn':
        return find_pawn_move(file, rank, move_color)
    if piece_type == 'rook':
        return find_rook_move(final_square_object, piece_type, move_color, specification)
    if piece_type == 'knight':
        return find_knight_move(final_square_object, move_color, specification)
    if piece_type == 'queen':
        return find_queen_move(final_square_object, piece_type, move_color, specification)
    if piece_type == 'bishop':
        return find_bishop_move(final_square_object, piece_type, move_color, specification)
    if piece_type == 'king':
        return find_king_move(final_square_object, move_color)

def find_pawn_capture(init_file,final_square_object,move_color,is_check_test): # This function tests for legal pawn captures.
    init_file_index = files.index(init_file)
    final_file_index = files.index(final_square_object.file)
    if init_file_index + 1 != final_file_index and init_file_index - 1 != final_file_index:
        return None
    if move_color == 'white':
        if final_square_object.rank == 1 or final_square_object.rank == 2:
            return None # Makes sure the pawn isn't capturing on an impossible square
        init_square = globals()[init_file + str(final_square_object.rank - 1)]
    else:
        if final_square_object.rank == 7 or final_square_object.rank == 8:
            return None # Makes sure the pawn isn't capturing on an impossible square
        init_square = globals()[init_file + str(final_square_object.rank + 1)]
    if init_square.piece == None:
            return None
    elif init_square.piece.color != move_color or init_square.piece.type != 'pawn':
            return None
    elif final_square_object.piece == None and is_check_test == False: # Testing for en passant
        vert_index = 0
        file_index = 0
        for i in range(0,8): # Locating the square of the possible capturable pawn.
            if final_square_object in board[i]: # This for loop just finds the index of i within board.
                vert_index = i
                file_index = board[i].index(final_square_object)
        if move_color == 'white':
            if vert_index == 7:
                return None
            else:
                vert_index += 1
        else:
            if vert_index == 0:
                return None
            else:
                vert_index -= 1
        en_passant_square = board[vert_index][file_index]
        if en_passant_square.piece != None: # Tests if there is a pawn which can be captured via en passant.
            if en_passant_square.piece.type == 'pawn' and en_passant_square.piece.color != move_color:
                if en_passant_square.piece.en_passant_possible == True:
                    return ['pawn',init_square.position,final_square_object.position,en_passant_square.position,True]
        return None
    elif is_check_test == True:
        return [init_square.position]
    else:
        return ['pawn',init_square.position,final_square_object.position,final_square_object.position,True]
    
def find_pawn_promote(final_square,move_color,promote_to): # This function finds possible pawn promotions.
    if final_square.piece != None:
        return None
    if move_color == 'white':
        if final_square.rank != 8:
            return None
        if globals()[final_square.file + '7'].piece != None:
            if globals()[final_square.file + '7'].piece.type == 'pawn' and globals()[final_square.file + '7'].piece.color == 'white':
                return ['promoting',final_square.file + '7',final_square.position,final_square.position,promote_to]
    else:
        if final_square.rank != 1:
            return None
        if globals()[final_square.file + '2'].piece != None:
            if globals()[final_square.file + '2'].piece.type == 'pawn' and globals()[final_square.file + '2'].piece.color == 'black':
                return ['promoting',final_square.file + '2',final_square.position,final_square.position,promote_to]
            
def find_pawn_capture_promote(init_file,final_square,move_color,promote_to): # This function finds pawn promotions by capturing.
    init_file_index = files.index(init_file)
    final_file_index = files.index(final_square.file)
    if init_file_index + 1 != final_file_index and init_file_index - 1 != final_file_index:
        return None # Ensures pawn is on a valid file
    if final_square.piece == None:
        return None # Ensures pawn is actually capturing an enemy piece
    elif final_square.piece.color == move_color:
        return None
    if move_color == 'white':
        if final_square.rank != 8:
            return None
        init_square = globals()[init_file + '7']
    else:
        if final_square.rank != 1:
            return None
        init_square = globals()[init_file + '2']
    if init_square.piece == None:
            return None
    elif init_square.piece.color != move_color or init_square.piece.type != 'pawn':
            return None
    if move_color == 'white':
        return ['promoting',init_square.position,final_square.position,final_square.position,promote_to]
    else:
        return ['promoting',init_square.position,final_square.position,final_square.position,promote_to]
    
def find_check(square,move_color=move_color,stalemate_check=False): # This function finds if a square is attacked by any of one side's pieces, which, when used on the square the king is on, can be used to test for check.
    file_indices = [files.index(square.file)+1,files.index(square.file)-1] # Lists possible files for a pawn to attack from
    pawn_files = []
    for i in file_indices:
        if 0 <= i <= 7: # Finds pawn files that are actually on the board.
            pawn_files.append(files[i])
    checking_pieces = []
    for file in pawn_files: # Checks for pawn captures on all possible files.
        if stalemate_check == False:
            checking_pieces.append(find_pawn_capture(file,square,move_color,True))
        else:
            checking_pieces.append(find_pawn_move(file,square.rank,move_color))
            if type(find_pawn_capture(file,square,move_color,True)) == list:
                if globals()[find_pawn_capture(file,square,move_color,True)[0]].piece != None:
                    if globals()[find_pawn_capture(file,square,move_color,True)[0]].piece.color != move_color:
                        checking_pieces.append(find_pawn_capture(file,square,move_color,True))
    checking_pieces.append(find_bishop_move(square,'bishop',move_color,'checking for check')) # Here a list is created of all of the moves which are attacking a given square
    checking_pieces.append(find_rook_move(square,'rook',move_color,'checking for check'))
    checking_pieces.append(find_queen_move(square,'queen',move_color,'checking for check'))
    checking_pieces.append(find_knight_move(square,move_color,'checking for check'))
    if find_king_move(square,move_color) != None:
        checking_pieces.append('king move') # The king move is irrelevant for the purposes of this function.
    final_list = [i for i in checking_pieces if i != None] # This comprehension removes the Nones, which are used in different situations to handle errors
    if final_list != []:
        return final_list
    else:
        return False
    
def find_short_castle(): # This function checks if a side can castle kingside.
    if move_color == 'white':
        if e1_king.short_castle_rights == False:
            return None
        elif (find_check(e1,'black') or find_check(f1,'black') or find_check(g1,'black')) != False:
            return None
        elif f1.piece != None or g1.piece != None:
            return None
        else:
            e1_king.long_castle_rights = False
            e1_king.short_castle_rights = False
            return 'castles short'
    else:
        if e8_king.short_castle_rights == False:
            return None
        elif (find_check(e8,'white') or find_check(f8,'white') or find_check(g8,'white')) != False:
            return None
        elif f8.piece != None or g8.piece != None:
            return None
        else:
            e8_king.long_castle_rights = False
            e8_king.short_castle_rights = False
            return 'castles short'
        
def find_long_castle(): # This function checks if a side can castle queenside.
    if move_color == 'white':
        if e1_king.long_castle_rights == False:
            return None
        elif (find_check(e1,'black') or find_check(d1,'black') or find_check(c1,'black') or find_check(b1,'black')) != False:
            return None
        elif d1.piece != None or c1.piece != None or b1.piece != None:
            return None
        else:
            e1_king.long_castle_rights = False
            e1_king.short_castle_rights = False
            return 'castles long'
    else:
        if e8_king.long_castle_rights == False:
            return None
        elif (find_check(e8,'white') or find_check(d8,'white') or find_check(c8,'white') or find_check(b8,'white')) != False:
            return None
        elif d8.piece != None or c8.piece != None or b8.piece != None:
            return None
        else:
            e8_king.long_castle_rights = False
            e8_king.short_castle_rights = False
            return 'castles long'
                    
def interpret_move(move): # This function analyzes user input to interpret the intended move.
    try: # This try statement ensures the input can be comprehended by the program.
        promote_to = None
        if move == 'O-O': # These are the symbols for castling.
            return find_short_castle()
        elif move == 'O-O-O':
            return find_long_castle()
        is_capture = False
        specification = None
        if move[0] in files: # This checks if the move is a pawn move, because the first letter in a pawn move is the file it is starting on.
            piece_type = 'pawn'
            if len(move) == 2: 
                if 1 <= int(move[1]) <= 7:
                    final_square = move[0] + move[1] # The 
                    final_square_object = globals()[final_square]
                else:
                    return None
            elif len(move) == 4:
                if move[1] == 'x': # 'x' denotes a capture
                    is_capture = True
                    if move[2] in files and (1 <= int(move[3]) <= 7):
                        final_square = move[2] + move[3]
                        final_square_object = globals()[final_square]
                elif move[2] == '=':
                    if move[1] == '8' and move[3] in piece_names:
                        final_square = move[0] + move[1]
                        final_square_object = globals()[final_square]
                        promote_to = move[3]
                else:
                    return None
            elif len(move) == 6:
                if move[1] == 'x' and move[2] in files and (1 <= int(move[3]) <= 8) and move[4] == '=' and move[5] in piece_names:
                    is_capture = True
                    final_square = move[2] + move[3]
                    final_square_object = globals()[final_square]
                    promote_to = move[5]
            else:
                return None
        elif move[0] == 'K':
            piece_type = 'king'
            if len(move) == 3 and move[1] in files and (1 <= int(move[2]) <= 8):
                final_square = move[1] + move[2]
                final_square_object = globals()[final_square]
            elif len(move) == 4 and move[1] == 'x' and move[2] in files and (1 <= int(move[3]) <= 8):
                final_square = move[2] + move[3]
                final_square_object = globals()[final_square]
            else:
                return None
        elif move[0] == 'Q': # Here the piece symbol is changed into the piece name for convenience throughout the program
            piece_type = 'queen'
        elif move[0] == 'B':
            piece_type = 'bishop'
        elif move[0] == 'R':
            piece_type = 'rook'
        elif move[0] == 'N':
            piece_type = 'knight'
        else:
            return None
        if piece_type != 'pawn' and piece_type != 'king': # This if block looks at cases of piece moves which are not pawns or kings.
            if len(move) == 3 and move[1] in files and (1 <= int(move[2]) <= 8):
                final_square = move[1] + move[2] # The destination square is identified here for 3 character moves.
                final_square_object = globals()[final_square]
            elif len(move) == 4: # If it is a 4 character move, it could be a capture, or it could be a case of a piece being specified (e.g. moving the g knight to e2 versus the c knight, Nge2 versus Nce2)
                if move[1] == 'x' and move[2] in files and (1 <= int(move[3]) <= 8):
                    is_capture = True
                    final_square = move[2] + move[3]
                    final_square_object = globals()[final_square]
                elif move[1] in (files + str_ranks) and move[2] in files and (1 <= int(move[3]) <= 8):
                    specification = move[1]
                    final_square = move[2] + move[3]
                    final_square_object = globals()[final_square]
            elif len(move) == 5:
                if move[1] in (files + str_ranks) and move[2] == 'x' and move[3] in files and (1 <= int(move[4]) <= 8):
                    specification = move[1]
                    is_capture = True
                    final_square = move[3] + move[4]
                    final_square_object = globals()[final_square]
            else:
                return None
        if final_square_object.piece != None: # Checks if attempting to move onto a square occupied by a friendly piece
            if final_square_object.piece.color == move_color:
                return None
        if promote_to != None:
            if promote_to == 'Q': # Here, the piece the pawn is promoting to is noted
                promote_to = 'queen'
            elif promote_to == 'B':
                promote_to = 'bishop'
            elif promote_to == 'R':
                promote_to = 'rook'
            elif promote_to == 'N':
                promote_to = 'knight'
        if piece_type == 'pawn' and is_capture == True: # The pawn capture function is called here
            if promote_to != None:
                return find_pawn_capture_promote(move[0],final_square_object,move_color,promote_to)
            return find_pawn_capture(move[0],final_square_object,move_color,False)
        if piece_type == 'pawn' and promote_to != None: # The pawn promotion function is called here
            return find_pawn_promote(final_square_object,move_color,promote_to)
        if is_capture == True and final_square_object.piece == None: # Checks if player attempts to capture nothing
            return None
        else:
            init_square = find_init_square(piece_type,final_square_object,specification) # The general function is called here to test where a piece could be moving from.
            return [piece_type, init_square, final_square, final_square, is_capture]
    except:
        return None
    
def process_castling(side): # This function performs the operations of castling.
    assert type(side) == str, 'The castling function was called with the wrong type of data for the parameter'
    if side == 'castles short':
        if move_color == 'white':
            g1.piece = e1_king # These statements just manually change the positions of the king and rook depending on the type of castling and the player castling.
            f1.piece = h1_rook
            e1.piece = None
            h1.piece = None
            e1_king.update_square('g1')
            h1_rook.update_square('f1')
            e1.update_image()
            f1.update_image()
            g1.update_image()
            h1.update_image()
        else:
            g8.piece = e8_king
            f8.piece = h8_rook
            e8.piece = None
            h8.piece = None
            e8_king.update_square('g8')
            h8_rook.update_square('f8')
            e8.update_image()
            f8.update_image()
            g8.update_image()
            h8.update_image()
    else:
        if move_color == 'white':
            c1.piece = e1_king
            d1.piece = h1_rook
            e1.piece = None
            a1.piece = None
            e1_king.update_square('c1')
            a1_rook.update_square('d1')
            e1.update_image()
            a1.update_image()
            c1.update_image()
            d1.update_image()
        else:
            c8.piece = e8_king
            d8.piece = h8_rook
            e8.piece = None
            a8.piece = None
            e8_king.update_square('c8')
            a8_rook.update_square('d8')
            e8.update_image()
            a8.update_image()
            c8.update_image()
            d8.update_image()

def can_defend_file(attack_square,defend_square_name,move_color,getting_list):
    file_index = 0
    for square in board[0]: # Finds index of the relevant file
        if defend_square_name[0] == square.file:
            file_index = board[0].index(square)
    attack_rank_index = abs(attack_square.rank - 8)
    defend_rank_index = abs(int(defend_square_name[1]) - 8)
    new_list = []
    if attack_rank_index < defend_rank_index: # Loops over relevant squares to see if the attack can be blocked
        for rank in board[attack_rank_index:defend_rank_index]:
            if getting_list == True:
                new_list.append(rank[file_index])
            elif find_check(rank[file_index],move_color) != None and find_check(rank[file_index],move_color) != ['king move']:
                return True
    else:
        for rank in board[attack_rank_index:defend_rank_index:-1]:
            if getting_list == True:
                new_list.append(rank[file_index])
            elif find_check(rank[file_index],move_color) != None and find_check(rank[file_index],move_color) != ['king move']:
                return True
    if getting_list == True:
        return new_list
            
def can_defend_rank(attack_square,defend_square_name,move_color,getting_list):
    for rank in board: # This function is the same as above, only for a rank instead of for a file.
        if attack_square in rank:
            attack_file_index = rank.index(attack_square)
            defend_file_index = rank.index(globals()[defend_square_name])
            if attack_file_index < defend_file_index:
                if getting_list == True:
                    return rank[attack_file_index:defend_file_index]
                for square in rank[attack_file_index:defend_file_index]:
                    if find_check(square,move_color) == False or find_check(square,move_color) != ['king move']:
                        return True
            else:
                if getting_list == True:
                    return rank[attack_file_index:defend_file_index:-1]
                for square in rank[attack_file_index:defend_file_index:-1]:
                    if find_check(square,move_color) == False or find_check(square,move_color) != ['king move']:
                        return True

def can_defend_diagonal(attack_square,defend_square_name,move_color,getting_list):
    for diagonal in diagonals: # Same as above two functions, only for diagonal attacks.
        if attack_square in diagonal and globals()[defend_square_name] in diagonal:
            attack_index = diagonal.index(attack_square)
            defend_index = diagonal.index(globals()[defend_square_name])
            if attack_index < defend_index:
                if getting_list == True:
                    return diagonal[attack_index:defend_index]
                for square in diagonal[attack_index:defend_index]:
                    if find_check(square,move_color) == False or find_check(square,move_color) != ['king move']:
                        return True
            else:
                if getting_list == True:
                    return diagonal[attack_index:defend_index:-1]
                for square in diagonal[attack_index:defend_index:-1]:
                    if find_check(square,move_color) == False or find_check(square,move_color) != ['king move']:
                        return True
            
def is_attack_stoppable(attack_square,defend_square_name,move_color,getting_list=False): # Here, move_color is the color that has to block.
    if attack_square.piece.type == 'knight' or attack_square.piece.type == 'pawn': # This function combines three functions to test if an attack on the king can be blocked.
        if getting_list == True:
            return [attack_square]
        if find_check(attack_square,move_color) == False:
            return False
    if attack_square.file == defend_square_name[0]:
        return can_defend_file(attack_square,defend_square_name,move_color,getting_list)
    elif str(attack_square.rank) == defend_square_name[1]:
        return can_defend_rank(attack_square,defend_square_name,move_color,getting_list)
    else:
        return can_defend_diagonal(attack_square,defend_square_name,move_color,getting_list)
         
def is_checkmate(move_color): # This is the function which determines if the king is in checkmate
    if move_color == 'white':
        king_square = globals()[e8_king.square]
        defend_color = 'black'
    else:
        king_square = globals()[e1_king.square]
        defend_color = 'white'
    if find_check(king_square,move_color) != False: # Checks if the king is in check
        king_moves = find_king_move(king_square,defend_color,True)
        for move in king_moves:
            if find_check(move,move_color) == False: # Checks if the king can't move
                return None
        attacking_squares = find_check(king_square,move_color)
        if len(attacking_squares) > 1: # Checks if it is a double check
            return True
        else:
            if type(attacking_squares[0]) == list:
                attacking_square_object = globals()[attacking_squares[0][0]]
            else:
                attacking_square_object = globals()[attacking_squares[0]]
            return not is_attack_stoppable(attacking_square_object,king_square.position,defend_color) # A function is run to determine if the attack can be blocked by another piece.

def is_stalemate(move_color): # This function checks to see if a position is stalemate.
    if move_color == 'white':
        king_square = globals()[e8_king.square]
        defend_color = 'black'
    else:
        king_square = globals()[e1_king.square]
        defend_color = 'white'
    if find_check(king_square,move_color) == False: # Checks if king is not in check
        king_moves = find_king_move(king_square,defend_color,True) # Lists possible squares the king can move to
        for move in king_moves:
            if find_check(move,move_color) == False: # Checks if the king can't move
                return None # If the king can move, it is not stalemate
        for rank in board:
            for square in rank: # These nested loops check every square on the board to see if there are any legal moves to be made.
                if square.piece != None:
                    if square.piece.color == defend_color:
                        continue
                if find_check(square,defend_color,True) != False and find_check(square,defend_color,True) != ['king move']:
                    test_square = find_check(square,defend_color,True)
                    if type(test_square[0]) == list: # Converts list square into a string
                        test_square = test_square[0][0]
                    else:
                        test_square = test_square[0]
                    test_piece = globals()[test_square].piece
                    globals()[test_square].piece = None # This removes the piece from the board temporarily
                    if find_check(king_square,move_color) != False: # With the piece removed, the program checks if the king is in check. If the king is now in check, moving the piece must be illegal, so this piece is skipped in the test for moveable pieces.
                        globals()[test_square].piece = test_piece # The piece is returned to teh board
                        continue
                    else:
                        globals()[test_square].piece = test_piece
                        return None
        return True

moves_dict = dict() # This dictionary will keep track of all of the moves of the game.
move_number = 1

def do_move():
    global move_color
    global moves_dict
    global move_number
    move = input(f'{move_color} to move: ')
    if move == 'resign':
        return 'resign'
    sol = interpret_move(move)
    if type(sol) != str:
        if sol == None:
            return None
        if sol[1] == None:
            return None
        init_square_object = globals()[sol[1]] # This code changes the pieces which are attributed to the square objects related to the move, and changes the square attributes for the piece objects.
        final_square_object = globals()[sol[2]]
        init_square_piece = init_square_object.piece
        final_square_piece = final_square_object.piece
        en_passant_piece = globals()[sol[3]].piece
        if sol[0] == 'promoting': # This changes the piece type for a pawn which promotes to another piece.
            init_square_object.piece.type = sol[4]
        init_square_object.piece.update_square(sol[2])
        final_square_object.piece = init_square_object.piece
        init_square_object.piece = None
        init_square_object.update_image()
        final_square_object.update_image()
        if sol[2] != sol[3]: # Updates square if en passant
            globals()[sol[3]].piece = None
            globals()[sol[3]].update_image()
        if move_color == 'white':
            king_square = globals()[e1_king.square]
            opposite_color = 'black'
        else:
            king_square = globals()[e8_king.square]
            opposite_color = 'white'
        if find_check(king_square,opposite_color) != False: # Checks if the king is in check after the move
            init_square_object.piece = init_square_piece
            final_square_object.piece = final_square_piece
            globals()[sol[3]].piece = en_passant_piece # This code reverts back to the previous position
            init_square_object.piece.update_square(init_square_object.position)
            if final_square_object.piece != None:
                final_square_object.piece.update_square(final_square_object.position)
            init_square_object.update_image()
            final_square_object.update_image()
            globals()[sol[3]].update_image()
            return None
        if final_square_object.piece.type == 'rook': # If a rook was moved, castling rights will be removed from the king who could have castled with this rook previously.
            if final_square_object.piece == a1_rook:
                e1_king.long_castle_rights = False
            elif final_square_object.piece == h1_rook:
                e1_king.short_castle_rights = False
            elif final_square_object.piece == a8_rook:
                e8_king.long_castle_rights = False
            else:
                e8_king.short_castle_rights = False
    else:
        process_castling(sol)
    moves_dict[str(move_number) + move_color] = move # This records each move to the move dictionary, noting the move number.
    if is_checkmate(move_color) == True:
        print_board(board)
        return 'checkmate'
    if is_stalemate(move_color) == True:
        print_board(board)
        return 'draw by stalemate'
    if move_color == 'white': # Changes the move color for the next move
        move_color = 'black'
    else:
        move_number += 1
        move_color = 'white'
    for pawn in pawns: # Removes en passant possibilities for pawns which were not captured.
        if pawn.color == move_color:
            pawn.en_passant_possible = False
    print_board(board) # Prints the new board
    return True

def record_moves(moves_dict): # This function takes a list of moves and writes them to a file so that a game can be saved
    for key in moves_dict.keys():
        with open('moves_list.txt', 'a') as file:
            if key[1:] == 'white':
                file.write(f'{key[0]}.{moves_dict.get(key)}')
            else:
                file.write(f' {moves_dict.get(key)}'+ '\n')
            
while True:
    result = do_move()
    if result == None:
        print('the previous move was invalid.')
    elif result == 'resign':
        record_moves(moves_dict)
        break
    elif result == 'checkmate':
        record_moves(moves_dict)
        if move_color == 'white':
            print("white wins by checkmate.")
        else:
            print("black wins by checkmate.")
        break
    elif result == 'draw by stalemate':
        record_moves(moves_dict)
        print('the game is drawn by stalemate.')
        break


