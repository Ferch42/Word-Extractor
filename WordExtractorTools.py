from itertools import permutations


def Skip(word,gap=1):
	skips=[]

	for i in range(len(word)):
		if(i+gap <= len(word)):
			skips.append(word[0:i]+word[i+gap:len(word)])

	return skips

def Permutations(word,window=2):
	perm=[]

	for i in range(len(word)):

		segment= word[i:(i+window)]
		segment_permutations= [''.join(p) for p in permutations(segment)]

		for sp in segment_permutations:
				
			new_word=word[0:i]+sp+word[i+window:len(word)]
			if(new_word not in perm):
					
				perm.append(new_word)

	return perm

def PhoneticSubstitutions(word,phonemes):
	subs=[]

	for phoneme in phonemes:
		#The first represent the phoneme that is being tested, the second the phoneme 
		#that is being substituted
		p1=phoneme[0]
		p2=phoneme[1]

		if(p1 in word):
			for i in range(len(word)):	
				if(i+len(p1) < len(word)):
					if(word[i:i+len(p1)] == p1):
						subs.append(word[0:i]+p2+word[i+len(p1):len(word)])

	return subs

def VowelSubstitutions(word):
	subs=[]
	vowels=['a','e','i','o','u']

	for i in range(len(word)):
		if(i+1<len(word)):
			if(word[i] in vowels):
				for v in vowels:
					new_word=word[0:i]+v+word[i+1:len(word)]
					if(new_word not in subs):
						subs.append(new_word)

	return subs


