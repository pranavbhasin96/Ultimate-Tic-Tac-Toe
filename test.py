def heuristics5(last_move,bs,BS):
	ownFlag = 'o'
	oppFlag = 'x'

	heurVal = 0

	# bs = boardCopy.block_status
	# BS = boardCopy.board_status

	##############################################################
	# checking if this move helped us win block
	##############################################################
	blockX = last_move[0]/4
	blockY = last_move[1]/4
	if bs[blockX][blockY] == ownFlag:
		heurVal+=50
	elif bs[blockX][blockY] == oppFlag:
		heurVal-=50

	##############################################################
	#checking for others continuous blocks or cutting other blocks
	##############################################################

	countSelfFDiagonal = 0
	countOtherFDiagonal = 0
	countSelfBDiagonal = 0
	countOtherBDiagonal = 0

	for i in range(4):
		countSelfRow = 0
		countOtherRow = 0
		countSelfColumn = 0
		countOtherColumn = 0
		for j in range(4):
			# Checking Rows
			if bs[i][j] == ownFlag:
				countSelfRow += 1
			if bs[i][j] == oppFlag:
				countOtherRow += 1

			# Checking Columns
			if bs[j][i] == ownFlag:
				countSelfColumn += 1
			if bs[j][i] == oppFlag:
				countOtherColumn += 1

		# Evaluating Rows
		if countSelfRow > 0 and countOtherRow > 0:
			if countSelfRow == 2:
				heurVal -= 10
			elif countSelfRow == 3:
				heurVal -= 25

		elif countOtherRow > 0:
			if countOtherRow == 2:
				heurVal -= 10
			elif countOtherRow == 3:
				heurVal -= 25

		# Evaluating Columns
		if countSelfColumn > 0 and countOtherColumn > 0:
			if countSelfColumn == 2:
				heurVal -= 10
			elif countSelfColumn == 3:
				heurVal -= 25

		elif countOtherColumn > 0:
			if countOtherColumn == 2:
				heurVal -= 10
			elif countOtherColumn == 3:
				heurVal -= 25

		# Checking Forward Diagonal
		if bs[i][i] == ownFlag:
			countSelfFDiagonal += 1
		if bs[i][i] == oppFlag:
			countOtherFDiagonal += 1

		# Checking Backward Diagonal
		if bs[3-i][i] == ownFlag:
			countSelfBDiagonal += 1
		if bs[3-i][i] == oppFlag:
			countOtherBDiagonal += 1

	# Evaluating Forward Diagonal
	if countSelfFDiagonal > 0 and countOtherFDiagonal > 0:
		if countSelfFDiagonal == 2:
			heurVal -= 10
		elif countSelfFDiagonal == 3:
			heurVal -= 25

	elif countOtherFDiagonal > 0:
		if countOtherFDiagonal == 2:
			heurVal -= 10
		elif countOtherFDiagonal == 3:
			heurVal -= 25

	# Evaluating Back Diagonal
	if countSelfBDiagonal > 0 and countOtherBDiagonal > 0:
		if countSelfBDiagonal == 2:
			heurVal -= 10
		elif countSelfBDiagonal == 3:
			heurVal -= 25

	elif countOtherBDiagonal > 0:
		if countOtherBDiagonal == 2:
			heurVal -= 10
		elif countOtherBDiagonal == 3:
			heurVal -= 25

	#############################################################
	#checking for other continuous cells in each block or cutting
	##############################################################
	for k in range(4):
		for l in range(4):
			countSelfFDiagonal = 0
			countOtherFDiagonal = 0
			countSelfBDiagonal = 0
			countOtherBDiagonal = 0
			for i in range(4):
				countSelfRow = 0
				countOtherRow = 0
				countSelfColumn = 0
				countOtherColumn = 0
				for j in range(4):
					# Checking Rows
					if BS[4*k + i][4*l + j] == ownFlag:
						countSelfRow += 1
					if BS[4*k + i][4*l + j] == oppFlag:
						countOtherRow += 1

					# Checking Columns
					if BS[4*k + j][4*l + i] == ownFlag:
						countSelfColumn += 1
					if BS[4*k + j][4*l + i] == oppFlag:
						countOtherColumn += 1

				# Evaluating Rows
				if countSelfRow > 0 and countOtherRow > 0:
					if countSelfRow == 2:
						heurVal -= 3
					elif countSelfRow == 3:
						heurVal -= 8

				elif countOtherRow > 0:
					if countOtherRow == 2:
						heurVal -= 3
					elif countOtherRow == 3:
						heurVal -= 8

				# Evaluating Columns
				if countSelfColumn > 0 and countOtherColumn > 0:
					if countSelfColumn == 2:
						heurVal -= 3
					elif countSelfColumn == 3:
						heurVal -= 8

				if countOtherColumn > 0:
					if countOtherColumn == 2:
						heurVal -= 3
					elif countOtherColumn == 3:
						heurVal -= 8

				# Checking Forward Diagonal
				if BS[4*k + i][4*l + i] == ownFlag:
					countSelfFDiagonal += 1
				if BS[4*k + i][4*l + i] == oppFlag:
					countOtherFDiagonal += 1

				# Checking Back Diagonal
				if BS[4*k + 3-i][4*l + i] == ownFlag:
					countSelfBDiagonal += 1
				if BS[4*k + 3-i][4*l + i] == oppFlag:
					countOtherBDiagonal += 1

			# Evaluating Forward Diagonal
			if countSelfFDiagonal > 0 and countOtherFDiagonal > 0:
				if countSelfFDiagonal == 2:
					heurVal -= 3
				elif countSelfFDiagonal == 3:
					heurVal -= 8

			elif countOtherFDiagonal > 0:
				if countOtherFDiagonal == 2:
					heurVal -= 3
				elif countOtherFDiagonal == 3:
					heurVal -= 8

			# Evaluating Back Diagonal
			if countSelfBDiagonal > 0 and countOtherBDiagonal > 0:
				if countSelfBDiagonal == 2:
					heurVal -= 3
				elif countSelfBDiagonal == 3:
					heurVal -= 8

			elif countOtherBDiagonal > 0:
				if countOtherBDiagonal == 2:
					heurVal -= 3
				elif countOtherBDiagonal == 3:
					heurVal -= 8

	##############################################################
	#checking for continuous blocks or cutting other blocks
	##############################################################

	countSelfFDiagonal = 0
	countOtherFDiagonal = 0
	countSelfBDiagonal = 0
	countOtherBDiagonal = 0

	for i in range(4):
		countSelfRow  = 0
		countOtherRow = 0
		countSelfColumn = 0
		countOtherColumn = 0

		for j in range(4):
			# Checking Rows
			if bs[i][j] == oppFlag:
				countOtherRow += 1
			if bs[i][j] == ownFlag:
				countSelfRow += 1

			# Checking Columns
			if bs[j][i] == oppFlag:
				countOtherColumn += 1
			if bs[j][i] == ownFlag:
				countSelfColumn += 1

		# Evaluating Rows
		if countOtherRow > 0 and countSelfRow > 0:
			if countOtherRow == 2:
				heurVal += 10
			elif countOtherRow == 3:
				heurVal += 25

		elif countSelfRow > 0:
			if countSelfRow == 2:
				heurVal += 10
			elif countSelfRow == 3:
				heurVal += 25

		# Evaluating Columns
		if countOtherColumn > 0 and countSelfColumn > 0:
			if countOtherColumn == 2:
				heurVal += 10
			elif countOtherColumn == 3:
				heurVal += 25

		elif countSelfColumn > 0:
			if countSelfColumn == 2:
				heurVal += 10
			elif countSelfColumn == 3:
				heurVal += 25

	# Checking Forward Diagonal
		if bs[i][i] == oppFlag:
			countOtherFDiagonal += 1
		if bs[i][i] == ownFlag:
			countSelfFDiagonal += 1

	# Checking Backward Diagonal
		if bs[3-i][i] == oppFlag:
			countOtherBDiagonal += 1
		if bs[3-i][i] == ownFlag:
			countSelfBDiagonal += 1

	# Evaluating Forward Diagonal
	if countOtherFDiagonal > 0 and countSelfFDiagonal > 0:
		if countOtherFDiagonal == 2:
			heurVal += 10
		elif countOtherFDiagonal == 3:
			heurVal += 25

	elif countSelfFDiagonal > 0:
		if countSelfFDiagonal == 2:
			heurVal += 10
		elif countSelfFDiagonal == 3:
			heurVal += 25

	# Evaluating Backward Diagonal
	if countOtherBDiagonal > 0 and countSelfBDiagonal > 0:
		if countOtherBDiagonal == 2:
			heurVal += 10
		elif countOtherBDiagonal == 3:
			heurVal += 25

	elif countSelfBDiagonal > 0:
		if countSelfBDiagonal == 2:
			heurVal += 10
		elif countSelfBDiagonal == 3:
			heurVal += 25

	#############################################################
	#checking for continuous cells in each block or cutting
	##############################################################

	for k in range(4):
		for l in range(4):
			countSelfFDiagonal = 0
			countOtherFDiagonal = 0
			countSelfBDiagonal = 0
			countOtherBDiagonal = 0

			for i in range(4):
				countSelfRow  = 0
				countOtherRow = 0
				countSelfColumn = 0
				countOtherColumn = 0

				for j in range(4):

					# Checking Rows
					if BS[4*k + i][4*l + j] == oppFlag:
						countOtherRow += 1
					if BS[4*k + i][4*l + j] == ownFlag:
						countSelfRow += 1

					# Checking Columns
					if BS[4*k + j][4*l + i] == oppFlag:
						countOtherColumn += 1
					if BS[4*k + j][4*l + i] == ownFlag:
						countSelfColumn += 1

					# Getting Center Squares in Blocks
					if ((i==1 or i==2) and (j==1 or j==2)):
						if BS[4*k + i][4*l + j] == ownFlag:
							# print "centre square mila"
							heurVal += 5
						elif BS[4*k + i][4*l + j] == oppFlag:
							# print "centre square kata"
							heurVal -= 5

					# Getting Corner Squares in Blocks
					if ((i==0 or i==3) and (j==0 or j==3)):
						if BS[4*k + i][4*l + j] == ownFlag:
							# print "corner square mila"
							heurVal += 5
						elif BS[4*k + i][4*l + j] == oppFlag:
							# print "corner square kata"
							heurVal -= 5

					# Getting Square in Centre Blocks
					if ((k==1 or k==2) and (l==1 or l==2)):
						if BS[4*k + i][4*l + j] == ownFlag:
							# print "centre block me mila"
							heurVal += 3
						elif BS[4*k + i][4*l + j] == oppFlag:
							# print "centre block me kata"
							heurVal -= 3

					# Getting Square in Corner Blocks
					if ((k==0 or k==3) and (l==0 or l==3)):
						if BS[4*k + i][4*l + j] == ownFlag:
							# print "corner block me mila"
							heurVal += 3
						elif BS[4*k + i][4*l + j] == oppFlag:
							# print "corner block me kata"
							heurVal -= 3

				if countOtherRow > 0 and countSelfRow > 0:
					if countOtherRow == 2:
						heurVal += 3
					elif countOtherRow == 3:
						heurVal += 8

				elif countSelfRow > 0:
					if countSelfRow == 2:
						heurVal += 3
					elif countSelfRow == 3:
						heurVal += 8

				if countOtherColumn > 0 and countSelfColumn > 0:
					if countOtherColumn == 2:
						heurVal += 3
					elif countOtherColumn == 3:
						heurVal += 8

				elif countSelfColumn > 0:
					if countSelfColumn == 2:
						heurVal += 3
					elif countSelfColumn == 3:
						heurVal += 8

				# Checking Forward Diagonal
				if BS[4*k + i][4*l + i] == oppFlag:
					countOtherFDiagonal += 1
				if BS[4*k + i][4*l + i] == ownFlag:
					countSelfFDiagonal += 1

				# Checking Backward Diagonal
				if BS[4*k + 3-i][4*l + i] == oppFlag:
					countOtherBDiagonal += 1
				if BS[4*k + 3-i][4*l + i] == ownFlag:
					countSelfBDiagonal += 1

			# Evaluating Forward Diagonal
			if countOtherFDiagonal > 0 and countSelfFDiagonal > 0:
				if countOtherFDiagonal == 2:
					heurVal += 3
				elif countOtherFDiagonal == 3:
					heurVal += 8

			elif countSelfFDiagonal > 0:
				if countSelfFDiagonal == 2:
					heurVal += 3
				elif countSelfFDiagonal == 3:
					heurVal += 8

			# Evaluating Backward Diagonal
			if countOtherBDiagonal > 0 and countSelfBDiagonal > 0:
				if countOtherBDiagonal == 2:
					heurVal += 3
				elif countOtherBDiagonal == 3:
					heurVal += 8

			elif countSelfBDiagonal > 0:
				if countSelfBDiagonal == 2:
					heurVal += 3
				elif countSelfBDiagonal == 3:
					heurVal += 8

			# Winning/Losing Centre Blocks
			if((k==1 or k==2) and (l==1 or l==2)):
				if(bs[k][l] == ownFlag):
					heurVal += 10
				elif(bs[k][l] == oppFlag):
					heurVal -= 10

			# Winning/Losing Corner Blocks
			if((k==0 or k==3) and (l==0 or l==3)):
				if(bs[k][l] == ownFlag):
					heurVal += 8
				elif(bs[k][l] ==oppFlag):
					heurVal -= 8

			# Winning/Losing Blocks
			if bs[k][l] == ownFlag:
				heurVal += 20
			elif bs[k][l] == oppFlag:
				heurVal -= 20

	return heurVal


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

    ownFlag = 'o'
    oppFlag = 'x'

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
            countOther=0
            for i in range(4):
                if BS[4*k+3-i][4*l+i] == oppFlag:
                    fl = 1
                    countOther+=1
                    if k==1 and l==2:
                        print "oppflag"
                        print i
                if BS[4*k+3-i][4*l+i] == ownFlag:
                    countSelf+=1
                    if k==1 and l==2:
                        print "ownflag"
                        print
            if(fl == 0 and countSelf>0):
                if countSelf == 2:

                    heurVal += contCell2
                elif countSelf == 3:
                    heurVal += contCell3
            if(fl == 1 and countOther>0 and countSelf>0):
                if countOther == 2:
                    print "hello"
                    print k
                    print l
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
                        # print "aww yeah"
                        heurVal -= contCell2
                        # print heurVal
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
    print heurVal
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

