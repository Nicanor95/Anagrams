#!/usr/bin/env py

from itertools import permutations
import enchant
import sys

if len(sys.argv) <= 1:
	print("Usage: anagrams.py <word> [word] ...")
	print("It will iterate over all words and return possible solutions.")

# Set up the dictionary.
dictionary = enchant.Dict("en_US")

# Iterate over args.
for i, word in enumerate(sys.argv[1:], start=1):
	# We make a list of all iterations, may take some time depending on length,
	# enchant.suggest(word) doesn't cut it.
	# For each permutation, check if it's an english word and save in words.
	words = filter(dictionary.check, map(lambda x: "".join(x), permutations(word)))

	# Print out results
	print("For the string {} we found the following results:".format(word))
	for w in words:
		print(w)
	
	# Make suggestions
	suggestions = dictionary.suggest(word)
	if suggestions:
		print("Consider the following suggestions: ")
		for s in suggestions:
			print(s)
	
	# Make separator
	if i < len(sys.argv) -1:
		print("--------------------------------------------")