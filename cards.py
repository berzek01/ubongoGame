
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
board1 = [
	[0, 0, 0, 0],
	[0, 0, 0, 0],
	[0, 0, 0, 0],
	[-1, 0, 0, 0]
]

groupPieces1_Board1 = [piece_l, piece_l2, piece_z, piece_q]

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
groupDado_Board2 = [groupPieces1_Board2,groupPieces2_Board2,groupPieces3_Board2,groupPieces4_Board2,groupPieces5_Board2,groupPieces6_Board2]
# ======================================================================= #
board3 = [
	[-1, 0, 0, 0, 0],
	[-1, 0, 0, 0, 0],
	[-1, 0, 0, 0, -1],
	[0, 0, 0, -1, -1]
]
models = [board1,board2,board3]

groupPieces1_Board3 = [piece_L4, piece_q, piece_L]
groupPieces2_Board3 = [piece_Z, piece_L4, piece_z]
groupPieces3_Board3 = [piece_L4, piece_q, piece_t]
groupPieces4_Board3 = [piece_l, piece_q, piece_f]
groupPieces5_Board3 = [piece_l, piece_q, piece_f]
groupPieces6_Board3 = [piece_l, piece_q, piece_f]
groupDado_Board3 = [groupPieces1_Board3,groupPieces2_Board3,groupPieces3_Board3,groupPieces4_Board3,groupPieces5_Board3,groupPieces6_Board3]
# ======================================================================= #
img12_1 = [
	[0, 0, -1, -1, -1],
	[0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0]
]

groupPieces1_img12_1 = [piece_cuadrado, piece_l, piece_q, piece_L]
groupPieces2_img12_1 = [piece_f, piece_cunia, piece_L4, piece_t]
groupPieces3_img12_1 = [piece_cunia, piece_q, piece_cuadrado, piece_L4]
groupPieces4_img12_1 = [piece_t, piece_f, piece_z, piece_cuadrado]
groupPieces5_img12_1 = [piece_l, piece_z, piece_L, piece_f]
groupPieces6_img12_1 = [piece_L, piece_cunia, piece_Z, piece_q]
# ======================================================================= #


img12_2 = [
	[-1, -1, 0, 0, 0],
	[-1, -1, 0, 0, 0],
	[-1, -1, 0, 0, 0],
	[-1, -1, 0, 0, 0],
	[0, 0, 0, 0, 0]
]

groupPieces1_img12_2 = [piece_f, piece_l3, piece_cuadrado, piece_L4]
groupPieces2_img12_2 = [piece_L, piece_q, piece_L4, piece_l3]
groupPieces3_img12_2 = [piece_cuadrado, piece_f, piece_l3, piece_q]
groupPieces4_img12_2 = [piece_l, piece_cunia, piece_L4, piece_f]
groupPieces5_img12_2 = [piece_f, piece_q, piece_l2, piece_L4]
groupPieces6_img12_2 = [piece_l3, piece_z, piece_Z, piece_q]
# ======================================================================= #

img12_3=[
	[-1, 0, 0, 0, -1],
	[0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0],
	[0, -1, -1, 0, 0]
]

groupPieces1_img12_3 = [piece_l3, piece_L4, piece_t, piece_z]
groupPieces2_img12_3 = [piece_f, piece_q, piece_l3, piece_cunia]
groupPieces3_img12_3 = [piece_l3, piece_Z, piece_t, piece_L]
groupPieces4_img12_3 = [piece_cuadrado, piece_t, piece_l3, piece_f]
groupPieces5_img12_3 = [piece_L, piece_Z, piece_q, piece_l2]
groupPieces6_img12_3 = [piece_f, piece_q, piece_l2, piece_L]
# ======================================================================= #

board = img12_3
pieces = groupPieces6_img12_3