def heuristics3(last_move,bs,BS):
    ownFlag = 'o'
    oppFlag = 'x'

    heurVal = 0

    # bs = boardCopy.block_status
    # BS = boardCopy.board_status

    ##############################################################
    # checking if this move helped us win block
    ##############################################################
    blockX = last_move[0]/4
    blockY = last_move[1]/4
    if bs[blockX][blockY] == ownFlag:
        heurVal+=50
    elif bs[blockX][blockY] == oppFlag:
        heurVal-=50
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
                heurVal += 10
            elif countSelf == 3:
                heurVal += 25
        if(fl == 1 and countOther>0 and countSelf>0):
            if countOther == 2:
                heurVal += 10
            elif countOther == 3:
                heurVal += 25

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
                heurVal += 10
            elif countSelf == 3:
                heurVal += 25
        if(fl == 1 and countOther>0 and countSelf>0):
            if countOther == 2:
                heurVal += 10
            elif countOther == 3:
                heurVal += 25

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
            heurVal += 10
        elif countSelf == 3:
            heurVal += 25
    if(fl == 1 and countOther>0 and countSelf>0):
        if countOther == 2:
            heurVal += 10
        elif countOther == 3:
            heurVal += 25

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
            heurVal += 10
        elif countSelf == 3:
            heurVal += 25
    if(fl == 1 and countOther>0 and countSelf > 0):
        if countOther == 2:
            heurVal += 10
        elif countOther == 3:
            heurVal += 25

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
                        heurVal += 3
                    elif countSelf == 3:
                        heurVal += 8
                if(fl == 1 and countOther>0 and countSelf>0):
                    if countOther == 2:
                        heurVal += 3
                    elif countOther == 3:
                        heurVal += 8

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
                        heurVal += 3
                    elif countSelf == 3:
                        heurVal += 8
                if(fl == 1 and countOther>0 and countSelf>0):
                    if countOther == 2:
                        heurVal += 3
                    elif countOther == 3:
                        heurVal += 8

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
                    heurVal += 3
                elif countSelf == 3:
                    heurVal += 8
            if(fl == 1 and countOther>0 and countSelf>0):
                if countOther == 2:
                    heurVal += 3
                elif countOther == 3:
                    heurVal += 8

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
                    heurVal += 3
                elif countSelf == 3:
                    heurVal += 8
            if(fl == 1 and countOther>0 and countSelf>0):
                if countOther == 2:
                    heurVal += 3
                elif countOther == 3:
                    heurVal += 8

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
                heurVal -= 10
            elif countOther == 3:
                heurVal -= 25
        if(fl == 1 and countSelf>0 and countOther>0):
            if countSelf == 2:
                heurVal -= 10
            elif countSelf == 3:
                heurVal -= 25

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
                heurVal -= 10
            elif countOther == 3:
                heurVal -= 25
        if(fl == 1 and countSelf>0 and countOther>0):
            if countSelf == 2:
                heurVal -= 10
            elif countSelf == 3:
                heurVal -= 25

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
            heurVal -= 10
        elif countOther == 3:
            heurVal -= 25
    if(fl == 1 and countSelf>0 and countOther>0):
        if countSelf == 2:
            heurVal -= 10
        elif countSelf == 3:
            heurVal -= 25

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
            heurVal -= 10
        elif countOther == 3:
            heurVal -= 25
    if(fl == 1 and countSelf>0 and countOther>0):
        if countSelf == 2:
            heurVal -= 10
        elif countSelf == 3:
            heurVal -= 25


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
                        heurVal -= 3
                    elif countOther == 3:
                        heurVal -= 8
                if(fl == 1 and countSelf>0 and countOther>0):
                    if countSelf == 2:
                        heurVal -= 3
                    elif countSelf == 3:
                        heurVal -= 8

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
                        heurVal -= 3
                    elif countOther == 3:
                        heurVal -= 8
                if(fl == 1 and countSelf>0 and countOther>0):
                    if countSelf == 2:
                        heurVal -= 3
                    elif countSelf == 3:
                        heurVal -= 8

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
                    heurVal -= 3
                elif countOther == 3:
                    heurVal -= 8
            if(fl == 1 and countSelf>0 and countOther>0):
                if countSelf == 2:
                    heurVal -= 3
                elif countSelf == 3:
                    heurVal -= 8

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
                    heurVal -= 3
                elif countOther == 3:
                    heurVal -= 8
            if(fl == 1 and countSelf>0 and countOther>0):
                if countSelf == 2:
                    heurVal -= 3
                elif countSelf == 3:
                    heurVal -= 8


    ####################################################################################
    #getting centre/corner squares in blocks AND getting squares in centre/corner blocks
    ####################################################################################
    for k in range(4):
        for l in range(4):

            #winning/losing centre block
            if( (k==1 or k==2) and (l==1 or l==2)):
                if(bs[k][l] == ownFlag):
                    heurVal += 10
                elif(bs[k][l] == oppFlag):
                    heurVal -= 10

            #winning/losing corner blocks
            if((k==0 or k==3) and (l==0 or l==3)):
                if(bs[k][l] == ownFlag):
                    heurVal += 8 #3
                elif(bs[k][l] ==oppFlag):
                    heurVal -= 8 #3

            #winning/losing blocks
            if bs[k][l] == ownFlag:
                heurVal += 20
            elif bs[k][l] == oppFlag:
                heurVal -= 20

            for i in range(4):
                for j in range(4):

                    #getting centre squares in blocks
                    if ((i==1 or i==2) and (j==1 or j==2)):
                        if BS[4*k+i][4*l+j] == ownFlag:
                            # print "centre square mila"
                            heurVal += 5
                        elif BS[4*k+i][4*l+j] == oppFlag:
                            # print "centre square kata"
                            heurVal -= 5

                    #getting corner squares in blocks
                    if ((i==0 or i==3) and (j==0 or j==3)):
                        if BS[4*k+i][4*l+j] == ownFlag:
                            # print "corner square mila"
                            heurVal += 5
                        elif BS[4*k+i][4*l+j] == oppFlag:
                            # print "corner square kata"
                            heurVal -= 5

                    #getting square in centre block
                    if ((k==1 or k==2) and (l==1 or l==2)):
                        if BS[4*k+i][4*l+j] == ownFlag:
                            # print "centre block me mila"
                            heurVal += 3
                        elif BS[4*k+i][4*l+j] == oppFlag:
                            # print "centre block me kata"
                            heurVal -= 3

                    #getting square in corner block
                    if ((k==0 or k==3) and (l==0 or l==3)):
                        if BS[4*k+i][4*l+j] == ownFlag:
                            # print "corner block me mila"
                            heurVal += 3
                        elif BS[4*k+i][4*l+j] == oppFlag:
                            # print "corner block me kata"
                            heurVal -= 3

    return heurVal



