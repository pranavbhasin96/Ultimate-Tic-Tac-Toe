#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import random
import signal
import time
from math import exp
import datetime
import copy
import hashlib
import json

class New_Heuristics:
	def __init__(self):
		self.INFINITY = 100000
		self.maxSearchDepth = 257
		self.marker = 'x'
		self.myMove = False
		self.timeLimit = datetime.timedelta(seconds = 14.5)
		self.begin = 0
		self.count = 0
		self.zobrist = []
		self.transpositionTable = dict()
		self.initZobrist()
		return

	def getMarker(self, flag):
		if flag == 'x':
			return 'o'
		else:
			return 'x'

	def allChildren(self, blockIdentifier):
		cells = boardCopy.find_valid_move_cells(blockIdentifier)
		return cells

	def revertBoard(self, root, blockVal):
		boardCopy.board_status[root[0]][root[1]] = '-'
		boardCopy.block_status[root[0]/4][root[1]/4] = blockVal

	def initZobrist(self):
		self.zobrist = []
		for i in xrange(0, 16):
			self.zobrist.append([])
			for j in xrange(0, 16):
				self.zobrist[i].append([])
				for k in xrange(0, 17):
					self.zobrist[i][j].append([])
					for l in xrange(0, 17):
						self.zobrist[i][j][k].append([])
						for m in xrange(0, 2):
							self.zobrist[i][j][k][l].append(random.randint(0, 2**64))

	def move(self, board, old_move, flag):
		self.marker = flag
		# Make a copy of board and old_move for future use
		global boardCopy
		boardCopy = copy.deepcopy(board)
		move = copy.deepcopy(old_move)
		try:
			answer_index = self.IDS(move)
		except Exception as e:
			print 'Exception occurred ', e
			print 'Traceback printing ', sys.exc_info()[2].format_exc()
		del move
		del boardCopy
		return answer_index

	def IDS(self, root):
		firstGuess = 0
		# Initialize beginning time
		self.begin = datetime.datetime.utcnow()
		# Search for best possible move for as long as time permits
		for depth in range(1, self.maxSearchDepth):
			self.transpositionTable = dict()
			firstGuess, move = self.MTDF(root, firstGuess, depth)
			if datetime.datetime.utcnow() - self.begin > self.timeLimit:
				break
			finalMove = move
		print depth - 1
		return finalMove

	def MTDF(self, root, firstGuess, depth):
		g = firstGuess

		upperBound = self.INFINITY
		lowerBound = -self.INFINITY

		while lowerBound < upperBound:
			if g == lowerBound:
				beta = g + 1
			else:
				beta = g

			self.myMove = True
			g, move = self.alphaBeta(root, beta-1, beta, depth)

			# Return value if time up
			if datetime.datetime.utcnow() - self.begin > self.timeLimit:
				return g, move

			if g < beta:
				upperBound = g
			else:
				lowerBound = g

		return g, move

	def cantorPairing(self, a, b):
		return (a + b)*(a + b + 1)/2 + b

	def zobristHash(self, root):
		h = 0
		BS = boardCopy.board_status
		for i in xrange(0, 16):
			for j in xrange(0, 16):
				if BS[i][j] == 'x':
					h = h^self.zobrist[i][j][root[0]+1][root[1]+1][0]
				elif BS[i][j] == 'o':
					h = h^self.zobrist[i][j][root[0]+1][root[1]+1][1]
		return h

	def alphaBeta(self, root, alpha, beta, depth):

		# Get hash of current board state for Transposition lookup
		# board_md5 = hashlib.sha1(json.dumps(boardCopy.board_status)).hexdigest()
		# board_md5 += hashlib.sha1(json.dumps(root)).hexdigest()

		board_md5 = self.zobristHash(root)
		nLower = self.cantorPairing(board_md5, 1)
		nUpper = self.cantorPairing(board_md5, 2)

		lower = -2*self.INFINITY, root
		upper = 2*self.INFINITY, root

		# Transposition table lookup
		if (nLower in self.transpositionTable):
			lower = self.transpositionTable[nLower]
			if (lower[0] >= beta):
				return lower

		if (nUpper in self.transpositionTable):
			upper = self.transpositionTable[nUpper]
			if (upper[0] <= alpha):
				return upper

		status = boardCopy.find_terminal_state()
		if status[1] == "WON":
			if self.myMove:
				return self.INFINITY, root
			else:
				return -self.INFINITY, root

		# Update values of alpha and beta based on values in Transposition Table
		alpha = max(alpha, lower[0])
		beta = min(beta, upper[0])

		# # Reorder moves
		# if (board_md5 + str(depth) not in self.moveOrder) and (depth != 0):
		# 	moveInfo = []
		# 	children = self.allChildren(root)
		# 	nSiblings = len(children)
		# 	for i in xrange(0, nSiblings):
		# 		blockVal = boardCopy.block_status[children[i][0]/4][children[i][1]/4]
		# 		boardCopy.update(root, children[i], self.marker)
		# 		temp = self.evaluate(children[i]), children[i]
		# 		moveInfo.append(temp)
		# 		self.revertBoard(children[i], blockVal)
		# 	if self.myMove:
		# 		moveInfo = sorted(moveInfo, reverse = True)
		# 	else:
		# 		moveInfo = sorted(moveInfo)
		#
		# 	children = []
		# 	for i in moveInfo:
		# 		children.append(i[1])
		#
		# 	self.moveOrder[board_md5 + str(depth)] = children
		#
		# # Reordered moves already present!
		# elif (board_md5 + str(depth) in self.moveOrder) and (depth != 0):
		# 	children = self.moveOrder[board_md5 + str(depth)]
		# 	nSiblings = len(children)

		children = self.allChildren(root)
		random.shuffle(children)
		nSiblings = len(children)

		if depth == 0 or nSiblings == 0:
			answer = root
			g = self.evaluate(root)

		# Node is a max node
		elif self.myMove:
			g = -self.INFINITY
			answer = children[0]
			# Return value if time up
			if datetime.datetime.utcnow() - self.begin > self.timeLimit:
					return g, answer

			# Save original alpha value
			a = alpha
			i = 0
			while ((g < beta) and (i < nSiblings)):
				self.myMove = False
				c = children[i]
				blockVal = boardCopy.block_status[c[0]/4][c[1]/4]
				# Mark current node as taken by us for future reference
				boardCopy.update(root, c, self.marker)
				val, temp = self.alphaBeta(c, a, beta, depth-1)
				self.revertBoard(c, blockVal)
				if val > g:
					g = val
					answer = c
				a = max(a, g)
				i = i + 1

		# Node is a min node
		else:
			g = self.INFINITY
			answer = children[0]
			# Return value if time up
			if datetime.datetime.utcnow() - self.begin > self.timeLimit:
					return g, answer

			# Save original beta value
			b = beta
			i = 0
			while ((g > alpha) and (i < nSiblings)):
				self.myMove = True
				c = children[i]
				blockVal = boardCopy.block_status[c[0]/4][c[1]/4]
				# Mark current node as taken by us for future reference
				boardCopy.update(root, c, self.getMarker(self.marker))
				val, temp = self.alphaBeta(c, alpha, b, depth-1)
				self.revertBoard(c, blockVal)
				if val < g:
					g = val
					answer = c
				b = min(b, g)
				i = i + 1

		# Traditional transposition table storing of bounds
		# ----------------------------------------------------#
		# Fail low result implies an upper bound
		if g <= alpha:
			self.transpositionTable[nUpper] = g, answer

		# Fail high result implies a lower bound
		if g >= beta:
			self.transpositionTable[nLower] = g, answer

		return g, answer

	def evaluate(self, old_move):
		return self.heuristics(old_move)

	def heuristics(self, last_move):

		openMove = 30
		lastBlockWin=30
		contBlock2=60
		contBlock3=150
		cutBlock2=60
		cutBlock3=150
		contCell2=4
		contCell3=10
		cutCell2=4
		cutCell3=10
		blockWin=20
		blockWinCor=10
		blockWinCent=10
		CCell=0.2
		cellOfC=0.1

		ownFlag = self.marker
		oppFlag = self.getMarker(ownFlag)

		heurVal = 0

		bs = boardCopy.block_status
		BS = boardCopy.board_status

		##############################################################
		# checking if this move helped us win block
		##############################################################
		blockX = last_move[0]/4
		blockY = last_move[1]/4
		if bs[blockX][blockY] == ownFlag:
			heurVal+=lastBlockWin
		elif bs[blockX][blockY] == oppFlag:
			heurVal-=lastBlockWin
		##############################################################
		#checking for continuous blocks or cutting other blocks
		##############################################################

		#checking rows
		for i in range(4):
			fl = 0
			countSelf  = 0
			countOther = 0
			for j in range(4):
				if bs[i][j] == oppFlag:
					fl = 1
					countOther+=1
				if bs[i][j] == ownFlag:
					countSelf+=1
			if(fl == 0 and countSelf>0):
				if countSelf == 2:
					heurVal += contBlock2
				elif countSelf == 3:
					heurVal += contBlock3
			if(fl == 1 and countOther>0 and countSelf>0):
				if countOther == 2:
					heurVal += cutBlock2
				elif countOther == 3:
					heurVal += cutBlock3

		#checking columns
		for j in range(4):
			fl = 0
			countSelf = 0
			countOther = 0
			for i in range(4):
				if bs[i][j] == oppFlag:
					fl = 1
					countOther+=1
				if bs[i][j] == ownFlag:
					countSelf +=1
			if(fl == 0 and countSelf>0):
				if countSelf == 2:
					heurVal += contBlock2
				elif countSelf == 3:
					heurVal += contBlock3
			if(fl == 1 and countOther>0 and countSelf>0):
				if countOther == 2:
					heurVal += cutBlock2
				elif countOther == 3:
					heurVal += cutBlock3

		#checking forward diagonal
 		fl = 0
		countSelf = 0
		countOther = 0
		for i in range(4):
			if bs[i][i] == oppFlag:
				fl = 1
				countOther+=1
			if bs[i][i] == ownFlag:
				countSelf+=1
		if(fl == 0 and countSelf>0):
			if countSelf == 2:
				heurVal += contBlock2
			elif countSelf == 3:
				heurVal += contBlock3
		if(fl == 1 and countOther>0 and countSelf>0):
			if countOther == 2:
				heurVal += cutBlock2
			elif countOther == 3:
				heurVal += cutBlock3

		#checking back diagonal
		fl = 0
		countSelf = 0
		countOther = 0
		for i in range(4):
			if bs[3-i][i] == oppFlag:
				fl = 1
				countOther+=1
			if bs[3-i][i] == ownFlag:
				countSelf+=1
		if(fl == 0 and countSelf>0):
			if countSelf == 2:
				heurVal += contBlock2
			elif countSelf == 3:
				heurVal += contBlock3
		if(fl == 1 and countOther>0 and countSelf > 0):
			if countOther == 2:
				heurVal += cutBlock2
			elif countOther == 3:
				heurVal += cutBlock3

		#############################################################
		#checking for continuous cells in each block or cutting
		##############################################################

		for k in range(4):
			for l in range(4):
				if bs[k][l]=='-':
					#checking rows
					for i in range(4):
						fl = 0
						countSelf = 0
						countOther = 0
						for j in range(4):
							if BS[4*k + i][4*l + j] == oppFlag:
								fl = 1
								countOther+=1
							if BS[4*k + i][4*l + j] == ownFlag:
								countSelf+=1
						if(fl == 0 and countSelf>0):
							if countSelf == 2:
								heurVal += contCell2
							elif countSelf == 3:
								heurVal += contCell3
						if(fl == 1 and countOther>0 and countSelf>0):
							if countOther == 2:
								heurVal += cutCell2
							elif countOther == 3:
								heurVal += cutCell3

					#checking columns
					for j in range(4):
						fl = 0
						countSelf = 0
						countOther = 0
						for i in range(4):
							if BS[4*k + i][4*l + j] == oppFlag:
								fl = 1
								countOther+=1
							if BS[4*k + i][4*l + j] == ownFlag:
								countSelf+=1
						if(fl == 0 and countSelf>0):
							if countSelf == 2:
								heurVal += contCell2
							elif countSelf == 3:
								heurVal += contCell3
						if(fl == 1 and countOther>0 and countSelf>0):
							if countOther == 2:
								heurVal += cutCell2
							elif countOther == 3:
								heurVal += cutCell3

					#checking forward diagonal
			 		fl = 0
					countSelf = 0
					countOther =0
					for i in range(4):
						if BS[4*k+i][4*l+i] == oppFlag:
							fl = 1
							countOther+=1
						if BS[4*k + i][4*l + i] == ownFlag:
							countSelf+=1
					if(fl == 0 and countSelf>0):
						if countSelf == 2:
							heurVal += contCell2
						elif countSelf == 3:
							heurVal += contCell3
					if(fl == 1 and countOther>0 and countSelf>0):
						if countOther == 2:
							heurVal += cutCell2
						elif countOther == 3:
							heurVal += cutCell3

					#checking back diagonal
					fl = 0
					countSelf=0
					for i in range(4):
						if BS[4*k+3-i][4*l+i] == oppFlag:
							fl = 1
							countOther+=1
						if BS[4*k+3-i][4*l+i] == ownFlag:
							countSelf+=1
					if(fl == 0 and countSelf>0):
						if countSelf == 2:
							heurVal += contCell2
						elif countSelf == 3:
							heurVal += contCell3
					if(fl == 1 and countOther>0 and countSelf>0):
						if countOther == 2:
							heurVal += cutCell2
						elif countOther == 3:
							heurVal += cutCell3

		##############################################################
		#checking for others continuous blocks or cutting other blocks
		##############################################################

		#checking rows
		for i in range(4):
			fl = 0
			countSelf = 0
			countOther = 0
			for j in range(4):
				if bs[i][j] == ownFlag:
					countSelf+=1
					fl = 1
				if bs[i][j] == oppFlag:
					countOther+=1
			if(fl == 0 and countOther>0):
				if countOther == 2:
					heurVal -= contBlock2
				elif countOther == 3:
					heurVal -= contBlock3
			if(fl == 1 and countSelf>0 and countOther>0):
				if countSelf == 2:
					heurVal -= cutBlock2
				elif countSelf == 3:
					heurVal -= cutBlock3

		#checking columns
		for j in range(4):
			fl = 0
			countSelf = 0
			countOther = 0
			for i in range(4):
				if bs[i][j] == ownFlag:
					countSelf+=1
					fl = 1
				if bs[i][j] == oppFlag:
					countOther+=1
			if(fl == 0 and countOther>0):
				if countOther == 2:
					heurVal -= contBlock2
				elif countOther == 3:
					heurVal -= contBlock3
			if(fl == 1 and countSelf>0 and countOther>0):
				if countSelf == 2:
					heurVal -= cutBlock2
				elif countSelf == 3:
					heurVal -= cutBlock3

		#checking forward diagonal
 		fl = 0
		countSelf = 0
		countOther = 0
		for i in range(4):
			if bs[i][i] == ownFlag:
				countSelf +=1
				fl = 1
			if bs[i][i] == oppFlag:
				countOther+=1
		if(fl == 0 and countOther>0):
			if countOther == 2:
				heurVal -= contBlock2
			elif countOther == 3:
				heurVal -= contBlock3
		if(fl == 1 and countSelf>0 and countOther>0):
			if countSelf == 2:
				heurVal -= cutBlock2
			elif countSelf == 3:
				heurVal -= cutBlock3

		#checking back diagonal
		fl = 0
		countSelf = 0
		countOther = 0
		for i in range(4):
			if bs[3-i][i] == ownFlag:
				fl = 1
				countSelf+=1
			if bs[3-i][i] == oppFlag:
				countOther+=1
		if(fl == 0 and countOther>0):
			if countOther == 2:
				heurVal -= contBlock2
			elif countOther == 3:
				heurVal -= contBlock3
		if(fl == 1 and countSelf>0 and countOther>0):
			if countSelf == 2:
				heurVal -= cutBlock2
			elif countSelf == 3:
				heurVal -= cutBlock3


		#############################################################
		#checking for other continuous cells in each block or cutting
		##############################################################
		BS = boardCopy.board_status
		for k in range(4):
			for l in range(4):
				if bs[k][l]=='-':
				#checking rows
					for i in range(4):
						fl = 0
						countSelf = 0
						countOther = 0
						for j in range(4):
							if BS[4*k + i][4*l + j] == ownFlag:
								fl = 1
								countSelf+=1
							if BS[4*k + i][4*l + j] == oppFlag:
								countOther+=1
						if(fl == 0 and countOther>0):
							if countOther == 2:
								heurVal -= contCell2
							elif countOther == 3:
								heurVal -= contCell3
						if(fl == 1 and countSelf>0 and countOther>0):
							if countSelf == 2:
								heurVal -= cutCell2
							elif countSelf == 3:
								heurVal -=cutCell3

					#checking columns
					for j in range(4):
						fl = 0
						countSelf = 0
						countOther = 0
						for i in range(4):
							if BS[4*k + i][4*l + j] == ownFlag:
								fl = 1
								countSelf+=1
							if BS[4*k + i][4*l + j] == oppFlag:
								countOther+=1
						if(fl == 0 and countOther>0):
							if countOther == 2:
								heurVal -= contCell2
							elif countOther == 3:
								heurVal -= contCell3
						if(fl == 1 and countSelf>0 and countOther>0):
							if countSelf == 2:
								heurVal -= cutCell2
							elif countSelf == 3:
								heurVal -= cutCell3

					#checking forward diagonal
			 		fl = 0
					countSelf = 0
					countOther = 0
					for i in range(4):
						if BS[4*k + i][4*l + i] == ownFlag:
							fl = 1
							countSelf+=1
						if BS[4*k+i][4*l+i] == oppFlag:
							countOther+=1
					if(fl == 0 and countOther>0):
						if countOther == 2:
							heurVal -= contCell2
						elif countOther == 3:
							heurVal -= contCell3
					if(fl == 1 and countSelf>0 and countOther>0):
						if countSelf == 2:
							heurVal -= cutCell2
						elif countSelf == 3:
							heurVal -= cutCell3

					#checking back diagonal
					fl = 0
					countSelf=0
					countOther=0
					for i in range(4):
						if BS[4*k+3-i][4*l+i] == ownFlag:
							fl = 1
							countSelf+=1
						if BS[4*k+3-i][4*l+i] == oppFlag:
							countOther+=1
					if(fl == 0 and countOther>0):
						if countOther == 2:
							heurVal -= contCell2
						elif countOther == 3:
							heurVal -= contCell3
					if(fl == 1 and countSelf>0 and countOther>0):
						if countSelf == 2:
							heurVal -= cutCell2
						elif countSelf == 3:
							heurVal -= cutCell3


		####################################################################################
		#getting centre/corner squares in blocks AND getting squares in centre/corner blocks
		####################################################################################
		for k in range(4):
			for l in range(4):

				#winning/losing centre block
				if( (k==1 or k==2) and (l==1 or l==2)):
					if(bs[k][l] == ownFlag):
						heurVal += blockWinCent
					elif(bs[k][l] == oppFlag):
						heurVal -= blockWinCent

				#winning/losing corner blocks
				if((k==0 or k==3) and (l==0 or l==3)):
					if(bs[k][l] == ownFlag):
						heurVal += blockWinCor #3
					elif(bs[k][l] ==oppFlag):
						heurVal -= blockWinCor #3

				#winning/losing blocks
				if bs[k][l] == ownFlag:
					heurVal += blockWin
				elif bs[k][l] == oppFlag:
					heurVal -= blockWin

				if bs[k][l]=='-':
					for i in range(4):
						for j in range(4):

							#getting centre squares in blocks
							if ((i==1 or i==2) and (j==1 or j==2)):
								if BS[4*k+i][4*l+j] == ownFlag:
									# print "centre square mila"
									heurVal += CCell
								elif BS[4*k+i][4*l+j] == oppFlag:
									# print "centre square kata"
									heurVal -= CCell

							#getting corner squares in blocks
							if ((i==0 or i==3) and (j==0 or j==3)):
								if BS[4*k+i][4*l+j] == ownFlag:
									# print "corner square mila"
									heurVal += CCell
								elif BS[4*k+i][4*l+j] == oppFlag:
									# print "corner square kata"
									heurVal -= CCell

							#getting square in centre block
							if ((k==1 or k==2) and (l==1 or l==2)):
								if BS[4*k+i][4*l+j] == ownFlag:
									# print "centre block me mila"
									heurVal += cellOfC
								elif BS[4*k+i][4*l+j] == oppFlag:
									# print "centre block me kata"
									heurVal -= cellOfC

							#getting square in corner block
							if ((k==0 or k==3) and (l==0 or l==3)):
								if BS[4*k+i][4*l+j] == ownFlag:
									# print "corner block me mila"
									heurVal += cellOfC
								elif BS[4*k+i][4*l+j] == oppFlag:
									# print "corner block me kata"
									heurVal -= cellOfC

		boardX = last_move[0]%4
		boardY = last_move[1]%4
		if bs[boardX][boardY]!='-':
			if self.myMove:
				heurVal -= openMove
			else:
				heurVal += openMove
		return heurVal
