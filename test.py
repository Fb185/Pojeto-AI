import csv
import math

c = 0.1
def train(X):

  print("train")
  global p
  global dictionary
  global n
  # Read documents X and labels Y
  documents = []
  labels = []
  with open(X, 'r') as csv_file:
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
  print(mham)
  mspam = labels.count('spam')
  print(mspam)

  # Initialize b
  global b
  b = math.log(c) + math.log(mham) - math.log(mspam)

  # Initialize p with pij = i, wspam = n, wham = n
  p = [[0] * n for _ in range(2)]
  wspam = n
  wham = n

  # Count occurrence of each word
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
    print("wspam = ", wspam)
    print("wham = ", wham)


  # Normalize counts to yield word probabilities
  for j in range(n):
    p[0][j] = (p[0][j] + 1) / (wspam + 2)  # Add a small positive value to p[0][j] to prevent math domain error
    p[1][j] = (p[1][j] + 1) / (wham + 2)  # Add a small positive value to p[1][j] to prevent math domain error
  
  return b

def classify(test_file, b):
  # Read test data from CSV file
  test_documents = []
  test_labels = []
  with open(test_file, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
      test_documents.append(row[1])
      test_labels.append(row[0])

  # Classify test documents
  predictions = []
  for x in test_documents:
    score_threshold = -b
    for j in range(n):
      word = list(dictionary)[j]
      score_threshold += x.count(word) * (math.log(p[0][j]) - math.log(p[1][j]))

    if score_threshold > 0:
      predictions.append('spam')
    else:
      predictions.append('ham')

  # Calculate precision
  correct = 0
  for i in range(len(test_labels)):
    if test_labels[i] == predictions[i]:
      correct += 1
  precision = correct / len(test_labels)

  return precision


b = train("./data/shortdataset.csv")
precision = classify("./data/testSet.csv", b)
print(f'Precision: {precision:.9f}')


