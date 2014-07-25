
guess_frequency=0
strike=0


# random--------------------------------------------------------------------------------------------------------------------------------------------
import random

number = random.sample(range(0,10),4)

if number[0] : random.sample(range(0,10),4)

print number
while strike!=4:
	guess_frequency += 1
	# guess----------------------------------------------------------------------------------------------------------------------------------------
	guess_number=[]
	zzz = 0

	for o in range(4): 
		guess=input("GUESS! "+ str(o+1) + "/4 :  ")
		guess_number.append(guess)
		for p in range(0,o):
			if guess_number[p] == guess_number[o]:
				zzz+=1
				break
	print guess_number
	if zzz != 0:
		print "jungbok : " +str(zzz)+ "      NOT JUNGBOK!"
		continue

	# strike----------------------------------------------------------------------------------------------------------------------------------------
	strike=0
	for g in range(4):
		if guess_number[g]== number[g]:
			strike+=1
	print str(strike)+ " Strike"
	# ball----------------------------------------------------------------------------------------------------------------------------------------
	ball=0

	for gn in guess_number:
		for n in number:
			if gn == n :
				ball+=1
	ball -= strike

	print str(ball)+ " Ball"

# game end----------------------------------------------------------------------------------------------------------------------------------------
if strike == 4:
	print "YOU WIN"
	print "turn : " + str(guess_frequency)