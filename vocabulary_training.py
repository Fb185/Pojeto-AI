import pdb
import csv
import nltk
from nltk.corpus import words # dilter for gibberish words
# TODO: switch this to open from the files it creates in if __name__ == "__main__":
spamWords = {}
hamWords = {}
nltk.download('words')
setOfWords = set(words.words()) # uses sets in order to not have duplicates

def determineProbabilityOfEachWord(spamWords, hamWords):
    for word in hamWords:
        hamWordProbability = hamWords[word][0]/len(hamWords)
        hamWords[word][1] = hamWordProbability

    for word in spamWords:
        spamWordsProbability = spamWords[word][0]/len(spamWords)
        spamWords[word][1] = spamWordsProbability


def buildVocabulary(currentEmail, tag):
    if(tag == 'spam'):
        wordAttributes = [1, 0]  # position 0 is the number of occurences and position 1 is the probability
        # of each word given that it was in a ham(or spam) message
        for word in currentEmail:
            word.lower()
            if word in setOfWords and word not in spamWords: # if the word is english
                spamWords.update({word:wordAttributes})
                wordAttributes[0]+=1
            elif word in setOfWords and word in spamWords:
                spamWords[word][0] +=1

    elif(tag == 'ham'):
        wordAttributes = [1, 0]
        for word in currentEmail:
            word.lower
            if word in setOfWords and word not in hamWords:
                hamWords.update({word:wordAttributes})
                wordAttributes[0]+=1
            elif word in setOfWords and word in hamWords:
                hamWords[word][0] +=1
    determineProbabilityOfEachWord(spamWords, hamWords)



if __name__ == "__main__":
    with open('data/spamHamDataset.csv') as file:
        dataset = csv.reader(file)
        for row in dataset:
            tag = row[0]
            currentEmail = row[1].split(" ")
            buildVocabulary(currentEmail, tag)

    hamfile = open("hamBag.txt", "w")
    hamfile.write(str(hamWords))
    hamfile.close()
    spamfile = open("spamBag.txt", "w")
    spamfile.write(str(spamWords))
    spamfile.close()

