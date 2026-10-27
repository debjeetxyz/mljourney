'''Write a program that takes a sentence and prints how many times each word appears.
~ Convert to lowercase and ignore punctuation (., ,, !, ?)
~ Use a dictionary
Input:  "the cat and the dog and the bird"
Output: {'the': 3, 'cat': 1, 'and': 2, 'dog': 1, 'bird': 1}'''

def wordCounter(s):
    s = s.lower()
    for p in [",",".","?",";",":","\"","\'"]:
        s = s.replace(p,"")
    wc = {}
    for i in s.split():
        if i in wc:
            wc[i] += 1
        else:
            wc[i] = 1
    print(wc)
       
string = input("Enter a line:")
wordCounter(string)