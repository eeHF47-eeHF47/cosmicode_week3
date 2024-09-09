# Task 3: Write a program to find the longest word in a sentence provided by the user, ignoring punctuation.
import string

def find_longest_word(sentence):
    sentence = sentence.translate(str.maketrans('','',string.punctuation))
    words = sentence.split()

    # find the longest word
    longest_word = max(words, key = len)
    return longest_word

sentence ="The quick brown fox jumping over the lazy dog."
longest_word = find_longest_word(sentence)
print("Longest word: ",longest_word)