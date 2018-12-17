#!/usr/bin/env python3


def lenSubstring(string, k):
	print(string)
	
	count = [0] * 26
	lastIndex = [0] * 26

	unique = 0

	#sLen = len(string)

	len1 = 0
	maxLen = 0
	i = 0
	current = 0

	while True:
		count[ord(string[current]) - 97] += 1
		lastIndex[ord(string[current]) - 97] = current

		if count[ord(string[current]) - 97] == 1:
			unique += 1

		len1 += 1

		if unique > k :
			print("i_char: " + string[i] + "   current: " + str(current))

			# remove
			ch = string[i]

			#print("h1")
			#print("lastIndex[ord(ch) - 97] + 1")
			#print("=h1")

			for m in range(i, lastIndex[ord(ch) - 97] + 1):
				
				len1 -= 1
				print("m: " + str(m) + "   len1: " + str(len1))
				if count[ord(string[m]) - 97] > 0:					
					count[ord(string[m]) - 97] -= 1

					if count[ord(string[m]) - 97] == 0:
						unique -= 1



			i = lastIndex[ord(ch) - 97] + 1
			#len1 = 1

		else:

			
			print("else " + str(current) + "   len: " + str(len1))
			if len1 > maxLen:
				maxLen = len1

		#print(string[current])

		current += 1
		#print("current:" + str(current))
		#print(current)
		#print(len(string))
		if (current == len(string)):
			break 


	print("maxlen:" + str(maxLen))
	print(string[i:current])

#lenSubstring("aabacbebebe", 3)
#lenSubstring("abcbbca", 2)
lenSubstring("aaabbb", 3)
