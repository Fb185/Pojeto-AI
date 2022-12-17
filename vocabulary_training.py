import pdb
import csv
# import nltk
# from nltk.corpus import words # dilter for gibberish words
# TODO: switch this to open from the files it creates in if __name__ == "__main__":
spamWords = {}
hamWords = {}
# nltk.download('words')
# setOfWords = set(words.words()) # uses sets in order to not have duplicates

def determineProbabilityOfEachWord(spamWords, hamWords):
    for word in hamWords:
        hamWordProbability = hamWords[word][0]/len(hamWords)
        hamWords[word][1] = hamWordProbability

    for word in spamWords:
        spamWordsProbability = spamWords[word][0]/len(spamWords)
        spamWords[word][1] = spamWordsProbability


# TODO what to do about gibberish like "K..."
# TODO we assumed that k...give = k and give 
# TODO we also take in 123456789 as a word por agora
# TODO how to deal with punctuation
def buildVocabulary(currentEmail, tag):
    if(tag == 'spam'):
        # of each word given that it was in a ham(or spam) message
        for word in currentEmail:
            wordAttributes = [1, 0]  # position 0 is the number of occurences and position 1 is the probability
            word = word.lower()
            if word not in spamWords: # if the word is english
                spamWords.update({word:wordAttributes})
            elif word in spamWords:
                spamWords[word][0] +=1

    elif(tag == 'ham'):
        for word in currentEmail:
            wordAttributes = [1, 0]
            word = word.lower()
            if word not in hamWords:
                hamWords.update({word:wordAttributes})
            elif word in hamWords:
                hamWords[word][0] +=1
    determineProbabilityOfEachWord(spamWords, hamWords)

def removePunctuation(c):
    characterList = ["*", "!", "?", ",", "-", ".", "/", ";", "_", "{", "}", "%", ":", "(", ")", "<", ">"]
    for i in characterList:
        if(c==i):
            c = ""



if __name__ == "__main__":
    with open('data/spamHamDataset.csv') as file:
        dataset = csv.reader(file)
        pdb.set_trace()
        for row in dataset:
            tag = row[0]
            email = row[1]
            # for i in email:
            #     removePunctuation(email[i])

                    
            currentEmail = row[1].split(" ")
            buildVocabulary(currentEmail, tag)

    hamfile = open("./data/hamBag.txt", "w")
    hamfile.write(str(hamWords))
    hamfile.close()
    spamfile = open("./data/spamBag.txt", "w")
    spamfile.write(str(spamWords))
    spamfile.close()

