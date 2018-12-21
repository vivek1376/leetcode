// AC
// TODO: make recursive

#include <stdio.h>
#include <string.h>
#include <stdlib.h>


int numDecodings(char* s) {
    int i, num, w1, w2, len, *ways;

    len = strlen(s);

    /* store no. of total ways for string s[i] in ways[i],
       ways[0] will be final solution */
    ways = (int *)malloc(len * sizeof(int));

    ways[len - 1] = (s[len - 1] == '0' ? 0 : 1);

    for (i = len - 2; i >= 0; i--) {
	if (s[i] == '0') {
	    /* vaild string can't start with '0' */
	    ways[i] = 0;
	    continue;
	}

	/* if decoding current character individually */
	w1 = ways[i+1];

	/* if grouping current character with next character,
	   it shouldn't be greater than '26' */

	/* convert to int */
	num = (s[i] - 48) * 10 + (s[i+1] - 48);

	if (num > 26) {
	    w2 = 0;
	} else {
	    w2 = (i + 2) >= len ? 1 : ways[i+2];
	}

	ways[i] = w1 + w2;
    }

    return ways[0];
}

int main()
{
    printf("%d\n", numDecodings("10"));
    return 0;
}
