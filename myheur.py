def heuristics2(last_move,bs,BS):

    lastBlockWin=50
    contBlock2=10
    contBlock3=25
    cutBlock2=10
    cutBlock3=25
    contCell2=3
    contCell3=8
    cutCell2=3
    cutCell3=8
    blockWin=20
    blockWinCor=8
    blockWinCent=10
    CCell=5
    cellOfC=3

    ownFlag = 'x'
    oppFlag = 'o'

    heurVal = 0

    # bs = boardCopy.block_status
    # BS = boardCopy.board_status

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
    # BS = boardCopy.board_status
    for k in range(4):
        for l in range(4):

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

    # boardX = last_move[0]%4
    # boardY = last_move[1]%4
    # if bs[boardX][boardY]!='-':
    #     if self.myMove:
    #         heurVal -= exp(-heurVal)
    #     else:
    #         heurVal += exp(heurVal)
    return heurVal
