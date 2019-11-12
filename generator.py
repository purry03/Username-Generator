import random

# get user input
num = int(input("Number of words to generate: "))

# read word lists
with open('nouns.txt', 'r') as infile:
    nouns = infile.read().strip(' \n').split('\n')
with open('adjectives.txt', 'r') as infile:
    adjectives = infile.read().strip(' \n').split('\n')

# generate usernames
for i in range(num):

    # construct username    
    word1 = random.choice(adjectives).title()
    word2 = random.choice(nouns).title()
    username = '{}{}{}'.format(word1, word2, random.randint(1, 99))

    # success
    print(username)  
