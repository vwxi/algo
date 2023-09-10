# make a failing function
def mkf(W):
	T = [0]*len(W)
	T[0] = 0

	for i in range(1, len(W)):
		j = T[i - 1]

		while j != 0 and W[j] != W[i]:
			j = T[j - 1]
		
		if j == 0 and W[j] != W[i]:
			T[i] = 0
		else:
			T[i] = j + 1

	return W, T

# search for W in S
def search(W,S):
	T = mkf(W)[1]

	i = 0 # W ctr
	j = 0 # S ctr

	while j < len(S):
		if W[i] == S[j]:
			i += 1
			j += 1

			if i == len(W):
				return j - i
		else:
			if i == 0: j += 1
			else: i = T[i]

	return -1

# test cases
print(search("fox", "The white fox jumps over the black dog"))
