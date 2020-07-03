from Piece import board
from Piece import pieces

def rotate(piece):
	piece_rotate = []
	for j in range(len(piece[0])):
		piece_rotate.append([])
	for j in range(len(piece[0])):
		for i in range(len(piece)):
			piece_rotate[j].append(None)
			
	for i in range(len(piece)):
		for j in range(len(piece[i])):
			piece_rotate[j][len(piece)-1-i] = piece[i][j]
	return piece_rotate

def turn(piece):
	piece_turn = []
	for i in range(len(piece)):
		piece_turn.append([])
		for j in range(len(piece[0])):
			piece_turn[i].append(None)

	for i in range(len(piece)):
		for j in range(len(piece[i])):
			piece_turn[i][len(piece[0])-1-j] = piece[i][j]
	return piece_turn

def pieceInBoard_position(board, piece, index, up, left):
	for i in range(len(piece)):
		for j in range(len(piece[i])):
			x = up + i
			y = left + j
			if (x >= len(board) or y >= len(board[0])) or ((board[x][y] != 0) and (piece[i][j] == 1)):
				return False
	for i in range(len(piece)):
		for j in range(len(piece[i])):
			x = up + i
			y = left + j
			board[x][y] = (index + 1) if piece[i][j] != 0 else board[x][y]
	return True

def pieceInBoard(board, piece, index):
	for left in range(len(board[0])):
		for up in range(len(board)):
			if pieceInBoard_position(board, piece, index, up, left):
				return True
	return False

def eraseSolution(board, piece, index):
	for i in range(len(board)):
		for j in range(len(board[i])):
			if board[i][j] == index + 1:
				board[i][j] = 0

def solution(board, pieces, index):
	if (index == len(pieces)):
		return True
	for attemp in range(len(pieces) - index):
		for i in range(4):
			pieces[index] = rotate(pieces[index])
			for j in range(2):
				pieces[index] = turn(pieces[index])
				if pieceInBoard(board, pieces[index], index):
					if solution(board, pieces, index + 1):
						return True
					eraseSolution(board, pieces[index], index)
		piece = pieces.pop(index)
		pieces.append(piece)
	return False