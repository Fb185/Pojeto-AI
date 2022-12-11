import csv
import nltk
from nltk.corpus import words # dilter for gibberish words
# TODO: switch this to open from the files it creates in if __name__ == "__main__":
spamWords = {}
hamWords = {}
nltk.download('words')
setOfWords = set(words.words()) # uses sets in order to not have duplicates

def buildVocabulary(currentEmail, tag):
    if(tag == 'spam'):
        index = 1
        for word in currentEmail:
            if word.lower() in setOfWords and word.lower() not in spamWords: # if the word is english
                spamWords.update({word:index})
                index +=1
            if word.lower() in setOfWords and word.lower in spamWords:
                spamWords[word] +=1

    elif(tag == 'ham'):
        index = 1
        for word in currentEmail:
            if word.lower() in setOfWords and word.lower() not in hamWords:
                hamWords.update({word:index})
                index +=1
            if word.lower() in setOfWords and word.lower in hamWords:
                hamWords[word] +=1
            

if __name__ == "__main__":
    with open('data/spamHamDataset.csv') as file:
        dataset = csv.reader(file)
        count = 0
        for row in dataset:
            tag = row[0]
            currentEmail = row[1].split(" ")
            buildVocabulary(currentEmail, tag)
            # if (count > 5):
            #     break
            # count +=1
            # print(f"current email is {tag}\
            #         ham word count: {len(hamWords)}\
            #         spam word count:{len(spamWords)}")
            # print(f"ham words {hamWords}")

    hamfile = open("hamBag.txt", "w")
    hamfile.write(str(hamWords))
    hamfile.close()
    spamfile = open("spamBag.txt", "w")
    spamfile.write(str(spamWords))
    spamfile.close()