def heuristics(last_move,bs,BS):
    openMove = 15
    lastBlockWin = 50
    contBlock = [0,0,10,25]
    cutBlock = [0,0,10,25]
    contCell = [0,0,3,8]
    cutCell = [0,0,3,8]
    blockWin = 20
    blockWinCent = 10
    blockWinCor = 8
    cCell = 5
    cellOfC = 3

    ownFlag = 'o'
    oppFlag = 'x'

    heurVal = 0

    # bs = boardCopy.block_status
    # BS = boardCopy.board_status



    ##############################################################
    #checking if providing a free move
    ##############################################################
    # blockX = last_move[0]%4
    # blockY = last_move[1]%4
    # if bs[blockX][blockY]!='-':
    # 	if self.myMove:
    # 		heurVal-=openMove
    # 	else:
    # 		heurVal+=openMove



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
    #checking for continuous blocks or cutting other blocks and
    #					and same for other
    ##############################################################
    FDcountSelf=0
    FDcountOther=0
    FDflagSelf=0
    FDflagOther=0
    BDcountSelf=0
    BDcountOther=0
    BDflagSelf=0
    BDflagOther=0

    for i in range(4):

        #forward diagonal block part-1
        if bs[i][i] == ownFlag:
            FDcountSelf+=1
            FDflagSelf = 1
        elif bs[i][i] == oppFlag:
            FDcountOther+=1
            FDflagOther = 1

        #back diagonal block part-1
        if bs[3-i][i] == ownFlag:
            BDcountSelf += 1
            BDflagSelf = 1
        elif bs[3-i][i] == oppFlag:
            BDcountOther += 1
            BDflagOther = 1


        RWcountSelf=0
        RWflagSelf=0
        RWcountOther=0
        RWflagOther=0
        CLcountSelf=0
        CLflagSelf=0
        CLcountOther=0
        CLflagOther=0
        #loop for rows columns and cells
        for j in range(4):

            #winning/losing centre blocks
            if( (i==1 or i==2) and (j==1 or j==2)):
                if(bs[i][j] == ownFlag):
                    heurVal += blockWinCent
                elif(bs[i][j] == oppFlag):
                    heurVal -= blockWinCent

            #winning/losing corner blocks
            if((i==0 or i==3) and (j==0 or j==3)):
                if(bs[i][j] == ownFlag):
                    heurVal += blockWinCor #3
                elif(bs[i][j] ==oppFlag):
                    heurVal -= blockWinCor #3

            #winning/losing blocks
            if bs[i][j] == ownFlag:
                heurVal += blockWin
            elif bs[i][j] == oppFlag:
                heurVal -= blockWin


            #rows block part-1
            if bs[i][j] == ownFlag:
                RWcountSelf += 1
                RWflagSelf = 1
            elif bs[i][j] == oppFlag:
                RWcountOther += 1
                RWflagOther = 1

            #columns block part-1
            if bs[j][i] == ownFlag:
                CLcountSelf += 1
                CLflagSelf = 1
            elif bs[j][i] == oppFlag:
                CLcountOther += 1
                CLflagOther = 1

            CCSFD=0
            CFSFD=0
            CCOFD=0
            CFOFD=0
            CCSBD=0
            CFSBD=0
            CCOBD=0
            CFOBD=0
            # if bs[i][j] == '-':
            for k in range(4):

                #forward diagonal cell part-1
                if BS[4*i+k][4*j+k] == ownFlag:
                    CCSFD+=1
                    CFSFD=1
                elif BS[4*i+k][4*j+k]==oppFlag:
                    CCOFD+=1
                    CFOFD=1

                #back diagonal cell part-1
                if BS[4*i+3-k][4*j+k] == ownFlag:
                    CCSBD+=1
                    CFSBD=1
                elif BS[4*i+3-k][4*j+k]==oppFlag:
                    CCOBD+=1
                    CFOBD=1

                CCSRW=0
                CCORW=0
                CFSRW=0
                CFORW=0
                CCSCL=0
                CCOCL=0
                CFSCL=0
                CFOCL=0

                for l in range(4):

                    #row cell part-1
                    if BS[4*i+k][4*j+l] ==ownFlag:
                        CCSRW+=1
                        CFSRW=1
                    elif BS[4*i+k][4*j+l]==oppFlag:
                        CCORW+=1
                        CFORW=1

                    #col cell part-1
                    if BS[4*i+l][4*j+k] ==ownFlag:
                        CCSCL+=1
                        CFSCL=1
                    elif BS[4*i+l][4*j+k]==oppFlag:
                        CCOCL+=1
                        CFOCL=1


                #row cell part-2
                if CFSRW == 1:
                    if CFORW == 0:
                        heurVal+=contCell[CCSRW]
                    else:
                        heurVal+=cutCell[CCORW]
                if CFORW == 1:
                    if CFSRW == 0:
                        heurVal-=contCell[CCORW]
                    else:
                        heurVal-=cutCell[CCSRW]

                #col cell part-2
                if CFSCL == 1:
                    if CFOCL == 0:
                        heurVal+=contCell[CCSCL]
                    else:
                        heurVal+=cutCell[CCOCL]
                if CFOCL == 1:
                    if CFSCL == 0:
                        heurVal-=contCell[CCOCL]
                    else:
                        heurVal-=cutCell[CCSCL]

            #forward diagonal cell part-2
            if CFSFD == 1:
                if CFOFD == 0:
                    heurVal+=contCell[CCSFD]
                else:
                    heurVal+=cutCell[CCOFD]
            if CFOFD == 1:
                if CFSFD == 0:
                    heurVal-=contCell[CCOFD]
                else:
                    heurVal-=cutCell[CCSFD]

            #back diagonal cell part-2
            if CFSBD == 1:
                if CFOBD == 0:
                    heurVal+=contCell[CCSBD]
                else:
                    heurVal+=cutCell[CCOBD]
            if CFOBD == 1:
                if CFSBD == 0:
                    heurVal-=contCell[CCOBD]
                else:
                    heurVal-=cutCell[CCSBD]

        #rows block part-2
        if RWflagSelf == 1:
            if RWflagOther == 0:
                heurVal+=contBlock[RWcountSelf]
            else:
                heurVal+=cutBlock[RWcountOther]

        if RWflagOther == 1:
            if RWflagSelf == 0:
                heurVal-=contBlock[RWcountOther]
            else:
                heurVal-=cutBlock[RWcountSelf]


        #columns block part-2
        if CLflagSelf == 1:
            if CLflagOther == 0:
                heurVal+=contBlock[CLcountSelf]
            else:
                heurVal+=cutBlock[CLcountOther]

        if CLflagOther == 1:
            if CLflagSelf == 0:
                heurVal-=contBlock[CLcountOther]
            else:
                heurVal-=cutBlock[CLcountSelf]


    #forward diagonal block part-2
    if FDflagSelf == 1:
        if FDflagOther == 0:
            heurVal+=contBlock[FDcountSelf]
        else:
            heurVal+=cutBlock[FDcountOther]
    if FDflagOther == 1:
        if FDflagSelf == 0:
            heurVal-=contBlock[FDcountOther]
        else:
            heurVal-=cutBlock[FDcountSelf]

    #back diagonal block part-2
    if BDflagSelf == 1:
        if BDflagOther == 0:
            heurVal+=contBlock[BDcountSelf]
        else:
            heurVal+=cutBlock[BDcountOther]
    if BDflagOther == 1:
        if BDflagSelf == 0:
            heurVal-=contBlock[BDcountOther]
        else:
            heurVal-=cutBlock[BDcountSelf]


    ####################################################################################
    #getting centre/corner squares in blocks AND getting squares in centre/corner blocks
    ####################################################################################
    for k in range(4):
        for l in range(4):
            # if bs[k][l]=='-':
            for i in range(4):
                for j in range(4):

                    #getting centre squares in blocks
                    if ((i==1 or i==2) and (j==1 or j==2)):
                        if BS[4*k+i][4*l+j] == ownFlag:
                            # print "centre square mila"
                            heurVal += cCell
                        elif BS[4*k+i][4*l+j] == oppFlag:
                            # print "centre square kata"
                            heurVal -= cCell

                    #getting corner squares in blocks
                    if ((i==0 or i==3) and (j==0 or j==3)):
                        if BS[4*k+i][4*l+j] == ownFlag:
                            # print "corner square mila"
                            heurVal += cCell
                        elif BS[4*k+i][4*l+j] == oppFlag:
                            # print "corner square kata"
                            heurVal -= cCell

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
    return heurVal

