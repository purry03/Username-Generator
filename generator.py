import random
import string
# get user input
num = int(input("Number of words to generate: "))
# read word lists
with open('nouns.txt', 'r') as infile:
    nouns = infile.read().strip(' \n').split('\n')
with open('adjectives.txt', 'r') as infile:
    adjectives = infile.read().strip(' \n').split('\n')
#read censor list
with open('blacklist.txt','r') as inline:
    censored = inline.read().strip(' \n').split('\n')
# generate usernames
for i in range(num):

    # construct username
    word1 = random.choice(adjectives)
    word2 = random.choice(nouns)
    #check if word2 is censored
    if word2 in censored:
        i -=1
        continue
    #else make and print the username
    #captilaize first letter
    word1 =word1.title()
    word2 =word2.title()
    username = '{}{}{}'.format(word1, word2, random.randint(1, 99))

    # success
    print(username)
