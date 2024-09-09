# Task 5: Write a program to find the most frequent word in a text file.
import string
from collections import Counter
def find_most_frequent_word(filename):
    try:
        with open(filename,'r',encoding="utf-8") as file:
            test = file.read()
    except FileNotFoundError:
        print(f"The file {filename} was not found.")
        return None

    text = text.lower().translate(str.maketrans('','',string.punctuation))
    words = text.split()
    word_count = Counter(words)
    most_frequent_word = word_count.most_common(1)[0]
    print(f"The most frequent word is '{most_frequent_word[0]}'with {most_frequent_word[1]} occurences.")
    return most_frequent_word

filename = 'example.txt'
find_most_frequent_word(filename)