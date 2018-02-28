import sys 
import Levenshtein
from WordExtractorTools import Skip, Permutations,PhoneticSubstitutions,VowelSubstitutions
from time import time
#Global Variables
permutation_window=2
skip_gap=1

#Input files
Dictionary={}
REP={}
try:
	Dictionary=open('pt-words-cleaned-4.txt','r',encoding='utf-8').readlines()
	REP=open('REP.txt','r',encoding='utf-8').readlines()
except OSError:
	print('Cannot open files')

#Cleaning up
Dictionary= [word.replace("\n","") for word in Dictionary]
Dictionary= set(Dictionary)
REP= [phoneme.replace("\n","") for phoneme in REP]
REP= [phoneme.split(" ") for phoneme in REP]
REP= [(phoneme[0],phoneme[1]) for phoneme in REP]

ConfusionPairs={}

for word in Dictionary:

	skips = Skip(word, gap=skip_gap)
	permutations = Permutations(word, window = permutation_window)
	phoneticsubstitutions = PhoneticSubstitutions(word,REP)
	vowelsubstitutions = VowelSubstitutions(word)

	possible_words=skips + permutations + phoneticsubstitutions + vowelsubstitutions

	ConfusionPairs[word]=[]
	for pw in possible_words:
		if(pw in Dictionary and pw not in ConfusionPairs.keys()):
			ConfusionPairs[word].append(pw)
	ConfusionPairs[word]=sorted(ConfusionPairs[word], key=lambda x: Levenshtein.distance(x,word))

for k in ConfusionPairs.keys():
	if(ConfusionPairs[k]!=[]):
		print(k+ " " +str(ConfusionPairs[k]))