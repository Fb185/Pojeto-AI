import pdb
import json
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



    

