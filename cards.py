# Piepiece_zas
piece_t = [
    [1,1,1],
    [0,1,0]
]
piece_q = [
    [1,1,1],
    [1,1,0]
]
piece_z = [
    [0,1,1],
    [1,1,0]
]
piece_Z = [
	[0, 1, 1],
	[0, 1, 0],
	[1, 1, 0]
]
piece_cunia = [
    [0,1],
    [1,1]
]
piece_f = [
    [1,1,1,1],
    [0,1,0,0]
]
piece_L = [
    [1,1,1],
    [1,0,0]
]
piece_cuadrado = [
    [1,1],
    [1,1]
]
piece_L4 = [
    [1,1,1,1],
    [0,0,0,1]
]
piece_l = [
	[1, 1, 1, 1]
]
piece_l2 = [
    [1,1]
]
piece_l3 = [
    [1,1,1]
]

# ======================================================================= #
board0 = [
	[0, 0, 0, 0],
	[0, 0, 0, 0],
	[0, 0, 0, 0],
	[-1, 0, 0, 0]
]

groupPieces1_Board0 = [piece_l, piece_l2, piece_z, piece_q]
piecesB0 = [groupPieces1_Board0];
# ======================================================================= #
board1 = [
	[0, 0, 0, 0],
	[0, 0, 0, 0],
	[0, 0, 0, 0],
	[-1, 0, 0, 0]
]

groupPieces1_Board1 = [piece_l, piece_l2, piece_z, piece_q]
piecesB1 = [groupPieces1_Board1];
# ======================================================================= #
board2 = [
	[-1, 0, 0, 0, 0],
	[-1, 0, 0, 0, 0],
	[-1, 0, 0, 0, -1],
	[0, 0, 0, -1, -1]
]

groupPieces1_Board2 = [piece_L4, piece_q, piece_L]
groupPieces2_Board2 = [piece_Z, piece_L4, piece_z]
groupPieces3_Board2 = [piece_L4, piece_q, piece_t]
groupPieces4_Board2 = [piece_l, piece_q, piece_f]
groupPieces5_Board2 = [piece_l, piece_q, piece_f]
groupPieces6_Board2 = [piece_l, piece_q, piece_f]
piecesB2 = [groupPieces1_Board2, groupPieces2_Board2, groupPieces3_Board2, groupPieces4_Board2, groupPieces5_Board2, groupPieces6_Board2];
# ======================================================================= #
board3 = [
	[-1, 0, 0, 0, 0],
	[-1, 0, 0, 0, 0],
	[-1, 0, 0, 0, -1],
	[0, 0, 0, -1, -1]
]


groupPieces1_Board3 = [piece_L4, piece_q, piece_L]
groupPieces2_Board3 = [piece_Z, piece_L4, piece_z]
groupPieces3_Board3 = [piece_L4, piece_q, piece_t]
groupPieces4_Board3 = [piece_l, piece_q, piece_f]
groupPieces5_Board3 = [piece_l, piece_q, piece_f]
groupPieces6_Board3 = [piece_l, piece_q, piece_f]
piecesB3 = [groupPieces1_Board3, groupPieces2_Board3, groupPieces3_Board3, groupPieces4_Board3, groupPieces5_Board3, groupPieces6_Board3]
# ======================================================================= #
board4 = [
	[0, 0, -1, -1, -1],
	[0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0]
]

groupPieces1_board4 = [piece_cuadrado, piece_l, piece_q, piece_L]
groupPieces2_board4 = [piece_f, piece_cunia, piece_L4, piece_t]
groupPieces3_board4 = [piece_cunia, piece_q, piece_cuadrado, piece_L4]
groupPieces4_board4 = [piece_t, piece_f, piece_z, piece_cuadrado]
groupPieces5_board4 = [piece_l, piece_z, piece_L, piece_f]
groupPieces6_board4 = [piece_L, piece_cunia, piece_Z, piece_q]
piecesB4 = [groupPieces1_board4, groupPieces2_board4, groupPieces3_board4, groupPieces4_board4, groupPieces5_board4, groupPieces6_board4]
# ======================================================================= #


board5 = [
	[-1, -1, 0, 0, 0],
	[-1, -1, 0, 0, 0],
	[-1, -1, 0, 0, 0],
	[-1, -1, 0, 0, 0],
	[0, 0, 0, 0, 0]
]

groupPieces1_board5 = [piece_f, piece_l3, piece_cuadrado, piece_L4]
groupPieces2_board5 = [piece_L, piece_q, piece_L4, piece_l3]
groupPieces3_board5 = [piece_cuadrado, piece_f, piece_l3, piece_q]
groupPieces4_board5 = [piece_l, piece_cunia, piece_L4, piece_f]
groupPieces5_board5 = [piece_f, piece_q, piece_l2, piece_L4]
groupPieces6_board5 = [piece_l3, piece_z, piece_Z, piece_q]
piecesB5 = [groupPieces1_board5, groupPieces2_board5, groupPieces3_board5, groupPieces4_board5, groupPieces5_board5, groupPieces6_board5]
# ======================================================================= #

board6=[
	[-1, 0, 0, 0, -1],
	[0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0],
	[0, -1, -1, 0, 0]
]

groupPieces1_board6 = [piece_l3, piece_L4, piece_t, piece_z]
groupPieces2_board6 = [piece_f, piece_q, piece_l3, piece_cunia]
groupPieces3_board6 = [piece_l3, piece_Z, piece_t, piece_L]
groupPieces4_board6 = [piece_cuadrado, piece_t, piece_l3, piece_f]
groupPieces5_board6 = [piece_L, piece_Z, piece_q, piece_l2]
groupPieces6_board6 = [piece_f, piece_q, piece_l2, piece_L]
piecesB6 = [groupPieces1_board6, groupPieces2_board6, groupPieces3_board6, groupPieces4_board6, groupPieces5_board6, groupPieces6_board6]
# ======================================================================= #



boards = [  
	board3, 
	board4, 
	board5, 
	board6 
]
pieces = [
	piecesB3,
	piecesB4,
	piecesB5,
	piecesB6
]