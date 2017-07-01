# 2017.03.04 02:29:25 IST
#Embedded file name: /home/pranav/Academics/sem4/AI/Ultimate TTT/classExperimentation3.py
import sys
import random
import signal
import time
import traceback
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
        self.timeLimit = datetime.timedelta(seconds=14.5)
        self.begin = 0
        self.index = 0
        self.zobrist = []
        self.transpositionTable = dict()
        self.moveOrder = dict()
        self.initZobrist()

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
        boardCopy.block_status[root[0] / 4][root[1] / 4] = blockVal

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
                            self.zobrist[i][j][k][l].append(random.randint(0, 18446744073709551616L))

    def move(self, board, old_move, flag):
        global boardCopy
        self.marker = flag
        boardCopy = copy.deepcopy(board)
        move = copy.deepcopy(old_move)
        self.moveOrder = dict()
        try:
            answer_index = self.IDS(move)
        except Exception as e:
            print 'Exception occurred ', e
            print 'Traceback printing '
            traceback.print_tb(sys.exc_info()[2])

        del move
        del boardCopy
        return answer_index

    def IDS(self, root):
        firstGuess = 0
        self.begin = datetime.datetime.utcnow()
        for depth in range(1, self.maxSearchDepth):
            self.transpositionTable = dict()
            firstGuess, move = self.MTDF(root, firstGuess, depth)
            if datetime.datetime.utcnow() - self.begin > self.timeLimit:
                break
            finalMove = move
            print depth

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
            self.index = 0
            g, move = self.alphaBeta(root, beta - 1, beta, depth)
            if datetime.datetime.utcnow() - self.begin > self.timeLimit:
                return (g, move)
            if g < beta:
                upperBound = g
            else:
                lowerBound = g

        return (g, move)

    def cantorPairing(self, a, b):
        return (a + b) * (a + b + 1) / 2 + b

    def zobristHash(self, root):
        h = 0
        BS = boardCopy.board_status
        for i in xrange(0, 16):
            for j in xrange(0, 16):
                if BS[i][j] == 'x':
                    h = h ^ self.zobrist[i][j][root[0] + 1][root[1] + 1][0]
                elif BS[i][j] == 'o':
                    h = h ^ self.zobrist[i][j][root[0] + 1][root[1] + 1][1]

        return h

    def alphaBeta(self, root, alpha, beta, depth):
        board_md5 = self.zobristHash(root)
        nLower = self.cantorPairing(board_md5, 1)
        nUpper = self.cantorPairing(board_md5, 2)
        lower = (-2 * self.INFINITY, root)
        upper = (2 * self.INFINITY, root)
        if nLower in self.transpositionTable:
            lower = self.transpositionTable[nLower]
            if lower[0] >= beta:
                return lower
        if nUpper in self.transpositionTable:
            upper = self.transpositionTable[nUpper]
            if upper[0] <= alpha:
                return upper
        status = boardCopy.find_terminal_state()
        if status[1] == 'WON':
            if self.myMove:
                return (self.INFINITY, root)
            else:
                return (-self.INFINITY, root)
        alpha = max(alpha, lower[0])
        beta = min(beta, upper[0])
        moveHash = self.cantorPairing(board_md5, self.index)
        moveInfo = []
        if moveHash in self.moveOrder:
            children = []
            children.extend(self.moveOrder[moveHash])
            nSiblings = len(children)
        else:
            children = self.allChildren(root)
            nSiblings = len(children)
        if depth == 0 or nSiblings == 0:
            answer = root
            g = self.evaluate(root)
        elif self.myMove:
            g = -self.INFINITY
            answer = children[0]
            if datetime.datetime.utcnow() - self.begin > self.timeLimit:
                return (g, answer)
            a = alpha
            i = 0
            while g < beta and i < nSiblings:
                self.myMove = False
                c = children[i]
                blockVal = boardCopy.block_status[c[0] / 4][c[1] / 4]
                boardCopy.update(root, c, self.marker)
                self.index += 1
                val, temp = self.alphaBeta(c, a, beta, depth - 1)
                self.revertBoard(c, blockVal)
                self.index -= 1
                temp = (val, c)
                moveInfo.append(temp)
                if val > g:
                    g = val
                    answer = c
                a = max(a, g)
                i = i + 1

            self.myMove = True
        else:
            g = self.INFINITY
            answer = children[0]
            if datetime.datetime.utcnow() - self.begin > self.timeLimit:
                return (g, answer)
            b = beta
            i = 0
            while g > alpha and i < nSiblings:
                self.myMove = True
                c = children[i]
                blockVal = boardCopy.block_status[c[0] / 4][c[1] / 4]
                boardCopy.update(root, c, self.getMarker(self.marker))
                self.index += 1
                val, temp = self.alphaBeta(c, alpha, b, depth - 1)
                self.revertBoard(c, blockVal)
                self.index -= 1
                temp = (val, c)
                moveInfo.append(temp)
                if val < g:
                    g = val
                    answer = c
                b = min(b, g)
                i = i + 1

            self.myMove = False
        temp = []
        if self.myMove:
            moveInfo = sorted(moveInfo, reverse=True)
        else:
            moveInfo = sorted(moveInfo)
        for i in moveInfo:
            temp.append(i[1])
            children.remove(i[1])

        random.shuffle(children)
        self.moveOrder[moveHash] = []
        self.moveOrder[moveHash].extend(temp)
        self.moveOrder[moveHash].extend(children)
        if len(self.moveOrder[moveHash]) != nSiblings:
            print "I've Given UUUUUUUUUUPPPPPP"
        if g <= alpha:
            self.transpositionTable[nUpper] = (g, answer)
        if g >= beta:
            self.transpositionTable[nLower] = (g, answer)
        return (g, answer)

    def evaluate(self, old_move):
        return self.heuristics(old_move)

    def heuristics(self, last_move):
        openMove = 35
        lastBlockWin = 20
        contBlock = [0,
         0,
         100,
         250,
         0]
        cutBlock = [0,
         0,
         100,
         250,
         0]
        contCell = [0,
         0,
         4,
         10,
         0]
        cutCell = [0,
         0,
         4,
         10,
         0]
        blockWin = 40
        blockWinCent = 10
        blockWinCor = 8
        cCell = 0.25
        cellOfC = 0.5
        ownFlag = self.marker
        oppFlag = self.getMarker(self.marker)
        heurVal = 0
        bs = boardCopy.block_status
        BS = boardCopy.board_status
        blockX = last_move[0] % 4
        blockY = last_move[1] % 4
        if bs[blockX][blockY] != '-':
            if self.myMove:
                heurVal -= openMove
            else:
                heurVal += openMove
        blockX = last_move[0] / 4
        blockY = last_move[1] / 4
        if bs[blockX][blockY] == ownFlag:
            heurVal += lastBlockWin
        elif bs[blockX][blockY] == oppFlag:
            heurVal -= lastBlockWin
        FDdrawCount = 0
        BDdrawCount = 0
        FDcountSelf = 0
        FDcountOther = 0
        FDflagSelf = 0
        FDflagOther = 0
        BDcountSelf = 0
        BDcountOther = 0
        BDflagSelf = 0
        BDflagOther = 0
        for i in range(4):
            if bs[i][i] == ownFlag:
                FDcountSelf += 1
                FDflagSelf = 1
            elif bs[i][i] == oppFlag:
                FDcountOther += 1
                FDflagOther = 1
            elif bs[i][i] == 'd':
                FDdrawCount += 1
            if bs[3 - i][i] == ownFlag:
                BDcountSelf += 1
                BDflagSelf = 1
            elif bs[3 - i][i] == oppFlag:
                BDcountOther += 1
                BDflagOther = 1
            elif bs[3 - i][i] == 'd':
                BDdrawCount += 1
            RWdrawCount = 0
            CLdrawCount = 0
            RWcountSelf = 0
            RWflagSelf = 0
            RWcountOther = 0
            RWflagOther = 0
            CLcountSelf = 0
            CLflagSelf = 0
            CLcountOther = 0
            CLflagOther = 0
            for j in range(4):
                if (i == 1 or i == 2) and (j == 1 or j == 2):
                    if bs[i][j] == ownFlag:
                        heurVal += blockWinCent
                    elif bs[i][j] == oppFlag:
                        heurVal -= blockWinCent
                if (i == 0 or i == 3) and (j == 0 or j == 3):
                    if bs[i][j] == ownFlag:
                        heurVal += blockWinCor
                    elif bs[i][j] == oppFlag:
                        heurVal -= blockWinCor
                if bs[i][j] == ownFlag:
                    heurVal += blockWin
                elif bs[i][j] == oppFlag:
                    heurVal -= blockWin
                if bs[i][j] == ownFlag:
                    RWcountSelf += 1
                    RWflagSelf = 1
                elif bs[i][j] == oppFlag:
                    RWcountOther += 1
                    RWflagOther = 1
                elif bs[i][j] == 'd':
                    RWdrawCount += 1
                if bs[j][i] == ownFlag:
                    CLcountSelf += 1
                    CLflagSelf = 1
                elif bs[j][i] == oppFlag:
                    CLcountOther += 1
                    CLflagOther = 1
                elif bs[j][i] == 'd':
                    CLdrawCount += 1
                CCSFD = 0
                CFSFD = 0
                CCOFD = 0
                CFOFD = 0
                CCSBD = 0
                CFSBD = 0
                CCOBD = 0
                CFOBD = 0
                if bs[i][j] == '-':
                    for k in range(4):
                        if BS[4 * i + k][4 * j + k] == ownFlag:
                            CCSFD += 1
                            CFSFD = 1
                        elif BS[4 * i + k][4 * j + k] == oppFlag:
                            CCOFD += 1
                            CFOFD = 1
                        if BS[4 * i + 3 - k][4 * j + k] == ownFlag:
                            CCSBD += 1
                            CFSBD = 1
                        elif BS[4 * i + 3 - k][4 * j + k] == oppFlag:
                            CCOBD += 1
                            CFOBD = 1
                        CCSRW = 0
                        CCORW = 0
                        CFSRW = 0
                        CFORW = 0
                        CCSCL = 0
                        CCOCL = 0
                        CFSCL = 0
                        CFOCL = 0
                        for l in range(4):
                            if BS[4 * i + k][4 * j + l] == ownFlag:
                                CCSRW += 1
                                CFSRW = 1
                            elif BS[4 * i + k][4 * j + l] == oppFlag:
                                CCORW += 1
                                CFORW = 1
                            if BS[4 * i + l][4 * j + k] == ownFlag:
                                CCSCL += 1
                                CFSCL = 1
                            elif BS[4 * i + l][4 * j + k] == oppFlag:
                                CCOCL += 1
                                CFOCL = 1

                        if CFSRW == 1:
                            if CFORW == 0:
                                heurVal += contCell[CCSRW]
                            else:
                                heurVal -= cutCell[CCSRW]
                        if CFORW == 1:
                            if CFSRW == 0:
                                heurVal -= contCell[CCORW]
                            else:
                                heurVal += cutCell[CCORW]
                        if CFSCL == 1:
                            if CFOCL == 0:
                                heurVal += contCell[CCSCL]
                            else:
                                heurVal -= cutCell[CCSCL]
                        if CFOCL == 1:
                            if CFSCL == 0:
                                heurVal -= contCell[CCOCL]
                            else:
                                heurVal += cutCell[CCOCL]

                    if CFSFD == 1:
                        if CFOFD == 0:
                            heurVal += contCell[CCSFD]
                        else:
                            heurVal -= cutCell[CCSFD]
                    if CFOFD == 1:
                        if CFSFD == 0:
                            heurVal -= contCell[CCOFD]
                        else:
                            heurVal += cutCell[CCOFD]
                    if CFSBD == 1:
                        if CFOBD == 0:
                            heurVal += contCell[CCSBD]
                        else:
                            heurVal -= cutCell[CCSBD]
                    if CFOBD == 1:
                        if CFSBD == 0:
                            heurVal -= contCell[CCOBD]
                        else:
                            heurVal += cutCell[CCOBD]

            if RWflagSelf == 1:
                if RWflagOther == 0:
                    heurVal += contBlock[RWcountSelf]
                elif RWflagOther == 1 or RWdrawCount > 0:
                    heurVal -= cutBlock[RWcountSelf]
            if RWflagOther == 1:
                if RWflagSelf == 0:
                    heurVal -= contBlock[RWcountOther]
                elif RWflagSelf == 1 or RWdrawCount > 0:
                    heurVal += cutBlock[RWcountOther]
            if CLflagSelf == 1:
                if CLflagOther == 0:
                    heurVal += contBlock[CLcountSelf]
                elif CLflagOther == 1 or CLdrawCount > 0:
                    heurVal -= cutBlock[CLcountSelf]
            if CLflagOther == 1:
                if CLflagSelf == 0:
                    heurVal -= contBlock[CLcountOther]
                elif CLflagSelf == 1 or CLdrawCount > 0:
                    heurVal += cutBlock[CLcountOther]

        if FDflagSelf == 1:
            if FDflagOther == 0:
                heurVal += contBlock[FDcountSelf]
            elif FDflagOther == 1 or FDdrawCount > 0:
                heurVal -= cutBlock[FDcountSelf]
        if FDflagOther == 1:
            if FDflagSelf == 0:
                heurVal -= contBlock[FDcountOther]
            elif FDflagSelf == 1 or FDdrawCount > 0:
                heurVal += cutBlock[FDcountOther]
        if BDflagSelf == 1:
            if BDflagOther == 0:
                heurVal += contBlock[BDcountSelf]
            elif BDflagOther == 1 or BDdrawCount > 0:
                heurVal -= cutBlock[BDcountSelf]
        if BDflagOther == 1:
            if BDflagSelf == 0:
                heurVal -= contBlock[BDcountOther]
            elif BDflagSelf == 1 or BDdrawCount > 0:
                heurVal += cutBlock[BDcountOther]
        for k in range(4):
            for l in range(4):
                if bs[k][l] == '-':
                    for i in range(4):
                        for j in range(4):
                            if (i == 1 or i == 2) and (j == 1 or j == 2):
                                if BS[4 * k + i][4 * l + j] == ownFlag:
                                    heurVal += cCell
                                elif BS[4 * k + i][4 * l + j] == oppFlag:
                                    heurVal -= cCell
                            if (i == 0 or i == 3) and (j == 0 or j == 3):
                                if BS[4 * k + i][4 * l + j] == ownFlag:
                                    heurVal += cCell
                                elif BS[4 * k + i][4 * l + j] == oppFlag:
                                    heurVal -= cCell
                            if (k == 1 or k == 2) and (l == 1 or l == 2):
                                if BS[4 * k + i][4 * l + j] == ownFlag:
                                    heurVal += cellOfC
                                elif BS[4 * k + i][4 * l + j] == oppFlag:
                                    heurVal -= cellOfC
                            if (k == 0 or k == 3) and (l == 0 or l == 3):
                                if BS[4 * k + i][4 * l + j] == ownFlag:
                                    heurVal += cellOfC
                                elif BS[4 * k + i][4 * l + j] == oppFlag:
                                    heurVal -= cellOfC

        return heurVal
+++ okay decompyling classExperimentation3.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.03.04 02:29:26 IST
