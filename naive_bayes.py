
import csv
import math

c = 1
global b
def train(X, validation_data):

    print("train")
    global p
    global dictionary
    global n
    # Read documents X and labels Y
    documents = []
    labels = []
    # encoding = 'cp850'
    with open(X, 'r', encoding='cp850') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            documents.append(row[1])
            labels.append(row[0])

  # Compute dictionary D of X with n words
    dictionary = set()
    for document in documents:
        words = document.split()
        for word in words:
            dictionary.add(word)
    n = len(dictionary)

  # Compute m, mham, and mspam
    m = len(documents)
    mham = labels.count('ham')
    mspam = labels.count('spam')

  # Initialize b
    b = math.log(c) + math.log(mham) - math.log(mspam)

  # Initialize matrix p with pij = i, wspam = n, wham = n
    p = [[0] * n for _ in range(2)]
    wspam = n
    wham = n

  # Counts occurrence of each word
    for i in range(m):
        if labels[i] == 'spam':
            for j in range(n):
                word = list(dictionary)[j]
                p[0][j] += documents[i].count(word)
                wspam += documents[i].count(word)
        else:
            for j in range(n):
                word = list(dictionary)[j]
                p[1][j] += documents[i].count(word)
                wham += documents[i].count(word)


  # Normalize counts to yield word probabilities
    for j in range(n):
        p[0][j] = (p[0][j]+1) / (wspam + 2)  # Add a small positive value to p[0][j] to prevent math domain error
        p[1][j] = (p[1][j]+1) / (wham + 2)  # Add a small positive value to p[1][j] to prevent math domain error

    # validation_documents, validation_labels = validation_data
    # correct = 0
    # for i in range(len(validation_labels)):
    #     score_threshold = 0
    #     for j in range(n):
    #         word = list(dictionary)[j]
    #         score_threshold += validation_documents[i].count(word) * (math.log(p[0][j]) - math.log(p[1][j]))

    #     if score_threshold > 0 and validation_labels[i] == 'spam':
    #         correct += 1
    #     elif score_threshold <= 0 and validation_labels[i] == 'ham':
    #         correct += 1

    # precision = correct / len(validation_labels)

    print("total words of spam: ", wspam)
    print("total words of ham: ", wham)
    return b, p#, precision


def classify(x, b, p):
  # Initialize score threshold t = -b
    t = -b

  # Loop through words in dictionary
    for j in range(n):
        t += x.count(list(dictionary)[j]) * (math.log(p[0][j]+1) - math.log(p[1][j]+1))

  # Classify document based on score threshold
    if t > 0:
        return 'spam'
    else:
        return 'ham'

def evaluate(test_file, b, p):
  # Read test data from CSV file
    test_documents = []
    test_labels = []
    with open(test_file, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            test_documents.append(row[1])
            test_labels.append(row[0])

    # print(len(test_documents), len(test_labels))
  # Classify test documents and compare to true labels
    correct = 0
    for i in range(len(test_documents)):
        prediction = classify(test_documents[i], b, p)
        # print("email:", test_documents[i], "label:", test_labels[i])
        # print("prediction:", prediction)
        # print("")
        if prediction == test_labels[i]:
            correct += 1

  # Calculate and return precision
    precision = correct / len(test_labels)
    return precision

def main():
    # X = './data/shortdataset.csv'
    X = './data/spamHamDataset.csv'

    # Train classifier
    b, p = train(X, './data/validationSet.csv')

    # Test classifier on test dataset
    test_file = './data/testSet.csv'
    precision = evaluate(test_file, b, p)
    print(f'Test precision: {precision:.9f}')

    # Test classifier on validation dataset
    validation_file = './data/validationSet.csv'
    precision = evaluate(validation_file, b, p)
    print(f'Validation precision: {precision:.9f}')
