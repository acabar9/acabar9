a = input()

for b in range(a) :
	for u in range(a-(b+1)) : 
		print " ",
		
	for u in range(b+1) : 
		print "*",
	
	for u in range(b) : 
		print "*",

	print