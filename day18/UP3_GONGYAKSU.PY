yaksu_a = []
yaksu_b = []
gongyaksu=[]

a=input()
b=input()

for x in range (1,a+1):
	if a % x == 0:
		yaksu_a.append(x)
print yaksu_a

for x in range (1,b+1):
	if b % x == 0:
		yaksu_b.append(x)
print yaksu_b


for x in yaksu_a:
	for i in yaksu_b:
		if x == i :
			gongyaksu.append(x)
			
print gongyaksu