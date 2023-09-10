#include <stdio.h>

int len(char* n)
{
	int i = 0, j = 0;

	while(n[i++] != '\0')
		j++;

	return j;
}

int strsearch(char* n, char* k)
{
	int nl = len(n), kl = len(k),
		i = 0, j = 0;

	if(kl >= nl)
		return 0;

	for(; i < nl; i++) {
		j = 0;
		while(j < kl && n[i+j] == k[j])
			j++;

		if(j == kl)
			return 1;
	}

	return 0;
}

int
main()
{
	printf("%d\n", strsearch("poopyness", "ness"));
	return 0;
}
