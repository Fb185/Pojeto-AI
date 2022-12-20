import pdb
from vocabulary_training import *
import json



    
def naiveBayes(hamBag, spamBag):
    spamEmailCounter = 0
    hamEmailCounter = 0
    #calculate the score of an email given that it is spam
    emailScore = 0
    with open("./testHam.csv") as th:
        testHam = csv.reader(th)
        for row in testHam:
            for word in row:
                pdb.set_trace()
                emailScore = spamWords.get(word)



    with open("./testSpam.csv") as ts:
        testSpam = csv.reader(ts)

with open("./data/spamBag.txt") as sp:
    spam = sp.read()
    spam = spam.replace("\'", "\"")
    spamBag = json.loads(spam)

with open("./data/hamBag.txt") as hb:
    ham = hb.read()
    ham = ham.replace("\'", "\"")
    hamBag = json.loads(ham)



hamPriorProbability = len(hamBag)/(len(hamBag) + len(spamBag))
spamPriorProbability = len(spamBag)/(len(spamBag) + len(hamBag))
print("hamPriorProbability = ", hamPriorProbability)
print("spamPriorProbability = ", spamPriorProbability)

naiveBayes(hamBag, spamBag)
    

