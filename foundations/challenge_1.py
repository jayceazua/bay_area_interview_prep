# Former Google Coding Interview Question: https://techdevguide.withgoogle.com/paths/foundational/find-longest-word-in-dictionary-that-subsequence-of-given-string/#!
# Find longest word in dictionary that is a subsequence of a given string.

# The Challenge
# Given a string S and a set of words D, find the longest word in D that is a subsequence of S.

# Word W is a subsequence of S if some number of characters, possibly zero, can be deleted from S to form W, without reordering the remaining characters.

# Note: D can appear in any format(list, hash table, prefix tree, etc.)

# For example, given the input of S="abppplee" and D={"able", "ale", "apple", "bale", "kangaroo"} the correct output would be "apple"

# The words "able" and "ale" are both subsequences of S, but they are shorter than "apple".
# The word "bale" is not a subsequence of S because even though S has all the right letters, they are not in the right order.
# The word "kangaroo" is the longest word in D, but it isn't a subsequence of S.

# Learning objectives
# This question gives you the chance to practice with algorithms and data structures.
# It’s also a good example of why careful analysis for Big-O performance is often worthwhile,
# as is careful exploration of common and worst-case input conditions.

# An optimal O(N + L) approach for any alphabet
# Instead of processing the words one at a time, we will process all words simultaneously.

# First, for each word w in D, create a 2-tuple containing w and the number 0 (i.e. (w, 0)).
# The number refers to the number of characters in w that have already been found in S
# initially, no characters have been found.
# For a tuple t, we'll refer to the word as t.w, and to the number as t.i(since it is an index).

# Group the words by t.w[t.i](initially t.i is 0, so initially it is by first letter).
# For our example dictionary D = {"able", "ale", "apple", "bale", "kangaroo"}, we’ll have.
