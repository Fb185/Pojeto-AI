
import csv
import math

c = 0.9
global b
def train(X, validation_data):

    print("train")
    global p    # matrix p
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


    print("total words of spam: ", wspam)
    print("total words of ham: ", wham)
    return b, p


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
    test_emails = []
    with open(test_file, 'r', encoding='cp850') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            test_emails.append(row)


  # Calculate and return precision
    tentativas = 0
    tentativasCertas = 0
    tentativasIncorretas = 0
    emailsSpam = 0
    emailsHam = 0
    truePositives = 1
    trueNegatives = 0
    falsePositives = 1
    falseNegatives = 0

    for email in test_emails:
        classifier = classify(email, b, p)
        if classifier == email[0]:
            tentativasCertas += 1
            if classifier == "spam":
                truePositives += 1
            elif classifier == "ham":
                trueNegatives += 1
        else:
            tentativasIncorretas += 1
            if classifier == "spam":
                falsePositives += 1
            elif classifier == "ham":
                falseNegatives += 1
        if email[0] == "spam":
            emailsSpam += 1
        elif email[0] == "ham":
            emailsHam += 1
        tentativas += 1

    print("\nNaive Bayes: \n")
    print("O Algoritmo do Naive Bayes percorreu ", tentativas, "emails, sendo observado o seguinte: \n")
    print("Dos ", emailsSpam, "emails de spam, avaliou corretamente ", truePositives, " emails e ", emailsSpam - truePositives, " emails foram avaliados de forma incorreta.")
    print("Dos ", emailsHam, "emails de ham, avaliou corretamente ", trueNegatives, " emails e ", emailsHam - trueNegatives, " emails foram avaliados de forma incorreta.")
    print("A taxa de sucesso geral é de", ((tentativasCertas/tentativas) * 100), "% e uma taxa de insucesso geral de", ((tentativasIncorretas/tentativas * 100)), "% \n")
    print("Métricas de Classificação: \n")
    print("A Accuracy calculada é:", (tentativasCertas / tentativas))
    print("A Error rate calculada é:", (tentativasIncorretas / tentativas))
    print("A Sensivity calculada é:", (truePositives / (truePositives + falseNegatives)))
    print("A Specificity calculada é:", (trueNegatives / (trueNegatives + falsePositives)))
    print("A Precision calculada é:", (truePositives / (truePositives + falsePositives)))
    print("O Recall calculado é:", (truePositives / (truePositives + trueNegatives)))
    p = truePositives / (truePositives + falsePositives)
    r = truePositives / (truePositives + trueNegatives)
    print("A F-Measure calculada é:", ((2 * p * r) / (p + r)))
    print("O Geometric-mean calculado é:", math.sqrt(truePositives * trueNegatives))


    #Classificamos cada email como spam ou ham e retornamos -1 ou 1 

def main():
    X = './data/shortdataset.csv'
    # X = './data/spamHamDataset.csv'

    # Train classifier
    b, p = train(X, './data/validationSet.csv')

    # Test classifier on test dataset
    # test_file = './data/testSet.csv'
    # precision = evaluate(test_file, b, p)
    # print(f'Test precision: {precision:.9f}')

    # Test classifier on validation dataset
    validation_file = './data/validationSet.csv'
    evaluate(validation_file, b, p)
    # performanceNaiveBayes(validation_file)
