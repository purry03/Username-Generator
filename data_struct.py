import random
import string

num = int(input("Number of words to generate: "))


for i in range(0,num):
    noun= open("nouns.txt","rt")
    adj = open("adjectives.txt","rt")
    adjnum = random.randint(0,1327)
    nounnum = random.randint(0,6801)
    postfixnum = str(random.randint(1,99))
    n=0
    word1=""
    word2=""
    for line in adj:
        if(n==adjnum):
            word1=line
        n+=1
    n=0
    for line in noun:
        if(n==nounnum):
            word2=line
        n+=1

    word1 = word1.strip()
    word2 = word2.strip()
    word1 = word1[0].upper() + word1[1:]
    word2 = word2[0].upper() + word2[1:]
    print(word1+word2+postfixnum)
