'''
ID:kyrazho1
LANG:PYTHON3
PROG:ride
'''
fin = open('ride.in','r')
fout = open('ride.out','w')

UFO = fin.readline()
comet = fin.readline()

UFOmul = 1
cometmul = 1

for char1 in range(0,len(UFO)):
	UFOmul *= ord(UFO[char1])-64

for char2 in range(0,len(comet)):
	cometmul *= ord(comet[char2])-64

#mod47
result = {}
if int(UFOmul % 47) == int(cometmul % 47):
	fout.write("GO"+"\n")
else:
	fout.write("STAY"+"\n")

fout.close()