#-----CARTAS-----#
# img4_4i=[[None,None,None,None,None,None,None,None,None,None],
#         [None,None,None,None,None,None,None,None,None,None],
#         [None,None,None,None,None,None,None,None,None,None],
#         [None,None,None,None,None,0,None,None,None,None],
#         [None,None,None,None,None,0,0,None,None,None],
#         [None,None,None,0,0,0,0,None,None,None],
#         [None,None,None,0,0,0,0,None,None,None],
#         [None,None,None,None,0,0,0,None,None,None],
#         [None,None,None,None,0,0,0,None,None,None],
#         [None,None,None,None,None,None,None,None,None,None],
#         [None,None,None,None,None,None,None,None,None,None],
#         [None,None,None,None,None,None,None,None,None,None]]
# img4_4d=[[None,None,None,None,None,None,None,None,None,None,None],
#         [None,None,None,None,None,None,None,None,None,None,None],
#         [None,None,None,None,None,None,None,None,None,None,None],
#         [None,None,None,None,None,0,0,None,None,None,None],
#         [None,None,None,None,None,0,0,None,None,None,None],
#         [None,None,None,None,None,0,0,0,None,None,None],
#         [None,None,None,0,0,0,0,0,None,None,None],
#         [None,None,None,0,0,0,0,0,None,None,None],
#         [None,None,None,None,None,None,None,None,None,None,None],
#         [None,None,None,None,None,None,None,None,None,None,None],
#         [None,None,None,None,None,None,None,None,None,None,None]]
# img4_4a=[[None,None,None,None,None,None,None,None,None,None,None],
#         [None,None,None,None,None,None,None,None,None,None,None],
#         [None,None,None,None,None,None,None,None,None,None,None],
#         [None,None,None,None,0,0,0,0,None,None,None],
#         [None,None,None,None,0,0,0,0,None,None,None],
#         [None,None,None,0,0,0,0,0,None,None,None],
#         [None,None,None,0,0,None,0,None,None,None,None],
#         [None,None,None,None,None,None,None,None,None,None,None],
#         [None,None,None,None,None,None,None,None,None,None,None],
#         [None,None,None,None,None,None,None,None,None,None,None]]

# img8_3i=[[None,None,None,None,None,None,None,None,None,None,None],
#         [None,None,None,None,None,None,None,None,None,None,None],
#         [None,None,None,None,None,None,None,None,None,None,None],
#         [None,None,None,None,0,0,None,None,None,None,None],
#         [None,None,None,0,0,0,0,None,None,None,None],
#         [None,None,None,None,0,0,0,0,None,None,None],
#         [None,None,None,None,0,0,0,None,None,None,None]]
# img8_3d=[[None,None,None,None,None,None,None,None,None,None],
#         [None,None,None,None,None,None,None,None,None,None],
#         [None,None,None,None,None,None,None,None,None,None],
#         [None,None,None,None,None,0,None,None,None,None],
#         [None,None,None,0,0,0,0,None,None,None],
#         [None,None,None,0,0,0,0,None,None,None],
#         [None,None,None,0,0,0,0,None,None,None],
#         [None,None,None,None,None,None,0,None,None,None],
#         [None,None,None,None,None,None,None,None,None,None],
#         [None,None,None,None,None,None,None,None,None,None],
#         [None,None,None,None,None,None,None,None,None,None]]
# img8_3a=[[None,None,None,None,None,None,None,None,None,None,None],
#         [None,None,None,None,None,None,None,None,None,None,None],
#         [None,None,None,None,None,None,None,None,None,None,None],
#         [None,None,None,None,0,0,None,None,None,None,None],
#         [None,None,None,None,0,0,0,None,None,None,None],
#         [None,None,None,0,0,0,0,0,None,None,None],
#         [None,None,None,None,None,0,0,0,None,None,None],
#         [None,None,None,None,None,None,None,None,None,None,None],
#         [None,None,None,None,None,None,None,None,None,None,None],
#         [None,None,None,None,None,None,None,None,None,None,None]]

