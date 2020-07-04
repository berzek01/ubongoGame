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
# NEW BOARDS============================================================= #img4
board7=[[-1,-1,0,-1],
        [-1,-1,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [-1,0,0,0],
        [-1,0,0,0]]
groupPieces1_Board7 = [piece_t, piece_z, piece_cuadrado, piece_L4]
groupPieces2_Board7 = [piece_l3, piece_f, piece_q, piece_t]
groupPieces3_Board7 = [piece_t, piece_q, piece_cunia, piece_z]
groupPieces4_Board7 = [piece_Z, piece_f, piece_l3, piece_L]
groupPieces5_Board7 = [piece_L, piece_q, piece_f, piece_cunia]
groupPieces6_Board7 = [piece_Z, piece_L, piece_q, piece_cuadrado]
piecesB7 = [groupPieces1_Board7, groupPieces2_Board7, groupPieces3_Board7, groupPieces4_Board7, groupPieces5_Board7, groupPieces6_Board7]
# ======================================================================= #
board8=[[-1,-1,0,0,-1],
        [-1,-1,0,0,-1],
        [-1,-1,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0]]
groupPieces1_Board8 = [piece_L4, piece_t, piece_l3, piece_q]
groupPieces2_Board8 = [piece_f, piece_l2, piece_q, piece_z]
groupPieces3_Board8 = [piece_cuadrado, piece_l, piece_f, piece_L]
groupPieces4_Board8 = [piece_t, piece_L4, piece_Z, piece_cuadrado]
groupPieces5_Board8 = [piece_cunia, piece_f, piece_cuadrado, piece_z]
groupPieces6_Board8 = [piece_Z, piece_q, piece_cuadrado, piece_L]
piecesB8 = [groupPieces1_Board8, groupPieces2_Board8, groupPieces3_Board8, groupPieces4_Board8, groupPieces5_Board8, groupPieces6_Board8]
# ======================================================================= #
board9=[[-1,0,0,0,0],
        [-1,0,0,0,0],
        [0,0,0,0,0],
        [0,0,-1,0,-1]]
groupPieces1_Board9 = [piece_f, piece_l2, piece_q, piece_t]
groupPieces2_Board9 = [piece_t, piece_L4, piece_l2, piece_q]
groupPieces3_Board9 = [piece_l2, piece_q, piece_f, piece_Z]
groupPieces4_Board9 = [piece_l3, piece_cuadrado, piece_Z, piece_q]
groupPieces5_Board9 = [piece_Z, piece_q, piece_L, piece_cunia]
groupPieces6_Board9 = [piece_L, piece_l3, piece_cuadrado, piece_q]
piecesB9 = [groupPieces1_Board9, groupPieces2_Board9, groupPieces3_Board9, groupPieces4_Board9, groupPieces5_Board9, groupPieces6_Board9]
# ======================================================================= #
board10=[[-1,0,0,-1,-1],
        [0,0,0,0,-1],
        [-1,0,0,0,0],
        [-1,0,0,0,-1]]
groupPieces1_Board10 = [piece_t, piece_f, piece_Z]
groupPieces2_Board10 = [piece_Z, piece_q, piece_t]
groupPieces3_Board10 = [piece_L, piece_t, piece_L4]
groupPieces4_Board10 = [piece_l3, piece_f, piece_q]
groupPieces5_Board10 = [piece_Z, piece_q, piece_L]
groupPieces6_Board10 = [piece_L, piece_t, piece_z]
piecesB10 = [groupPieces1_Board10, groupPieces2_Board10, groupPieces3_Board10, groupPieces4_Board10, groupPieces5_Board10, groupPieces6_Board10]
# ======================================================================= #
board11=[[-1,-1,0,-1],
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [-1,-1,-1,0]]
groupPieces1_Board11 = [piece_f, piece_L4, piece_L]
groupPieces2_Board11 = [piece_t, piece_q, piece_f]
groupPieces3_Board11 = [piece_L4, piece_l, piece_q]
groupPieces4_Board11 = [piece_t, piece_z, piece_f]
groupPieces5_Board11 = [piece_z, piece_f, piece_Z]
groupPieces6_Board11 = [piece_L, piece_f, piece_q]
piecesB11 = [groupPieces1_Board11, groupPieces2_Board11, groupPieces3_Board11, groupPieces4_Board11, groupPieces5_Board11, groupPieces6_Board11]
# ======================================================================= #
board12=[[-1,0,0,-1,-1],
        [-1,0,0,0,-1],
        [0,0,0,0,0],
        [-1,-1,0,0,0]]
groupPieces1_Board12 = [piece_L, piece_t, piece_q]
groupPieces2_Board12 = [piece_t, piece_q, piece_Z]
groupPieces3_Board12 = [piece_cunia, piece_z, piece_q]
groupPieces4_Board12 = [piece_cunia, piece_q, piece_L4]
groupPieces5_Board12 = [piece_L, piece_f, piece_cuadrado]
groupPieces6_Board12 = [piece_cuadrado, piece_L4, piece_L]
piecesB12 = [groupPieces1_Board12, groupPieces2_Board12, groupPieces3_Board12, groupPieces4_Board12, groupPieces5_Board12, groupPieces6_Board12]
# ======================================================================= #
board13=[[0,0,-1,-1,-1],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0]]
groupPieces1_Board13 = [piece_L, piece_cunia, piece_z,piece_q]
groupPieces2_Board13 = [piece_l, piece_Z, piece_L,piece_f]
groupPieces3_Board13 = [piece_t, piece_f, piece_Z,piece_cuadrado]
groupPieces4_Board13 = [piece_cunia, piece_q, piece_cuadrado,piece_L4]
groupPieces5_Board13 = [piece_f, piece_cunia, piece_L4,piece_t]
groupPieces6_Board13 = [piece_cuadrado, piece_l, piece_q,piece_L]
piecesB13 = [groupPieces1_Board13, groupPieces2_Board13, groupPieces3_Board13, groupPieces4_Board13, groupPieces5_Board13, groupPieces6_Board13]
# ======================================================================= #
board14=[[-1,-1,0,0,0],
        [-1,-1,0,0,0],
        [-1,-1,0,0,0],
        [-1,-1,0,0,0],
        [0,0,0,0,0]]
