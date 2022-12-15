import pdb
import json
with open("./spamBag.txt") as spamBag:
    spam = spamBag.read()
    spam = spam.replace("\'", "\"")
    spamBag = json.loads(spam)

with open("./hamBag.txt") as hamBag:
    ham = hamBag.read()
    ham = ham.replace("\'", "\"")
    hamBag = json.loads(ham)

global hamPriorProbability == len(hamBag)/(len(hamBag) + len(spamBag))
global spamPrioroProbability
    
