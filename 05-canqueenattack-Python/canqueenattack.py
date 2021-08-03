# canQueenAttack(qX, qY, oX, oY) [15 pts]
# Given the position of the queen (qX, qY) and the opponent (oX, oY) on a chessboard. The task is to determine 
# whether the queen can attack the opponent or not. Note that the queen can attack in the same row, same column and 
# diagonally.

def canqueenattack(qR, qC, oR, oC):
	# Your code goes here
	if qR==oR or qC==oC or (abs(qR-oR)==abs(qC-oC)):
		return True
	
	# else:
	# 	for i in range (max(qR,qC,oR,oC)):
	# 		for j in range(max(qR,qC,oR,oC)):
	# 			if (oR==qR+i or oR==qR-i) and (oC==qC+i or oC==qC-i):
	# 				return True
	

	return False