	string="Python is easy"
	words=string.split()
	reversed_words=[]
	for word in words:
	    reversed_word=" "
	    i=len(word)-1
	    while i>=0:
	      reversed_word+=word[i]
	      i-=1
	    reversed_words.append(reversed_word)
	reversed_words=" ".join(reversed_words)
	print(reversed_words)