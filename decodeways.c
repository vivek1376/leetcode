// AC
// TODO: make recursive

#include <stdio.h>
#include <string.h>
#include <stdlib.h>


int numDecodings(char* s) {
    int i, num, w1, w2, len, *ways;

    char letterString[2] = "";
    
    len = strlen(s);
        
    ways = (int *)malloc(len * sizeof(int));

    ways[len - 1] = (s[len - 1] == '0' ? 0 : 1);
    
    for (i = len - 2; i >= 0; i--) {
	if (s[i] == '0') {
	    ways[i] = 0;
	} else {
	    w1 = ways[i+1];

	    letterString[0] = s[i];
	    letterString[1] = s[i+1];

	    num = atoi(letterString);
	    if (num <= 26) {
		if ((i + 2) >= len)
		    w2 = 1;
		else
		    w2 = ways[i+2];
	    } else {
		w2 = 0;
	    }

	    ways[i] = w1 + w2;
	}
    }

    return ways[0];
}

int main()
{
    printf("%d\n", numDecodings("10"));
    return 0;
}