# img12_4i=[1,1,0,0,0,
#         1,1,1,1,1,
#         1,1,1,1,1,
#         1,1,1,1,1]
# img12_4d=[0,0,1,1,1,
#         0,0,1,1,1,
#         0,0,1,1,1,
#         0,0,1,1,1,
#         1,1,1,1,1]
# img12_4a=[0,1,1,1,0,
#         1,1,1,1,1,
#         1,1,1,1,1,
#         1,0,0,1,1]

# img16_3i=[1,1,0,0,
#         1,1,1,0,
#         1,1,1,0,
#         1,1,1,1]
# img16_3d=[0,1,1,0,0,
#         1,1,1,0,0,
#         1,1,1,1,0,
#         0,1,1,1,1]
# img16_3a=[1,1,1,1,
#         1,1,1,1,
#         0,0,1,1,
#         0,0,1,0,
#         0,0,1,0]

# img20_4i=[0,0,0,1,0,
#         0,0,0,1,0,
#         0,0,0,1,1,
#         0,1,1,1,1,
#         1,1,1,1,1,
#         1,1,1,1,0]
# img20_4d=[0,1,1,1,
#         1,1,1,1,
#         1,1,1,1,
#         0,1,1,1,
#         0,1,1,0,
#         0,1,1,0]
# img20_4a=[1,1,1,1,1,
#         1,1,1,1,0,
#         1,1,1,1,0,
#         1,1,1,1,0,
#         0,1,0,0,0]

# img24_3i=[0,1,0,0,
#         0,1,1,0,
#         0,1,1,1,
#         1,1,1,1,
#         0,0,0,1]
# img24_3d=[0,1,1,
#         1,1,1,
#         1,1,1,
#         1,0,1,
#         1,0,0]
# img24_3a=[1,1,1,1,
#         1,1,1,0,
#         0,1,1,0,
#         0,1,1,0,
#         0,1,0,0]

#-----PIEZAS-----#
#CARTILLA -- 4
# pieza1 = [
#     [1,1,1],
#     [0,1,0]
# ]
# pieza2 = [
#     [1,1,1],
#     [1,1,0]
# ]
# pieza3 = [
#     [0,1,1],
#     [1,1,0]
# ]
# pieza4 = [
#     [1,1,1],
#     [1,1,0]
# ]
# pieza5 = [
#     [0,1],
#     [1,1]
# ]
# pieza6 = [
#     [1,1,1],
#     [1,1,0]
# ]
# pieza7 = [
#     [1,1,1],
#     [1,1,0]
# ]
# pieza8 = [
#     [1,1]
# ]
# pieza9 = [
#     [1,1,1,1],
#     [0,1,0,0]
# ]
# pieza10 = [
#     [0,1,1],
#     [1,1,0]
# ]
# pieza11 = [
#     [1,1,1],
#     [1,0,0]
# ]
# pieza12 = [
#     [1,1],
#     [1,1]
# ]
# pieza13 = [
#     [1,1]
# ]
# pieza14 = [
#     [1,1,1,1],
#     [0,0,0,1]
# ]
# pieza15 = [
#     [1,1,1],
#     [1,1,0]
# ]
# pieza16 = [
#     [1,1],
#     [1,1]
# ]
# pieza17 = [
#     [1, 1, 1],
#     [1, 1, 0]
# ]
# pieza18 = [
#     [1,1,1]
# ]
# pieza19 = [
#     [1, 1, 1, 1],
#     [0, 1, 0, 0]
# ]
# pieza20 = [
#     [1, 1, 1],
#     [0, 1, 0]
# ]
# pieza21 = [
#     [1, 1]
# ]
# pieza22 = [
#     [1,1,1]
# ]
# pieza23 = [
#     [0, 1, 1],
#     [1, 1, 0]
# ]
# pieza24 = [
#     [1, 1, 1],
#     [1, 0, 0]
# ]


