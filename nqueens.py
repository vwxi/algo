C=[]
S=[]
Pd=[]
Nd=[]
k=[]

def good(x,y):
	global C, Pd, Nd
	return x not in C and x+y not in Pd and x-y not in Nd
	
# find all solutions to the N-Queens problem
def n(d,N,r):
	global S,C,Pd,Nd,k

	if N == d: 
		board=[["." for _ in range(d)] for _ in range(d)]
		for i,j in S: board[i][j] = "Q"
		k += [["".join(i) for i in board]]
		return True

	for i in range(d):
		if not good(i,r): continue

		C += [i]
		Pd += [i+r]
		Nd += [i-r]
		S += [(i, r)]

		n(d,N+1,r+1)

		S.remove((i, r))
		Nd.remove(i-r)
		Pd.remove(i+r)
		C.remove(i)

from sys import argv
n(int(argv[1]),0,0)
print(k)