def heuristics4(last_move,bs,BS):
    ownFlag = 'o'
    oppFlag = 'x'

    heurVal = 0

    # bs = boardCopy.block_status
    # BS = boardCopy.board_status

    ##############################################################
    # checking if this move helped us win block
    ##############################################################
    blockX = last_move[0]/4
    blockY = last_move[1]/4
    if bs[blockX][blockY] == ownFlag:
        heurVal+=50
    elif bs[blockX][blockY] == oppFlag:
        heurVal-=50
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
                heurVal += 10
            elif countSelf == 3:
                heurVal += 25
        if(fl == 1 and countOther>0 and countSelf>0):
            if countOther == 2:
                heurVal += 10
            elif countOther == 3:
                heurVal += 25

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
                heurVal += 10
            elif countSelf == 3:
                heurVal += 25
        if(fl == 1 and countOther>0 and countSelf>0):
            if countOther == 2:
                heurVal += 10
            elif countOther == 3:
                heurVal += 25

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
            heurVal += 10
        elif countSelf == 3:
            heurVal += 25
    if(fl == 1 and countOther>0 and countSelf>0):
        if countOther == 2:
            heurVal += 10
        elif countOther == 3:
            heurVal += 25

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
            heurVal += 10
        elif countSelf == 3:
            heurVal += 25
    if(fl == 1 and countOther>0 and countSelf > 0):
        if countOther == 2:
            heurVal += 10
        elif countOther == 3:
            heurVal += 25

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
                        heurVal += 3
                    elif countSelf == 3:
                        heurVal += 8
                if(fl == 1 and countOther>0 and countSelf>0):
                    if countOther == 2:
                        heurVal += 3
                    elif countOther == 3:
                        heurVal += 8

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
                        heurVal += 3
                    elif countSelf == 3:
                        heurVal += 8
                if(fl == 1 and countOther>0 and countSelf>0):
                    if countOther == 2:
                        heurVal += 3
                    elif countOther == 3:
                        heurVal += 8

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
                    heurVal += 3
                elif countSelf == 3:
                    heurVal += 8
            if(fl == 1 and countOther>0 and countSelf>0):
                if countOther == 2:
                    heurVal += 3
                elif countOther == 3:
                    heurVal += 8

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
                    heurVal += 3
                elif countSelf == 3:
                    heurVal += 8
            if(fl == 1 and countOther>0 and countSelf>0):
                if countOther == 2:
                    heurVal += 3
                elif countOther == 3:
                    heurVal += 8

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
                heurVal -= 10
            elif countOther == 3:
                heurVal -= 25
        if(fl == 1 and countSelf>0 and countOther>0):
            if countSelf == 2:
                heurVal -= 10
            elif countSelf == 3:
                heurVal -= 25

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
                heurVal -= 10
            elif countOther == 3:
                heurVal -= 25
        if(fl == 1 and countSelf>0 and countOther>0):
            if countSelf == 2:
                heurVal -= 10
            elif countSelf == 3:
                heurVal -= 25

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
            heurVal -= 10
        elif countOther == 3:
            heurVal -= 25
    if(fl == 1 and countSelf>0 and countOther>0):
        if countSelf == 2:
            heurVal -= 10
        elif countSelf == 3:
            heurVal -= 25

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
            heurVal -= 10
        elif countOther == 3:
            heurVal -= 25
    if(fl == 1 and countSelf>0 and countOther>0):
        if countSelf == 2:
            heurVal -= 10
        elif countSelf == 3:
            heurVal -= 25


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
                        heurVal -= 3
                    elif countOther == 3:
                        heurVal -= 8
                if(fl == 1 and countSelf>0 and countOther>0):
                    if countSelf == 2:
                        heurVal -= 3
                    elif countSelf == 3:
                        heurVal -= 8

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
                        heurVal -= 3
                    elif countOther == 3:
                        heurVal -= 8
                if(fl == 1 and countSelf>0 and countOther>0):
                    if countSelf == 2:
                        heurVal -= 3
                    elif countSelf == 3:
                        heurVal -= 8

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
                    heurVal -= 3
                elif countOther == 3:
                    heurVal -= 8
            if(fl == 1 and countSelf>0 and countOther>0):
                if countSelf == 2:
                    heurVal -= 3
                elif countSelf == 3:
                    heurVal -= 8

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
                    heurVal -= 3
                elif countOther == 3:
                    heurVal -= 8
            if(fl == 1 and countSelf>0 and countOther>0):
                if countSelf == 2:
                    heurVal -= 3
                elif countSelf == 3:
                    heurVal -= 8


    ####################################################################################
    #getting centre/corner squares in blocks AND getting squares in centre/corner blocks
    ####################################################################################
    for k in range(4):
        for l in range(4):

            #winning/losing centre block
            if( (k==1 or k==2) and (l==1 or l==2)):
                if(bs[k][l] == ownFlag):
                    heurVal += 10
                elif(bs[k][l] == oppFlag):
                    heurVal -= 10

            #winning/losing corner blocks
            if((k==0 or k==3) and (l==0 or l==3)):
                if(bs[k][l] == ownFlag):
                    heurVal += 8 #3
                elif(bs[k][l] ==oppFlag):
                    heurVal -= 8 #3

            #winning/losing blocks
            if bs[k][l] == ownFlag:
                heurVal += 20
            elif bs[k][l] == oppFlag:
                heurVal -= 20

            for i in range(4):
                for j in range(4):

                    #getting centre squares in blocks
                    if ((i==1 or i==2) and (j==1 or j==2)):
                        if BS[4*k+i][4*l+j] == ownFlag:
                            # print "centre square mila"
                            heurVal += 5
                        elif BS[4*k+i][4*l+j] == oppFlag:
                            # print "centre square kata"
                            heurVal -= 5

                    #getting corner squares in blocks
                    if ((i==0 or i==3) and (j==0 or j==3)):
                        if BS[4*k+i][4*l+j] == ownFlag:
                            # print "corner square mila"
                            heurVal += 5
                        elif BS[4*k+i][4*l+j] == oppFlag:
                            # print "corner square kata"
                            heurVal -= 5

                    #getting square in centre block
                    if ((k==1 or k==2) and (l==1 or l==2)):
                        if BS[4*k+i][4*l+j] == ownFlag:
                            # print "centre block me mila"
                            heurVal += 3
                        elif BS[4*k+i][4*l+j] == oppFlag:
                            # print "centre block me kata"
                            heurVal -= 3

                    #getting square in corner block
                    if ((k==0 or k==3) and (l==0 or l==3)):
                        if BS[4*k+i][4*l+j] == ownFlag:
                            # print "corner block me mila"
                            heurVal += 3
                        elif BS[4*k+i][4*l+j] == oppFlag:
                            # print "corner block me kata"
                            heurVal -= 3

    return heurVal