groupPieces1_Board14 = [piece_l2, piece_Z, piece_z,piece_q]
groupPieces2_Board14 = [piece_f, piece_q, piece_l2,piece_L4]
groupPieces3_Board14 = [piece_l, piece_cunia, piece_L4,piece_f]
groupPieces4_Board14 = [piece_cuadrado, piece_f, piece_l3,piece_q]
groupPieces5_Board14 = [piece_L, piece_q, piece_L4,piece_l3]
groupPieces6_Board14 = [piece_f, piece_l3, piece_cuadrado,piece_L4]
piecesB14 = [groupPieces1_Board14, groupPieces2_Board14, groupPieces3_Board14, groupPieces4_Board14, groupPieces5_Board14, groupPieces6_Board14]
# ======================================================================= #
board15=[[-1,0,0,0,-1],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,-1,-1,0,0]]
groupPieces1_Board15 = [piece_l3, piece_L4, piece_t,piece_Z]
groupPieces2_Board15 = [piece_f, piece_q, piece_l3,piece_cunia]
groupPieces3_Board15 = [piece_l3, piece_z, piece_t,piece_L]
groupPieces4_Board15 = [piece_cuadrado, piece_t, piece_l3,piece_f]
groupPieces5_Board15 = [piece_L, piece_z, piece_q,piece_l2]
groupPieces6_Board15 = [piece_f, piece_q, piece_l2,piece_L]
piecesB15 = [groupPieces1_Board15, groupPieces2_Board15, groupPieces3_Board15, groupPieces4_Board15, groupPieces5_Board15, groupPieces6_Board15]
# ======================================================================= #

boards = [ 
	board2, 
	board3, 
	board4, 
	board5, 
	board6 
]
pieces = [
	piecesB2,
	piecesB3,
	piecesB4,
	piecesB5,
	piecesB6
]