board = [['-' for i in range(16)] for j in range(16)]
block =[['-' for j in range(4)] for i in range(4)]

block[0][0]='x'
block[0][1]='x'
block[0][2]='x'
block[0][3]='o'

block[1][0]='x'
block[1][1]='x'
block[1][2]='o'

block[2][1]='x'
block[2][2]='o'
block[2][3]='o'

block[3][2]='o'
block[3][3]='o'

board[0][0]='x'
board[0][1]='x'

board[1][4]='x'
board[1][5]='x'
board[1][6]='x'

board[3][8]='x'
board[3][9]='x'
board[3][10]='o'

board[0][13]='x'
board[1][13]='x'
board[2][13]='o'
board[3][13]='x'
#
board[4][0]='o'
board[4][1]='o'

board[5][4]='o'
board[5][5]='o'
board[5][6]='o'

board[6][8]='o'
board[6][9]='o'
board[6][10]='x'

board[4][14]='o'
board[5][14]='o'
board[6][14]='x'
board[7][14]='o'

board[1][6]='o'
board[1][14]='o'
board[4][5]='x'
board[5][9]='x'
board[5][10]='x'
board[6][9]='o'
board[8][7]='x'
last_move = [12,12]
ans = heuristics5(last_move, block,board)
print heuristics(last_move,block,board)
print ans
# print block
# print board
